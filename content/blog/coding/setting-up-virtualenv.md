Title: Setting Up a Virtual Environment for Python
Date: 2017-6-4
Category: Python
Tags: virtualenv, webdev, python
Slug: setup-virtual-env
Authors: Adam Li
Summary: A short walkthrough of setting up a virtual environment for Python development.

# Getting Setup with Virtual Environment for Python Development
# By: Adam Li
<!-- MarkdownTOC autolink="true" bracket="round" -->

- [Basics \(Create, Delete\):](#basics-create-delete)
- [Tips](#tips)
- [Convenient Tools](#convenient-tools)
- [References:](#references)

<!-- /MarkdownTOC -->

VirtualEnv: 15.1.0
VirtualEnvWrapper

# Basics (Create, Delete):
1. Create
For Virtualenvwrapper: Run the command 'mkvirtualenv <envname>'

For Virtualenv: Run command virtualenv './venv/' inside your project directory

2. Delete a Virtualenv
For Virtualenvwrappper: In order to delete a virtual environment, all you need to do is to remove it recursively from your ~/.virtualenvs directory with 'sudo rm -rf <name>'.

For Virtualenv: Go to the directory of your project and delete the /venv/ directory.

# Tips


# Convenient Tools
1. Automatically cd to your project directory
Input the following code to your ./virtualenvs/postactivate file

'''
    #
    # subtract strings to get the project name
    #
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
'''

Make sure you change 'root_dir' to the correct root directory of your projects. This assumes that your project directory files are all correspondingly named with your virtualenv.

2. 

# References:
1. https://nolar.info/automatically-activate-virtualenv-on-cd/
- code to input into .bashrc
2. 