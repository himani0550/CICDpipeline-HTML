import requests
import os
# The repository URL
REPO_URL = "https://github.com/himani0550/CICDpipeline-HTML"
BRANCH_NAME = "prod"
WEB_DIR = "/var/www/html/"
def check_for_new_commits():
    headers = {'Authorization': 'token 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'}
    # Construct the URL to get the commits on the branch
    url = f"{REPO_URL}/commits?sha={BRANCH_NAME}"
    # Initialize the list of commit IDs and the latest commit ID to None
    commit_ids = []
    latest_commit_id = None

    # Try to get the commits from the repository
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        commits = response.json()
        print(f"New commits found: {len(commits)}")
        # Get the IDs of all the commits
        for commit in commits:
            commit_ids.append(commit["sha"])
        print(commit_ids)
    except requests.exceptions.RequestException as e:
        # Print the error message and exit the function
        print(f"Error: {e}")
        return
    if commit_ids[0] != latest_commit_id:
        latest_commit_id = commit_ids[0]
        print(latest_commit_id)
        # Pull the changes from the branch
        try:
            os.system("git pull origin prod")
            # Copy all HTML files to the web server directory
            os.system(f"sudo cp -rf {WEB_DIR}*.html {WEB_DIR}")
            # Restart the nginx service
            os.system("sudo service nginx restart")
        except Exception as e:
            # Print the error message
            print(f"Error: {e}")
check_for_new_commits()
