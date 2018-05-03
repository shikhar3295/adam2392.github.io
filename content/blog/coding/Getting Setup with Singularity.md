Title: Setting Up Singularity Containers
Date: 2018-01-31
Category: Coding
Tags: cloud, singularity, python, hpc, tensorflow
Slug: setup-singularity
Authors: Adam Li
Summary: A short walkthrough of setting up the Singularity containers
status: draft

# Getting Setup with Singularity
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC -->

- Installation
- Setting Up A Solidity Container Recipe
    - 1. Needed Docker Containers:
    - 2. Environment
    - 3. Post
    - 4. Run Script
- References:

<!-- /MarkdownTOC -->

# Installation
To install singularity locally with root privelages, you can then build up containers that can be hosted online.


# Setting Up A Solidity Container Recipe

    Bootstrap: docker
    From: tensorflow/tensorflow:latest-gpu

    %environment
      # use bash as default shell
      SHELL=/bin/bash
      export SHELL
    %setup
      # runs on host - the path to the image is $SINGULARITY_ROOTFS
    %post
      # post-setup script
      # load environment variables
      . /environment

      # use bash as default shell
      echo 'SHELL=/bin/bash' >> /environment

      # make environment file executable
      chmod +x /environment

      # default mount paths
      mkdir /scratch /data 

      # load in extra packages for python
      apt-get update && apt-get -y install locales
      locale-gen en_US.UTF-8
      apt-get install -y git wget python3-dev python3-pip
      apt-get clean

      apt-get install -y libcupti-dev
      pip3 install --upgrade pip
      pip3 install keras
      pip3 install numpy scipy scikit-learn pandas

    %runscript
      # executes with the singularity run command
      # delete this section to use existing docker ENTRYPOINT command

    %test
      # test that script is a success


## 1. Needed Docker Containers:
The best thing to do is start off with a docker container that is already prebuilt. The nice thing is that for cloud computing with tensorflow-gpu, tensorflow is maintained on docker and up to date. 

    Bootstrap: Docker
    From: tensorflow/tensorflow:latest-gpu

Other options are:

    Bootstrap: shub
    From:

## 2. Environment
These are commands that can be used to export variables into the environment.

## 3. Post

## 4. Run Script


# References:

