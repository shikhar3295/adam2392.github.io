Title: Setting Up a Virtual Environment for Python
Date: 2017-6-4
Category: Coding
Tags: virtualenv, webdev, python
Slug: setup-virtual-env
Authors: Adam Li
Summary: A short walkthrough of setting up a virtual environment for Python development.

# Getting Setup with Virtual Environment for Python Development
# By: Adam Li

### Table of Contents
<!-- MarkdownTOC autolink="true" bracket="round" -->

- [Installing](#installing)
- [Basics \(Create, Delete\):](#basics-create-delete)
    - [1. Create](#1-create)
    - [2. Delete a Virtualenv](#2-delete-a-virtualenv)
- [Tips](#tips)
    - [1. Starting up your Venv](#1-starting-up-your-venv)
    - [2. Requirements.txt](#2-requirementstxt)
- [Convenient Tools](#convenient-tools)
    - [1. Automatically cd To Project Directory](#1-automatically-cd-to-project-directory)
- [References:](#references)

<!-- /MarkdownTOC -->

VirtualEnv: 15.1.0
VirtualEnvWrapper

A virtual environment is useful for development in Python because it keeps your packages for certain projects separate from each other. It'll keep everything for that project separated in a separate wrapper.

# Installing
For virtualenvironment, follow https://virtualenv.pypa.io/en/stable/installation/

For virtualenvwrapper, follow http://virtualenvwrapper.readthedocs.io/en/latest/install.html

# Basics (Create, Delete):
## 1. Create

For Virtualenvwrapper: Run the command 

    'mkvirtualenv <envname>'

For Virtualenv: Run command 

    virtualenv './venv/' 

inside your project directory. or

    mkvirtualenv -p python3 

or

    virtualenv -p python3

to make the virtual environment with a specific python installation (e.g. 2.7, or 3.4). With python3.6 and most of the recent versions, the virtualenvironment is built in, so you can just run

    python3 -m venv <name_of_venv>

which is great because it handles it for you.

## 2. Delete a Virtualenv

For Virtualenvwrappper: In order to delete a virtual environment, all you need to do is to remove it recursively from your ~/.virtualenvs directory with    
    
    'sudo rm -rf <name>'.

For Virtualenv: Go to the directory of your project and delete the /venv/ directory.

# Tips
## 1. Starting up your Venv
Startup your virtual environment by typing:

    workon name_of_virtualenvironment

## 2. Requirements.txt
This is a convenient file for you to make that keeps track of all your packages. If you ever want to run your project on a new computer, you just create a new virtual environment and run:

    pip install -r requirements.txt

To create the file:

    pip freeze > requirements.txt

# Convenient Tools
## 1. Automatically cd To Project Directory
Input the following code to your ./virtualenvs/postactivate file

        # subtract strings to get the project name
        function get_project_name() {
            local venv_dir=$VIRTUALENVWRAPPER_HOOK_DIR
            local venv=$VIRTUAL_ENV

            temp_project_name=${venv#"$venv_dir"}   # get difference between two strings
            project_name=${temp_project_name:1}     # remove leading '/' character

            echo $project_name
            ## uncomment for debugging
            # echo $venv_dir
            # echo $venv
            # echo $temp_project_name
            # echo $project_name
        }

        # export proj="cd ~/Documents/$(get_project_name)"
        root_dir='/Users/adam2392/Documents/'
        project_dir=$(get_project_name)
        cd ${root_dir}/${project_dir}

Make sure you change 'root_dir' to the correct root directory of your projects. 

This assumes that your project directory files are all correspondingly named with your virtualenv. This is convenient for changing directory into your project directory automatically.


# References:
1. https://nolar.info/automatically-activate-virtualenv-on-cd/
- code to input into .bashrc