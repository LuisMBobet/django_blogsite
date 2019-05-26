#!/usr/bin/env bash

# Install linux dependencies
sudo apt-get install -y nginx # Proxy server
sudo apt-get install -y supervisor # To launch django app
sudo apt-get install -y ufw # Firewall control
sudo apt-get install -y mysql-server # Database
sudo apt-get install -y libmariadbclient-dev # Package to get mysql working with python3
sudo apt-get install -y python3-pip # Install pip3 to create virtual environment using python 3

sudo mysql_secure_installation
sudo mysql < deploy_database.sql # Create database


# Set up firewall to only allow incoming http and ssh connections
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw enable
sudo ufw reload

# Create python 3 virtual environment
pip3 install virtualenv
python3 -m virtualenv ve_py3
source ./ve_py3/bin/activate
pip install -r py3_requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
deactivate

# Setup supervisor, gunicorn and NGINX
sed 's/$USER/'"$USER"'/' supervisor.template.conf | sudo tee /etc/supervisor/conf.d/myBlog.conf
sed 's/$USER/'"$USER"'/' nginx.template | sudo tee /etc/nginx/sites-available/myBlog
sed 's/$USER/'"$USER"'/' gunicorn_start.template | tee ve_py3/bin/gunicorn_start
chmod u+x ve_py3/bin/gunicorn_start
sudo ln -s /etc/nginx/sites-available/myBlog /etc/nginx/sites-enabled

mkdir ve_py3/logs ve_py3/run

sudo systemctl enable supervisor
sudo systemctl restart supervisor

sudo rm /etc/nginx/sites-available/default
sudo systemctl restart nginx
