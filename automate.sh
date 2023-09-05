REPO_URL="https://github.com/himani0550/CICDpipeline-HTML"

# Clone the latest code
git clone $REPO_URL /var/www/automate
sudo service nginx restart
