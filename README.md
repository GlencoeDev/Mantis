[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/GlencoeDev/Mantis/graphs/commit-activity)
[![Build Status](https://travis-ci.org/abhinavtripathy/XAuth.svg?branch=master)](https://travis-ci.org/GlencoeDev/Mantis/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](./LICENSE)


# Mantis
> Management Web Application with Dynamic Functionality

# Requirements  (Prerequisites)
Tools and packages required to successfully install this project.
For example:
* [Python 3.8 and up](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [pipenv](https://pipenv.readthedocs.io/en/latest/basics/install.html)

# Installation
A step by step list of commands / guide that informs how to install an instance of this project.
```sh
    pipenv shell
    pipenv sync
```
## Create and source the .env files
See included in the repo the .env sample file to create your .env file with all secret keys required :
```sh
    cd expensesapp
    source .env
    export DJANGO_SETTINGS_MODULE=mantisapi.settings.dev
```

## Run the server
To start the django server run the following command:
```sh
    python manage.py runserver
```
## Features
Here are the features of this project.
* Django admin dashboard configured
* Web application with dynamic functionality
* Etc Etc......

## Preparing to make a pull request
When making a pull request, please make sure to include the following:
* A detailed description of the changes you are making
* A test-plan for the changes
* Run the pre-commit hook to ensure that the changes are valid
* Run the tests to ensure that the changes are working as expected
* Commit the changes
* Push the changes to the remote repository

## How to run pre-commit hook
To run the pre-commit hook, run the following command:
```sh
    pre-commit install
    pre-commit run --all-files
```

## Deployment Notes
Coming soon.
# Authors
The Glencoe Software Canada Team:

Dami Adesola -> Project Manager
[<img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="25" height="20"/>](https://www.linkedin.com/in/damilola-adesola/)

Milo GoodFellow -> Software Developer
[<img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="25" height="20"/>](https://www.linkedin.com/in/damilola-adesola/)

Eric Scholtz -> Software Developer
[<img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="25" height="20"/>](https://www.linkedin.com/in/damilola-adesola/)

Alex Hemphill -> Software Developer
[<img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="25" height="20"/>](https://www.linkedin.com/in/damilola-adesola/)

Calvin Foote -> Software Developer
[<img src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" width="25" height="20" style="margin-left:10px"/>](https://www.linkedin.com/in/damilola-adesola/)

# License
GNU GENERAL PUBLIC LICENSE

Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed. This project is licensed under the GPL License - see the LICENSE.md file for details

Mantis © Glencoe Software
