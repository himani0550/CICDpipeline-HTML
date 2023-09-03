import requests



repository_url = "https://api.github.com/repos/himani0550/CICDpipeline-HTML/commits"
headers = {"Authorization": "Bearer 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"}

response = requests.get(repository_url, headers=headers)

if response.status_code == 200:
    commits = response.json()
    # Process the commits as needed
else:
    print("Failed to fetch commits.")

