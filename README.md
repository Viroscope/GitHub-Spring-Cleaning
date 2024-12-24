# GitHub Repository Manager

Welcome to the GitHub Repository Manager, a Python script designed to help you manage your GitHub repositories with ease. With this tool, you can back up all your repositories locally or delete them entirely from your account. Remember, use this script with caution—especially when deleting repositories!

## Features

- **Backup Repositories:** Clone all repositories from your GitHub account to a local directory.
- **Delete Repositories:** Permanently delete all repositories from your GitHub account.

## Prerequisites

Before using the GitHub Repository Manager, ensure you have the following:

1. **Python 3.x**: Make sure Python is installed on your system.
2. **Git**: Ensure that Git is installed and accessible via command line.
3. **Personal Access Token**: Generate a personal access token from [GitHub](https://github.com/settings/tokens) with appropriate permissions (repo access).

## Installation

To get started, clone this repository and install the required packages:


```git clone https://github.com/viroscope/Github-Spring-Cleaning.git && cd Github-Spring-Cleaning && pip install -r requirements.txt```


### Requirements

The script relies on two main libraries:
- `requests`: For making HTTP requests to the GitHub API.
- `gitpython`: To handle cloning of repositories.

## Usage

To run the program, execute:


```python main.py```


### Options

Upon running the script, you'll be presented with three options:

1. **Backup Repositories**
   - Enter your GitHub username and personal access token when prompted.
   - Specify the local directory where you'd like to save your backups.
   - The script will clone each of your repositories into the specified directory.

2. **Delete Repositories**
   - Enter your GitHub username and personal access token when prompted.
   - Confirm if you're sure about deleting all repositories (type 'yes' to proceed).
   - The script will attempt to delete each repository in your account.

3. **Exit**
   - Simply exits the program.

## Important Note

- Use caution when choosing the "Delete Repositories" option as it cannot be undone!
- Ensure that you've backed up any important data before proceeding with deletion.
- When backing up, it will not backup pre-existing projects in the backup directory.
- This is a choice, if for some reason it hangs, delete that dir and restart to ensure complete backup.

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for enhancements or bug fixes.

![image](https://github.com/user-attachments/assets/a8961aa4-d746-4f38-adb2-2856f3a19ece)
