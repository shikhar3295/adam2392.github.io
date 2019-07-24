Title: Simulating Epileptic iEEG Activity Using The Virtual Brain
Date: 2017-9-27
Category: Academic
Tags: data analysis, eeg, phd, computational modeling
Slug: simulating-tvb
Authors: Adam Li
Summary: To guide the simulation of Epileptic iEEG activity using TVB in Marseille, France.

<!-- MarkdownTOC autolink="true" -->

- [Background](#background)
- [Data & Metadata](#data--metadata)
- [Implementation](#implementation)
    - [1. Setting Up Environment](#1-setting-up-environment)
    - [1b. Setting Up Environment on a Cluster](#1b-setting-up-environment-on-a-cluster)
    - [1c. Using Docker / Singularity](#1c-using-docker--singularity)
    - [2. Simulating Epilepsy](#2-simulating-epilepsy)
    - [References:](#references)

<!-- /MarkdownTOC -->

# Background
TVB is a platform for simulating whole-brain dynamics that starts from raw data involving:
    1. structural connectivity derived from DTI
    2. brain parcellation derived from MRI and CT
    3. SEEG xyz locations derived from MRI and CT
This will then determine a gain matrix to determine SEEG signals from the source signals that are generated from neural mass models.

The neural mass models will be implemented with nonlinear, complex models for simulating certain type of electrophysiology. The Epileptor is used for simulating seizure activity from a specific source region. 

The epileptor is a set of coupled differential equations that rely on 6 different variables. They are described here:

# Data & Metadata
Generally, refer to my post on "Freesurfer" to establish the preprocessing data pipeline using Freesurfer, FSL and MRtrix3.

The minimum necessary requirements for creating the TVB dataset are a set of T1 and DWI images as a list of dicom files, or a single 4-D image nifti file.

A high level summary of how the pipeline proceeds is:
1. Construct Cortical Surface, Subcortical Surface
Using freesurfer, you can get the reconstructed surfaces, which are your files that outline the voxels that belong to each region of the brain. This will give you the surface geometries of the cortical and subcortical surface.

2. Construct Parcellation Scheme
This can range from the default in freesurfer to different atlases available for the human brain. This will give you a region mapping for every vertex/face from your cortical/subcortical surface geometries files.

3. Construct Corticography Tracts
First, you need to coregister the DWI images with the T1 scans

Using the DWI images, along with the reconstructed surfaces, you can count fiber tracts between each region of the brain and reconstruct the structural connectivity matrices. This is composed from the weights matrix and the length matrix between parcellated regions.

4. Obtain Electrode Coordinates in T1 Space
First, you need to coregister the CT reconstructed freesurfer file into the T1 space. 

5. Computing Gain Matrix Between Brain Regions and Electrodes
In order to compute forward solutions of electrode (i.e. SEEG, ECoG, etc.) activity, you need to compute a gain matrix that transforms region activity into electrode activity. 

This can be done using an inverse-square method fall-off on the region activity, or using a dipole method as outlined in the "Virtual Epileptic Patient" paper.

# Implementation
## 1. Setting Up Environment
First you may want to set up a conda environment, or a virtualenv that will separate the entire python project from your normal OS.

    $
    pip install nibabel networkx
    git clone https://github.com/the-virtual-brain/tvb-data
    git clone https://github.com/the-virtual-brain/tvb-library
    $

If you want to have a script to add these all to path for your jupyter notebook, use the following:

    #!/bin/bash
    echo "Launching IPython Notebook from TVB Distribution"
    if [ -z "$LANG" ]; then
        export LANG=en_US.UTF-8
    fi
    export LC_ALL=$LANG
    # add tvb data and library to path and launch notebook
    export PYTHONPATH=$(pwd)/_tvbdata:$(pwd)/_tvblibrary:$PYTHONPATH;
    jupyter notebook

## 1b. Setting Up Environment on a Cluster

    . /soft/miniconda3/activate
    conda env list
    conda create -n tridesclous python=3.6 scipy numpy pandas scikit-learn matplotlib seaborn pyqt=5 ipykernel
    source activate tridesclous
    pip install pyqtgraph
    pip install https://github.com/tridesclous/tridesclous/archive/master.zip
    python -m ipykernel install --name tridesclous-testing —user

## 1c. Using Docker / Singularity
TBD

## 2. Simulating Epilepsy
In order to simulate epilepsy, you are going to walk through a pipeline using TVB. Details are left out for now.

i. Structural Connectivity
What is the matrix of connectivities between your brain regions?
Ex: Connectivity weights, conduction speed, coupling function between long-range regions

ii. Neural Mass Model
What is the phenomenological model at brain regions?
Ex: Epileptor6D, with parameter settings

iii. Integrators
How to solve your stochastic differential equation?
Ex: Heunstochastic, with noise levels

iv. Coupling
How are your brain regions coupled?
Ex: linear, additive, hyperbolic

v. Monitors
What variables to monitor and store?
Ex: State variables, iEEG activity from sampling rate and period.

Then once these are complete, you can run your simulation.

## References:
1. https://github.com/the-virtual-brain/tvb-library
2. https://github.com/the-virtual-brain/tvb-epilepsy
3. https://www.thevirtualbrain.org/tvb/zwei


