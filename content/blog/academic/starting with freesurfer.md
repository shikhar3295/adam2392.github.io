Title: Using FreeSurfer
Date: 2017-12-7
Category: Academic
Tags: data analysis, eeg, phd, brain rendering
Slug: using-freesurfer
Authors: Adam Li
Summary: To guide the user in how to setup freesurfer correctly.

# Questions

# Background
Freesurfer is a tool built for rendering 3D brains using MRI and Ct scans.

## Common Definitions:
1. Registration: to find a common coordinate system for the input data sets
2. 
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

## 2. Running Through T1-Weighted MRI Images
First you want to set your current Subjects directory to where you are working with the raw say .dcm data.

    export SUBJECTS_DIR=$PWD

There may be an issue where you can't run the functions with your .dcm files. I have no idea why this occurs, but an easy fix is to externally run a dicom to nii converter and pass this type of file instead. Here is a link to a matlab converter that can do this:
https://www.mathworks.com/matlabcentral/fileexchange/42997-dicom-to-nifti-converter--nifti-tool-and-viewer

There are also other resources online.

Afterwards, you can run the following command(s):

    recon-all -i <data>.nii -s <subject_name> -autorecon1
    recon-all -i <data>.nii -s <subject_name> -all

This will take a long time! So be prepared to run this on a compute engine that has time.

## 3. Running Through CT Images
flirt <ct_data> <mri_data>.mgz

This command will coregister the CT data onto the domain of the MRI data and provide a coregistration for you to look at where certain contacts of electrodes are. You can also view in Freeview the different cuts of the brain using either CT, or MRI. 

## 4. Getting Surface Parcellations 


## 5. Getting SEEG XYZ Coordinates
Once you have CT images coregistered with MRI images, you can easily extract the locations of all iEEG contacts in the MRI axis system. This is done by noting a contact within each electrode (e.g. A1, B1, C10, etc.) and then an algorithm can fill in the entire electrode's xyz coordinates and output to a file.

# References:
1. https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#Setup.26Configuration
2. 
