Title: Simulating Epileptic iEEG Activity Using The Virtual Brain
Date: 2017-9-27
Category: Academic
Tags: data analysis, eeg, phd, computational modeling
Slug: simulating-tvb
Authors: Adam Li
Summary: To guide the simulation of Epileptic iEEG activity using TVB in Marseille, France.

# Questions
Using convolutional and recurrent neural networks, this paper showed that they could perform seizure detection as well as incidence detection (of some experimental marker). I am interested in the possibility of exploring how this algorithm might perform on simulated TVB data, which to my knowledge has not been done yet. I would be interested in seeing how this improves, or is similar to training on the real data.

Then I was going to see if I could extend this same network onto the fragility maps.

I was wondering:
1. Would it be possible to get access to patient's SEEG data that has the SEEG xyz coordinates, and raw iEEG data? (n as big as can be)
2. A problem with the previous paper was the unbalance of data in training (e.g. much less seizure starts, then non seizure instances). For TVB, is it possible to virtually ensure seizures happen at a certain rate if I simulated for say... 2 minutes, 100 times? So that we could have many instances of seizure occurence and could train on an equal set of seizure occurence and non seizure?
3. Can TVB determine when the seizure occurred exactly in Epileptor time series?

# Background
TVB is a platform for simulating whole-brain dynamics that starts from raw data involving:
    1. structural connectivity derived from DTI
    2. brain parcellation derived from MRI and CT
    3. SEEG xyz locations derived from MRI and CT
This will then determine a gain matrix to determine SEEG signals from the source signals that are generated from neural mass models.

The neural mass models will be implemented with nonlinear, complex models for simulating certain type of electrophysiology. The Epileptor is used for simulating seizure activity from a specific source region. 

The epileptor is a set of coupled differential equations that rely on 6 different variables. They are described here:

# Data & Metadata

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

## 2. Simulating Epilepsy
In order to simulate epilepsy, you are going to walk through a pipeline using TVB. 

i. Structural Connectivity

ii. Neural Mass Model

iii. Integrators

iv. Monitors

Then once these are complete, you can run your simulation.

