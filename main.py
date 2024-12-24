import requests
from git import Repo
import os

def get_user_input():
    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub personal access token: ")
    return username, token

def get_all_repos(username, token):
    repos = []
    page = 1
    while True:
        response = requests.get(
            f'https://api.github.com/user/repos?page={page}&per_page=100',
            auth=(username, token)
        )
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            break
        
        batch = response.json()
        if not batch:
            break
        
        repos.extend(batch)
        page += 1
    
    return repos

def backup_repos(username, token):
    output_dir = input("Enter the directory where you want to back up your repositories: ")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    repos = get_all_repos(username, token)

    for repo in repos:
        repo_name = repo['name']
        clone_url = repo['clone_url']
        
        repo_path = os.path.join(output_dir, repo_name)
        
        if os.path.exists(repo_path):
            print(f"Skipping {repo_name} (already cloned).")
            continue
        
        try:
            print(f"Cloning {repo_name}...")
            Repo.clone_from(clone_url, repo_path)
        except Exception as e:
            print(f"Failed to clone {repo_name}: {e}")

    print("All repositories processed.")

def delete_repos(username, token):
    confirmation = input("Are you sure you want to delete all repositories? This action cannot be undone! (yes/no): ")
    
    if confirmation.lower() != 'yes':
        print("Deletion cancelled.")
        return

    repos = get_all_repos(username, token)

    for repo in repos:
        repo_name = repo['name']
        
        delete_url = f'https://api.github.com/repos/{username}/{repo_name}'
        
        response = requests.delete(delete_url, auth=(username, token))
        
        if response.status_code == 204:
            print(f"Deleted {repo_name}.")
        else:
            print(f"Failed to delete {repo_name}: {response.status_code} - {response.text}")

def main():
    while True:
        print("\nGitHub Repository Manager\n")
        print("1. Backup Repositories")
        print("2. Delete Repositories")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            username, token = get_user_input()
            backup_repos(username, token)
            
        elif choice == '2':
            username, token=get_user_input()
            delete_repos(username,token)
                
        elif choice=='3':
            break
        
        else:
            print("\nInvalid choice; try again.")
	
if __name__=="__main__":
	main()

