Title: Using FreeSurfer
Date: 2017-12-7
Category: Academic
Tags: data analysis, eeg, phd, brain rendering
Slug: using-freesurfer
Authors: Adam Li
Summary: To guide the user in how to setup freesurfer correctly.
status: draft 

# Questions


# Background
Freesurfer is a tool built for rendering 3D brains using MRI and Ct scans.

# Implementation
## 1. Set Up
First you will want to download freesurfer from the following website:

https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall
Linux:
    ## bash
    $> export FREESURFER_HOME=/usr/local/freesurfer
    $> source $FREESURFER_HOME/SetUpFreeSurfer.sh

    ## tcsh
    $> setenv FREESURFER_HOME /usr/local/freesurfer
    $> source $FREESURFER_HOME/SetUpFreeSurfer.csh
Mac:
    $> export FREESURFER_HOME=/Applications/freesurfer
    $> source $FREESURFER_HOME/SetUpFreeSurfer.sh

Run those commands within your terminal, or add them to ~/.bashrc file to have access to all the command line tools for freeview.

You will need to setup your own directory where you will hold all your subject data.

    export SUBJECTS_DIR=<path to subject data> 

This will be where you store say patient's MRI/CT scans that you will use to reconstruct the brain.

# References:
1. https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#Setup.26Configuration
2. 
