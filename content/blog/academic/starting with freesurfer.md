Title: Using FreeSurfer
Date: 2017-12-7
Category: Academic
Tags: data analysis, eeg, phd, brain rendering
Slug: using-freesurfer
Authors: Adam Li
Summary: To guide the user in how to setup freesurfer correctly.

<!-- MarkdownTOC autolink="true" -->

- [Necessary Tools](#necessary-tools)
- [Data Processing Pipeline:](#data-processing-pipeline)
    - [1. DWI Processing](#1-dwi-processing)
    - [2. T1 MRI Processing](#2-t1-mri-processing)
    - [3. \(Optional\) CT Processing](#3-optional-ct-processing)
    - [4. Connectome Generation](#4-connectome-generation)
- [Background](#background)
    - [Common Definitions:](#common-definitions)
- [Implementation](#implementation)
    - [1. Set Up](#1-set-up)
    - [2. Running Through T1-Weighted MRI Images](#2-running-through-t1-weighted-mri-images)
    - [3. Running Through CT Images](#3-running-through-ct-images)
    - [4. Getting Surface Parcellations](#4-getting-surface-parcellations)
    - [5. Getting SEEG XYZ Coordinates](#5-getting-seeg-xyz-coordinates)
- [References:](#references)

<!-- /MarkdownTOC -->

# Necessary Tools
Freesurfer, FSL, and MRtrix3 are the three main neuroimaging and registration softwares that you need to run a systematic data pipeline of neuroimaging data (i.e. CT, MRI, DWI).

1. Freesurfer
https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall

FreeSurfer is a software package for the analysis and visualization of structural and functional neuroimaging data from cross-sectional or longitudinal studies. 

2. FSL
https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation

FSL is a comprehensive library of analysis tools for FMRI, MRI and DTI brain imaging data.

3. MRtrix3
http://mrtrix.readthedocs.io/en/latest/installation/mac_install.html

MRtrix3 is primarily intended to be used for the analysis of diffusion MRI data. In addition, at its fundamental level it is designed as a general-purpose library for the analysis of any type of MRI data. 

# Data Processing Pipeline:
## 1. DWI Processing
- Process diffusion imaging data, by denoising the data, then preprocessing it, then applying bias correction and then estimating the response function.
    
$$
    dwidenoise </DTI_dicom_dir/> <dti_img_denoise.mif>
    
    dwipreproc -rpe_none AP DTI_30_average-2_denoise.mif <dti_img_preproc_output.mif>
    
    dwibiascorrect <dti_img_preproc_output.mif> <dti_img_preproc_biascorrect_output.mif> –fsl

    dwi2response tournier <dti_img_preproc_biascorrect_output.mif> <dti_img_preproc_biascorrect_response.txt>

    dwi2fod csd DTI_30_average-2_denoise_preproc_biascorrected.mif DTI_30_average-2_denoise_preproc_biascorrected_response.txt DTI_30_average-2_denoise_preproc_biascorrected_fod.mif
$$

## 2. T1 MRI Processing


## 3. (Optional) CT Processing


## 4. Connectome Generation


# Background
Freesurfer is a tool built for rendering 3D brains using MRI and Ct scans.

FSL is a tool for coregistration and image analysis.

Download both online:

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

flirt -in patient_ct.nii -ref patient_mri.nii -omat patient_omat.mat -out patient_registered.nii.gz

This command will coregister the CT data onto the domain of the MRI data and provide a coregistration for you to look at where certain contacts of electrodes are. You can also view in Freeview the different cuts of the brain using either CT, or MRI. 

## 4. Getting Surface Parcellations 
TBD

## 5. Getting SEEG XYZ Coordinates
Once you have CT images coregistered with MRI images, you can easily extract the locations of all iEEG contacts in the MRI axis system. This is done by noting a contact within each electrode (e.g. A1, B1, C10, etc.) and then an algorithm can fill in the entire electrode's xyz coordinates and output to a file.

# References:
1. https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall#Setup.26Configuration
2. 
