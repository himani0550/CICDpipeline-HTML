import time
from github import Github

"""
This code uses the PyGithub module to monitor a GitHub repository for new commits.
It prints the SHA of the latest commit every 60 seconds if it has changed.
"""

# The repository URL
REPO_URL = "himani0550/CICDpipeline-HTML"

# Create a Github instance using an access token
g = Github("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")

# Get the repository object
repo = g.get_repo(REPO_URL)
# Initialize the last commit SHA to None
last_commit_sha = None

# Loop indefinitely
while True:
    # Try to get the commits from the repository
    try:
        commits = repo.get_commits()
        # Get the latest commit
        latest_commit = commits[0]
        # Check if the SHA has changed
        if last_commit_sha != latest_commit.sha:
            # Print the new commit SHA
            print(f"New commit: {latest_commit.sha}")
            # Update the last commit SHA
            last_commit_sha = latest_commit.sha
    except Exception as e:
        # Print the error message
        print(f"Error: {e}")

    # Try to sleep for 60 seconds
    try:
        time.sleep(60)
    except Exception as e:
        # Print the error message and exit the loop
        print(f"Error: {e}")
        break
