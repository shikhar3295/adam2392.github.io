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

# Data & Metadata

# Implementation