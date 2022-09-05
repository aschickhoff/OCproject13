<h1 align="center">OpenClassrooms Project 13</h1>

# Scale a Django Application Using Modular Architecture
> This is my project No. 13 for OpenClassrooms where I had to improve a company’s Django website, both in terms of the code and its deployment.

## Table of Contents
* [General Info](#general-information)
* [Postman documentation](#postman-documentation)
* [Prerequisite](#prerequisite)
* [Setup](#setup)


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
- Using Sentry so that uncaught exceptions are propagated through to the issues page of a Sentry project.

