Title: Using The Virtual Brain to Understand Algorithms
Date: 2018-06-01
Category: Academic
Tags: tvb, phd
Slug: whitaker-summary-experience
Authors: Adam Li
Summary: To summarize my Whitaker/Chateaubriand research experience abroad in Marseille, France.

<!-- MarkdownTOC -->

- Background
    - 1. Epilepsy
    - 2. Computational Modeling
    - 3. Algorithms
- Random Notes
    - Data Pipeline Design
    - PhD and Research Understanding
- Concepts
    - 1. TVB vs Network Data Analysis
    - 2. Using TVB To Augment Neural Datasets For Deep Learning
- Conclusions / Future Considerations
        - References:

<!-- /MarkdownTOC -->
# Background
## 1. Epilepsy
Epilepsy is a disease that affects more then 70 M people worldwide, which characterizes itself with seizures (i.e. abnormal brain activity) for seconds to several minutes. Epilepsy can be treated with medicine that generally inhibits brain activity (albeit with numerous side effects), and also with surgery. Surgery can involve resection (i.e. cutting a portion of the hypothesized diseased brain) and laser ablation (i.e. heat treatment of small spherical regions within the brain). When successful, surgery can result in complete seizure freedom!

However, the problem is that surgery is extremely variable in success (e.g. ~50% average), even though mortality rates have drastically lowered. A main obstacle to high success rates is incorrect localization of the epileptogenic zone, the clinical region of the brain that seizures originate from. The goal of any researcher in this field is to identify biomarkers and methods for robustly identifying this diseased brain region given neural data. Neural data can come in the form of electrophysiological recordings, MRI images, Diffusion weighted MRI images and CT images.

## 2. Computational Modeling
Computational modeling is the art of using mathematical equations to model how certain systems (i.e. the brain) behaves given parameters you input. So here, at Marseille, the group has developed computational models that take in the patient's specific reconstructed brain tractography and geometry to model epilepsy. The way it does this is by parcellating the brain into multiple regions, where each region is modeled by a computational model that can exhibit seizure phenomena. By coupling every region based on realistic brain connectivity, you can simulate brain behavior when you "set" different regions of the brain to be "diseased". One could then compare the simulation and the real electrophysiological recording data in patients to test different hypotheses, such as: 
1. what happens if we set this region to be epileptogenic? does it resemble the real dynamics recorded in the patient's brain? 
2. If we remove this region of the brain (i.e. remove connectivity to and from this region), will it help prevent propagation of seizure activity to healthy regions of the brain?
3. Can we generate realistic data that can reflect feature variability of the real recording data?

## 3. Algorithms
Algorithms are spelling out a certain set of computations that a program should undertake to get a specific answer. In our research group, we are attempting to develop algorithms that take in brain data of the patient and outputs a prediction of the diseased region. There are different kinds of algorithms that use the data in various ways. In general, all data analysis tries to represent data in various ways. Does the amplitude, or frequency of the data matter? Should we represent the data as a graph? Should we apply filters to the data to remove noise? Should we just leave the data alone and let the model decide what is important?

