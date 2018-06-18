Title: Setting Up Singularity Containers
Date: 2018-01-31
Category: Coding
Tags: cloud, singularity, python, hpc, tensorflow, deep-learning
Slug: setup-singularity
Authors: Adam Li
Summary: A short walkthrough of setting up the Singularity containers

# Getting Setup with Singularity
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC -->

- Installation
- Setting Up A Tensorflow Container Recipe \(Example\):
  - 1. Needed Docker Containers:
  - 2. Environment / Setup
  - 3. Post
  - 4. Run Script
  - 5. Test
- Common Commands
- Conclusions
- References:

<!-- /MarkdownTOC -->

# Installation
To install singularity locally with root privelages, you can then build up containers that can be hosted online.

# Setting Up A Tensorflow Container Recipe (Example):

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
      pip3 install numpy scipy scikit-learn pandas tensorboard natsorted tqdm
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

## 2. Environment / Setup
These are commands that can be used to export variables into the environment. Then you can run setup of files/variables before running any installations.

## 3. Post
This is the main area where your image will install different packages and load different environment variables.

## 4. Run Script
This will run a script afterwards, say a scientific experiment:
  
    python3 main.py --args

## 5. Test
This will run test scripts to see that your "main.py" did what it was supposed to do. Were files saved? Were computations correct?

# Common Commands
Pulling images, shelling into the image and executing the image with a script

    singularity pull

    singularity shell

    singularity exec 

Common argument flags:
* verbose mode(s): -v, -vv, -vvv
* debug mode: -d 
* link nvidia driver & GPU: --nv
* binds an existing directory onto the image: -B

An example use case that runs a tensorflow simg and runs a training script:

    singularity exec --nv ./tensorflow.simg python main.py ${traindatadir} ${testdatadir} --output_data_dir ${outputdatadir} --log_data_dir ${logdatadir} --patient_to_loo ${patient} --expname ${expname}


# Conclusions
This allows an end-to-end HPC/scientific computation analysis that uses Docker/Singularityhub to setup your system, and then runs setup, main scripts and testing to create a consistent output.

# References:
1. https://www.singularity-hub.org/
2. http://geekyap.blogspot.com/2016/11/docker-vs-singularity-vs-shifter-in-hpc.html
3. https://singularity.lbl.gov/docs-docker
