Title: Setting up Your Data Analysis
Date: 2017-9-25
Category: Coding
Tags: mac, os, data analysis, data science
Slug: setup-data-analysis
Authors: Adam Li
Summary: To guide the setup of a work station for data analysis.
status: draft
# Background

# OS Tools
#### 1. SSHFS
Link: https://github.com/libfuse/sshfs

Used for linking ssh to your remote file system for easy visualization.

#### 2. Virtual Environment
See my blog post on virtual environments.


#### 3. Jupyter Notebook
https://taufiqhabib.wordpress.com/2016/12/18/intalling-jupyter-in-a-virtualenv/


#### 4. Git


#### 5. R Notebook / IDE


#### 6. The Virtual Brain

    mkvirtualenv tvb
    pip install numpy scipy numexpr numba matplotlib 
    pip install ipython jupyter
    pip install nibabel networkx
    git clone https://github.com/the-virtual-brain/tvb-data
    git clone https://github.com/the-virtual-brain/tvb-library

Then in your project directory, create a launch_tvb.command file and add this:

    #!/bin/bash
    # add tvb data and library to path and launch notebook
    export PYTHONPATH=$(pwd)/tvb-data:$(pwd)/tvb-library:$PYTHONPATH;
    jupyter notebook

Now to open up a jupyter notebook ready to run TVB, just type into your terminal:
    
    ./launch_tvb.command


# Miscellaneous Tools
#### 1. Text Editor
I generally use sublime text editor. It has nice colors and a lot of cool packages to get you running stuff quickly.

https://ashleynolan.co.uk/blog/launching-sublime-from-the-terminal

#### 2. 

# Implementation