Our research group currently developed a linear algorithm that analyzes the data as a graph by applying a very specific type of computation. Namely, it constructs a graph out of the dataset and applies perturbations to the graph (i.e. add's vectors of noise in a very structured way), to determine which regions of the brain are most susceptible to being perturbed into seizuring. This specific type of analysis requires some simple linear systems theory to derive an analytical equation for doing this.

On the other end of the spectrum, one could apply deep learning to this problem for a way of supervised learning. What this would require is knowing the exact regions of the brain that are diseased and then feeding in the data and the labels of the regions to let the model determine which features of the data are most predictive of the diseased region. This is more general, but can require large amounts of data and hyperparameter tuning of the neural networks.

# Random Notes
This year, I really had to deal with more data then I was accustomed to at JHU. At JHU, I had access to various text files, EEG recordings and MRI/CT imaging data for various patients from various clinical centers. However, these recordings were never longer then 5-10 minutes. 

Here, I had to deal with data at scale. I had to understand how to optimize parallelized runs of linear algorithms on said data. My datasets went from a couple hundred MB (i.e. few recordings for a single patient), to a few GB (i.e. multiple patients) to a couple hundred GB and few TBs (i.e. >50 patients with multiple recordings). My analysis and data pipeline design scaled at the same time, but required me to refactor and understand how to continuously analyze the data robustly and efficiently.

I started out with analyzing datasets on my laptop/workstation with unoptimized code. Then I proceeded to optimize different parts of my workflow and moduralize it, so that it could be parallelized onto multiple cores. I then proceeded to submit it onto the JHU High-Performance Computing cluster. 

## Data Pipeline Design
1. First, I began with one CPU per window of data (each dataset was split into a number of windows to analyze). This resulted in hundreds-thousands of CPUs being fired up with loading the data and then analyzing a short segment of the dataset. This had numerous problems. One CPU out of hundreds/thousands could easily fail the run the job correctly, which would result in a missing computed window.
2. Then, I began using a parallel framework with GNU that ran each dataset with a fixed 24 cores per node. This helped because GNU allows you to restart jobs using a log file, but this was also problematic because as datasets grew longer, it wasn't clear how long I would have to wait to get data per each patient.
3. Now, I also break up datasets into chunks and then analyze using 24-48 cores at a time that sift through the data. These data analyzed-chunks can later be combined to form into the one dataset if necessary, but a metadata json object is used to store information allowing anyone using the data to understand how to put computations together.

## PhD and Research Understanding
A lot of this year was spent reading papers and doing a lot of thinking... Not very productive, but I really felt like I learned a lot and expanded my research mindset.

Couple things I started learning more about:
1. reading papers is good to do on a consistent basis, but focus on getting to the core of the "key" papers (how you decide which papers are key comes with exp)

I realized that some papers are great to learn and skim through the results and methods to understand how they did it, what are the limitations and what was innovated on. Then there are other papers that introduce a completely new concept that might be different. These papers are important to understand because they usually spur papers down the road that require you to understand this one. I tend to go through the figures and equations multiple times to understand the details of the motivation, methods and results.
2. software engineering is very important in data analysis.

It helps you formulate and design a software package that is intended to "experiment" the different parameters, datasets, and visualize results in an end-to-end fashion. I probably refactored my code around 5-6 times this year, which was a great learning experience, but it took a lot of time. It helped me understand the scope of my projects and will hopefully be helpful down the road.

3. it's easy to get stuck in a loop of feeling like "you're not going anywhere". 

Research takes time and whether it's analyzing data, thinking of a math problem, understanding an experiment, or testing a computational model, it can become easy to think you're making no progress. It is extremely important to set mini-goals (e.g. weekly) on top of your milestone goals (e.g. monthly, or few months). You want to also allow yourself room to learn how to set these goals realistically. At the beginning, you'll think that you are capable of accomplish ABC...Z in one week. Most of the time, this ends up being overly optimistic. As you grow, you start to realize what is realistically accomplishable on a week-to-week basis. This helps you scope out each week and plan accordingly to make incremental progress.

Even if your results don't pan out, this helps build a mindset of systematic thinking. You want to plan mini-experiments on your analysis that will provide you with the next step to pursue. "The analysis did not work the way you expect? Okay, then we probalby need to test these factors and visualize data over the next week. Okay if those factors will take too long, we should back up and clean up our approach."

# Concepts
## 1. TVB vs Network Data Analysis
This was the main project proposed when I applied for the Whitaker/Chateaubriand fellowships. The goal was to use the flexible modeling capabilities of "The Virtual Brain" platform developed here in Marseille to understand how network data predictions of the epileptogenic zone performs under various model configurations. So, how can our predictions work under various clinical settings? Can we arrive at the same conclusion when our algorithm is applied to an in-silico model?

Being able to demonstrate agreement by using this whole-brain model helps provide evidence on two fronts: 1. provides additional evidence that TVB is capable of modeling the dynamical characteristics of seizures realistically and 2. provide hypothetical constraints on data analysis by providing ground-truth simulations of epileptic seizures and demonstrating when the algorithms work.

## 2. Using TVB To Augment Neural Datasets For Deep Learning
A core problem of deep learning is the amount of data required to train successful models to perform classification/regression. This is especially apparent in models surrounding neuroscience and neural data. That is because neural data is traditionally difficult to obtain, and is extremely constrained because of the different variables that go into collecting the data. For this reason, recording data from one clinical center can be significantly different from another clinical center because of protocols used and hardware settings.

TVB at its core is a generative model of the brain that utilizes realistic brain geometry, connectivity and clinical hypotheses to simulate electrophysiological signals. Based on the model placed into TVB, it can generate different patterns of behavior, or in our case, epileptic seizures. This is extremely important because as a scientist, you can control the variables to produce different types of data, but all demonstrating epileptic seizing. This hypothetically would give you a huge amount of variable data, that has ground truth set by you, and also only require computing power to simulate. It is not constrained by medical procedures and could help in generating data that deep learning models can learn from for each patient BEFORE surgery. This could help establish a completely in-silico pipeline for helping clinicians make informed decisions and hypotheses before the patient is operated on.

# Conclusions / Future Considerations
TBD: Returning to JHU...

### References:
1. http://www.thevirtualbrain.org/tvb/
2. https://ieeexplore.ieee.org/document/7963378/
3. 

