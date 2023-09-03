import requests, os

def check_for_new_commits():
    headers = {'Authorization': f'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'}
    url = f'https://api.github.com/repos/himani0550/CICDpipeline-HTML/commits?sha=prod'
    response = requests.get(url, headers=headers)
    commit_ids = []
    latest_commit_id = None

    if response.status_code == 200:
        commits = response.json()
        print(f'New commits found: {len(commits)}')
        for commit in commits:
            commit_ids.append({commit["sha"]})
        print(commit_ids)
    else:
        print(f'Error: {response.status_code}')
    
    if commit_ids and commit_ids[0] != latest_commit_id:
    # Do something

        latest_commit_id = commit_ids[0]
        # print(latest_commit_id)
        os.system('git pull origin prod')
        os.system('sudo cp -rf *.html /var/www/html/')
        os.system("sudo service nginx restart")


check_for_new_commits()