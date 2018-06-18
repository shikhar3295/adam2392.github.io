Title: Setting Up Postgre SQL
Date: 2018-06-17
Category: Coding
Tags: webdev, sql, postgres, macos
Slug: setup-postgresql
Authors: Adam Li
Summary: A short walkthrough of setting up postgre sql and some notes.
status: draft

# Getting Setup with PostgreSQL
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC -->

- Installation
- Set Up
    - 1a. Using a LaunchAgent and plist to Launch PostgreSQL on Startup
        - 1b. Manually Starting PostgreSQL
    - 2. Initializing Database
    - 3. Creating and Deleting Databases
    - 4.
        - 1c. Use Docker
- Testing
    - 1.
    - 2.
- Deployment
- References:

<!-- /MarkdownTOC -->

# Installation
The following packages need to be installed for a test time environment:

    brew update
    brew doctor
    brew install postgres

- Testrpc is an in-memory blockchain that can be used to test the development of the application.
- Web3 is essentially the web interface with the backend and frontend.
- Solc is a solidity code compiler
- Truffle is a web framework for building dAPPs using Ethereum

# Set Up
## 1a. Using a LaunchAgent and plist to Launch PostgreSQL on Startup
First, you’ll need to create a directory for your LaunchAgents to reside (if the directory doesn’t exist already). LaunchAgents in OS X are simple scripts used by launchd that cause the system to run programs or code during startup.

    mkdir -p ~/Library/LaunchAgents

Now you’ll need to create a symbolic link from the script that actually allows Postgres to run to the LaunchAgents directory. A symbolic link is similar to creating a new copy of a file for use in another directory, but since the link is ‘symbolic’, the link is just a forwarding address: any request made to that symbolic link location is actually “forwarded along” or redirected to where the real file actually resides.

    ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents

Note: Double-check that the command is correct: It should’ve been part of the installation output mentioned above when Homebrew installed Postgres initially.

Finally, we load the new symbolic linked LaunchAgent file using the launchctl load command, which is specifically what informs the computer to run this script and start Postgres when the computer launches. Again, the exact command to enter for your own installation will be an output during Homebrew’s Postgres installation, but it should look something like this:

    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

### 1b. Manually Starting PostgreSQL

    postgres -D /usr/local/var/postgres


## 2. Initializing Database


## 3. Creating and Deleting Databases



## 4. 

### 1c. Use Docker
Refer to https://medium.com/@leo_hetsch/local-development-with-go-postgresql-and-elasticsearch-in-docker-61bc8a0d5e66 for a nice little explanation for some common docker installation commands for postgresql and elastic search.

    docker-compose -f local.yml build

or 

    export COMPOSE_FILE=local.yml
    docker-compose up

Possible / common methods:
    
    docker-compose -f local.yml run --rm django python manage.py migrate
    docker-compose -f local.yml run --rm django python manage.py createsuperuser

Since docker is composed of a set of build commands, you should read up on the documentation here:

https://docs.docker.com/compose/compose-file/#resources

# Testing
## 1. 

## 2. 


# Deployment


# References:
1. http://boot2docker.io/
2. https://docs.docker.com/engine/examples/postgresql_service/#installing-postgresql-on-docker
3. https://chartio.com/resources/tutorials/how-to-start-postgresql-server-on-mac-os-x/
4. https://www.pubnub.com/blog/testing-and-deploying-an-ethereum-token-part-2/
