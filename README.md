<h1 align="center">OpenClassrooms Project 13</h1>

# Scale a Django Application Using Modular Architecture
> This is my project No. 13 for OpenClassrooms where I had to improve a company’s Django website, both in terms of the code and its deployment.

## Table of Contents
* [General Info](#general-information)
* [Postman documentation](#postman-documentation)
* [Prerequisite](#prerequisite)
* [Setup](#setup)
* [Docker](#docker)
* [Deployment](#deployment)
* [Sentry](#sentry)


## General Information
- Original GitHub repository used: [OC Lettings](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings "OC Lettings")

### Areas of the site and deployment to be improved/added
#### Miscellaneous technical debt refactor
- Fixing the linting errors
- Ensuring the pluralization is correct in the admin section of the site

#### Modular architecture refactor
- Creating a new app lettings, containing the address and letting models and a new app profiles, containing the profile model
- Using Django migrations, to create new tables for the address, letting and profile models in the database
- Populating the new tables with the current data
- Renaming lettings_index.html to index.html and lettings_index view to index
- Moving the lettings and profiles URLs from oc_lettings_site into the new apps, keeping ROOT_URLCONF the same
- Moving the lettings and profiles views in oc_lettings_site and the templates in templates into lettings or profiles
- Using Django migrations to remove the old tables from the database
- Making oc_lettings_site not an app and removing the appropriate files.
- Creating tests so that pytest and flake8 should continue to be usable.

#### CI/CD pipeline using CircleCI and Heroku
- Creating a build-and-test job that replicates the local development environment
- Creating a containerization job that builds a Docker image of the site and pushes it to the Docker Hub container registry
- Creating a deploy-production job that deploys the site using Heroku

#### Production error logging using Sentry
- Using Sentry so that uncaught exceptions are propagated through to the issues page of a Sentry project

## Prerequisite
- [Python 3.10.4](https://www.python.org/ "Python") is installed
- You need a [GitHub](https://github.com/ "GitHub") account
- You need a [CirleCI](https://circleci.com/ "CirleCI") account
- You need a [Docker](https://www.docker.com/ "Docker") account
- You need a [Heroku](https://www.heroku.com/ "Heroku") account
- You need a [Sentry](https://sentry.io/ "Sentry") account
- [Git](https://git-scm.com/ "Git") is installed for a command-line interface
- [SQLite3](https://www.sqlite.org/index.html "SQLite3") is installed for a command-line interface
- [Docker](https://www.docker.com/ "Docker") is installed

## Setup
### Clone repository
```Bash
cd /path/to/project/
git clone https://github.com/aschickhoff/OCproject13.git
```
### Create and activate virtual environment
```Bash
cd /path/to/OCproject13/
python -m venv venv
.\env\Scripts\activate
```
### Install dependencies
```Bash
pip install -r requirements.txt
```
### Run the site
```Bash
python manage.py migrate
python manage.py runserver
```
Go to http://localhost:8000 in a browser to confirm the site is running and can be navigated.
### Linting
```Bash
flake8
```
### Unit tests
```Bash
pytest
```
### Database
- Open a shell session `sqlite3`
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profiles table, `pragma table_info(profiles_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`
- `.quit` to exit
### Admin panel
Go to http://localhost:8000/admin
Login with user `admin`, password `Abc1234!`

## Docker
### Run the app locally:
- Build the image `docker build -t <image-name> .`
- Run the image `docker run -dp 8080:8080 --env-file .env <image-name>`
You should be able to run the app at http://localhost:8080/
### Pull latest image from DockerHub
- `docker run -dp 8080:8080 aschickhoff/oc_lettings:latest`
You should be able to run the app at http://localhost:8080/

## Deployment
### Heroku
- Connect with Heroku `heroku login`
- Create Heroku app `heroku create <app-name> --region eu`
- Push repo to Heroku `git push heroku main`
- Run the app `heroku open`
You should be able to run the app at https://<app-name>.herokuapp.com/
### Deployment with CirleCI
1. Connect with CirleCI and link your account to your GitHub account
2. Go to `Projects` and choose your project from GitHub
3. Set the following environment variables in your CircleCi project
- `DOCKERHUB_IMAGE` your image name
- `DOCKERHUB_PASSWORD` your password for dockerhub
- `DOCKERHUB_USERNAME` your username for dockerhub
- `DSNkey` your Sentry key
- `HEROKU_API_KEY` your Heroku api key
- `HEROKU_APP_NAME` the Heroku app name
- `SECRET_KEY` your SecretKey for the repo
The next time you push your project to Github, CircleCI will run the following jobs:
- build-and-test
- build-and-push-to-dockerhub
- deploy-to-heroku

## Sentry
The Sentry error logging can be triggered by browsing the following url: https://<app-name>.herokuapp.com/sentry-debug/ or locally http://localhost:8000/sentry-debug (http://localhost:8080/sentry-debug/)

You can find an example here:
https://sentry.io/share/issue/57b1f5b10a0d447990fb3340cc873f81/