Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 intall virtualenv

## Nginx Virutal Host config

* see nginx.template.conf
* replace SITENAME with, eg, stating.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, stating.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/usename
 |--- sites
      |--- SITENAME
             |--- database
             |--- source
             |--- static
             |--- virutalenv
