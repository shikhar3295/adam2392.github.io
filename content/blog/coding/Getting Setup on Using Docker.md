Title: Setting Up Docker
Date: 2018-06-17
Category: Coding
Tags: webdev, docker, macos
Slug: setup-docker
Authors: Adam Li
Summary: A short walkthrough of setting up Docker and some notes on setting up a containerized approach to development with persistent database.
status: draft

# Getting Setup on Using Docker
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC -->

- Installation
- Setting Hardware Requirements:
- Using Docker
    - 1. Docker Image
        - 1a. Setting Base Docker Volume
        - 1b. Creating The Container
        - 1c. Running PostgreSQL via Container
        - 1d. \(Optional\) Expose Docker Container To Host
    - 2.
- Linking All This With Docker-Compose
    - 1.
- Common Commands
    - Images
    - Containers
    - Volumes
- Testing
    - 1.
    - 2.
- References:

<!-- /MarkdownTOC -->

# Installation
The following packages need to be installed for a test time environment:

    brew update
    brew prune
    brew doctor
    brew install postgres
    brew install docker

# Setting Hardware Requirements:
Some packages need minimum hardware requirements assigned to Docker usage.

A minimum of 4GB RAM assigned to Docker

Elasticsearch alone needs at least 2GB of RAM to run.

With Docker for Mac, the amount of RAM dedicated to Docker can be set using the UI: see How to increase docker-machine memory Mac (Stack Overflow).

# Using Docker
## 1. Docker Image
Most docker images have been prebuilt and tested online. Containers are these dynamic "images" of your system that will host data, programs, etc. Images are snapshots of those containers (mainly at the beginning) to setup the baseline container. 

Volumes are a way of allowing containers persistent storage across usage.

### 1a. Setting Base Docker Volume
This will create a docker with a volume (in the docker image) at the volume you specify with the "-v" tag. The docker image has the name that you set, and then it is based off of "busybox", which is a generalized light-weight docker image by Docker.

    docker create -v /var/lib/postgresql/data --name postgres10.4-data busybox

### 1b. Creating The Container

    docker run --name local-postgres10.4 -e POSTGRES_PASSWORD=dappstore -d --volumes-from postgres10.4-data postgres:10.4 

### 1c. Running PostgreSQL via Container

    docker run -it --link local-postgres10.4:postgres --rm postgres:10.4 sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

Enter the password you just set.

Inside, you can modify and begin the basic configuration of the base container volume by creating tables and initializing roles using SQL.

Now, your base container is set up! Don't remove this if you want to have persistant Postgresql set up.


### 1d. (Optional) Expose Docker Container To Host

    docker run --name local-postgres10.4 -p 5432:5432 -e POSTGRES_PASSWORD=asecurepassword -d --volumes-from postgres10.4-data postgres:10.4

This will expose the PostGRESQL docker instance via port 5432 localhost, so that you can connect to it via any application now.

## 2. 

# Linking All This With Docker-Compose
Docker-compose is a way of composing up the docker images that you have in a way that fits your needs. You can modularly stack docker images and then run additional installations that fit your specifications.

So, for example, here we will compose a docker image that is composed of django, postgres and elasticsearch to have a fully functional web-app with logging capabilities. (Perhaps we should also think about adding Kibana and Logstash for a full ELK stack)?

## 1.
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

# Common Commands

## Images
    docker image ls
    docker ps

    docker rmi <image_name>

## Containers
    docker container ls

## Volumes

# Testing
## 1. 

## 2. 


# References:
1. http://boot2docker.io/
2. https://ryaneschinger.com/blog/dockerized-postgresql-development-environment/
3. 