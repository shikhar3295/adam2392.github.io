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
- Concepts
    - 1. The Virtual Brain \(TVB\) vs Network Data Analysis
    - 2. Using TVB To Augment Neural Datasets For Deep Learning
- Conclusions / Future Considerations
- Random Notes
    - Data Pipeline Design
    - PhD and Research Understanding
        - References:

<!-- /MarkdownTOC -->
# Background
## 1. Epilepsy
Epilepsy is a disease that affects more then 70 M people worldwide, which characterizes itself with seizures (i.e. abnormal brain activity) for seconds to several minutes. Epilepsy can be treated with medicine that generally inhibits brain activity (albeit with numerous side effects), and also with surgery. Surgery can involve resection (i.e. cutting a portion of the hypothesized diseased brain) and laser ablation (i.e. heat treatment of small spherical regions within the brain). When successful, surgery can result in complete seizure freedom! 

However, the problem is that surgery is extremely variable in success (e.g. ~50% average). Imagine getting permanent brain surgery, when there is a high likelihood of you still having seizures afterwards. A main obstacle to high success rates is incorrect localization of the epileptogenic zone, the clinical region of the brain that seizures originate from. In addition, clinicians employ a strategy similar to cancer resection; they will cut out a greater portion of the brain then possibly hypothesized because it will have good "margins" on the diseased tissue. This can cause unnecessary neural dysfunction, especially when these regions are close to important areas for language, motor or executive function. The goal of any researcher in this field is to identify biomarkers and methods for robustly identifying this diseased brain region given neural data. The result would be more successful surgeries and more accurate maps, leading to less brain regions being resected. Neural data can come in the form of electrophysiological recordings, MRI images, Diffusion weighted MRI images and CT images.

## 2. Computational Modeling
Computational modeling is the art of using mathematical equations to model how certain systems (i.e. the brain) behaves given parameters you input. These are normally formed in the framework of differential equations (i.e. that class we took in undergrad that made us go "huh?"). So here, at Marseille, the group has developed computational models that take in the patient's specific brain imaging to model epilepsy in a patient-specific manner (i.e. personalized brain modeling). The way it does this is by parcellating the brain into multiple regions, where each region is modeled by a computational model that can exhibit certain seizure phenomena. Then, by coupling (connecting) every region based on realistic brain connectivity, you can simulate brain behavior when you "set" different regions of the brain to be "diseased" that has some form of a realistic brain network. One could then compare the simulation and the real electrophysiological recording data in patients to test different hypotheses, such as: 

1. what happens if we set this region to be epileptogenic? does it resemble the real dynamics recorded in the patient's brain? 
2. If we remove this region of the brain (i.e. remove connectivity to and from this region), will it help prevent propagation of seizure activity to healthy regions of the brain?
3. Can we generate realistic data that can reflect feature variability of the real recording data?

## 3. Algorithms
Algorithms are spelling out a certain set of computations that a program should undertake to get a specific answer. In our research group, we are attempting to develop algorithms that take in brain data of the patient and outputs a prediction of the diseased region. There are different kinds of algorithms that use the data in various ways. In general, all data analysis tries to represent data in various ways. Does the amplitude, or frequency of the data matter? Should we represent the data as a graph? Should we apply filters to the data to remove noise? Should we just leave the data alone and let the model decide what is important?

Our research group currently developed a fast network-based algorithm that analyzes the data as a graph by applying a very specific type of computation. Namely, it constructs a graph out of the dataset and applies perturbations to the graph (i.e. add's vectors of noise in a very structured way), to determine which regions of the brain are most susceptible to being perturbed into seizing. This specific type of analysis requires some simple linear systems theory to derive an analytical equation for doing this. It was biologically inspired and can be read in some of the reference publications.

On the other end of the spectrum, one could apply deep learning to this problem for a way of supervised learning. What this would require is knowing the exact regions of the brain that are diseased and then feeding in the data and the labels of the regions to let the model determine which features of the data are most predictive of the diseased region. This is more general, but can require large amounts of data and hyperparameter tuning of the neural networks. In addition, epilepsy data has the problem of "noisy labeling". Clinicians are never sure where exactly the EZ is, so even if we have a significant amount of patients, our training data for deep learning are not optimal. Contrast this with the infamous case of recognizing "cats vs dogs", where I am pretty positive most cats are definitely correctly labeled as cats, and vice versa.

# Concepts
## 1. The Virtual Brain (TVB) vs Network Data Analysis
This was the main project proposed when I applied for the Whitaker/Chateaubriand fellowships. The goal was to use the flexible modeling capabilities of "The Virtual Brain" (TVB) platform developed here in Marseille to understand how network data predictions of the epileptogenic zone performs under various model configurations. So, how can our predictions work under various clinical settings? Can we arrive at the same conclusion when our algorithm is applied to an in-silico model?

Being able to demonstrate agreement by using this whole-brain model helps provide evidence on two fronts: 

1. provides additional evidence that TVB is capable of modeling the dynamical characteristics of seizures realistically and 
2. provide hypothetical constraints on data analysis by providing ground-truth simulations of epileptic seizures and demonstrating when the algorithms work.

**Summary of Work**
By using a patient's individual neuroimaging scans, and their actual recorded epileptic seizures, we can 1) create a personalized brain from those scans and 2) analyze their electrophysiological recordings with our network-based algorithm. 

From the personalized brain, we can use TVB as a software platform to simulate signals that we hypothesize might come from different regions of that patient's brain. If we fix all parameters, and then systematically change which region of the brain is epileptic, then we can form a suite of datasets that we know the region that is epileptic. This would not be possible with real data because we never know for sure which region of the brain is epileptic! So assuming this model is accurate to some degree in replicating features of the  brain's electrophysiology, we can compare the results of the network-based analysis for each simulated dataset.

With tools from statistics, we can statistically compare the different results from our algorithm to the real data. The results that are closest to our real data suggest that this is the region most likely to be actually epileptic. This region was where we set as epileptic in the software and was capable of producing the simulated data that best represented the real data; in other words, it is a measure of how similar our simulations are to real data under different hypotheses of epileptic regions. This presents a framework to systematically produce an estimate of the real epileptic region in a patient, and also to study situations in which our network-based algorithm can fail. It is a "step" towards opening the black box, which is the patient's brain.

## 2. Using TVB To Augment Neural Datasets For Deep Learning
A core problem of deep learning is the amount of data required to train successful models to perform classification/regression. Generally, more data means more variation in your dataset, thus having a higher likelihood of capturing the true underlying distribution of all possible data. This is especially apparent in models surrounding neuroscience and neural data. That is because neural data is traditionally difficult to obtain, and is extremely constrained because of the different variables that go into collecting the data in a clinical setting. Clinical procedures can vary, recording electrodes can be implanted in various places of the brain, brains vary structurally from patient to patient, brains vary functionally from patient to patient, and different regions of the brain are epileptic from patient to patient.

TVB at its core is a model of the brain that utilizes realistic brain geometry, connectivity and clinical hypotheses to simulate electrophysiological signals. Based on the model, it can generate different patterns of behavior, or in our case, epileptic seizures. This is extremely important because as a scientist, you can control the variables to produce different types of data, but all demonstrating epileptic seizing. This hypothetically would give you a huge amount of variable data, that has ground truth set by you, and also only require computing power to simulate. It is not constrained by medical procedures and could help in generating data that deep learning models can learn from for each patient BEFORE surgery. This could help establish a completely computerized pipeline for helping clinicians make informed decisions and hypotheses before the patient is operated on with the help of deep learning.

**Summary of Work**
Using a batch of real recording data from patients, we can construct a deep learning model that learns some useful classification from the data. For example, which region is "epileptic", or when is the patient seizing? However, in order to be fair, your training of the model will always use a leave-one-patient out scheme because you have to assume you do not have access to a patient's data before making predictions on that specific patient. This brings up a lot of problems though! Even if we have "a lot" of data, there are so many clinical variables (brought up earlier) that can cause variations in how the test patient's data will look compared to your training data.

So my proposal is to use TVB as a way of constructing the personalized brain model for a patient, and then simulating a highly variable dataset by varying parameters. Although it is highly possible that parts of this dataset is not fully realistic or representative of real data, it gives a way of generating significant amounts of data and a way of generating data points that are closer representations in terms of the patient's specific brain structure, connections, and electrode implantation schema. 

I test the potential for this by performing a set of experiments using a standard neural network trained only on the real data, vs trained on the real data AND the simulated dataset from the test patient's specific brain model. Initial results show improved convergence of training, but more work needs to be done.

# Conclusions / Future Considerations
Returning to JHU, I have a lot of things to accomplish before being able to graduate with my PhD. Although spending this year may have increased my timeline to graduation, it also expanded my research scope and scientific knowledge. This is exciting to me because a PhD is not just about quickly graduating, but about developing a broad range of deep skills that allow you to make impacts on a variety of different problems.

# Random Notes
This year, I really had to deal with more data then I was accustomed to at JHU. At JHU, I had access to various text files, EEG recordings and MRI/CT imaging data for various patients from various clinical centers. However, these recordings were never longer then 5-10 minutes. 

Here, I had to begin dealing with data at larger scales. I had to understand how to optimize parallelized runs of linear algorithms on said data. My datasets went from a couple hundred MB (i.e. few recordings for a single patient), to a few GB (i.e. multiple patients) to a couple hundred GB and few TBs (i.e. >50 patients with multiple recordings). My analysis and data pipeline design scaled at the same time, but required me to refactor and understand how to continuously analyze the data robustly and efficiently. I complain a lot about having to refactor code (since it's not really research), but I think there is a lot to be learned by having to independently design, implement and test your own data pipelines as your data/analysis becomes more and more complex.

I started out with analyzing datasets on my laptop/workstation with unoptimized code. Then I proceeded to optimize different parts of my workflow and moduralize it, so that it could be parallelized onto multiple cores. I then proceeded to submit it onto the JHU Maryland High-Performance Computing cluster. At the same time, I ended up learning a lot more about Unix and terminal-based commands.

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

Even if your results don't pan out, this helps build a mindset of systematic thinking. You want to plan mini-experiments on your analysis that will provide you with the next step to pursue. The analysis did not work the way you expect? Okay, then we probably need to test these factors and visualize data over the next week. Okay if those factors will take too long, we should back up and clean up our approach.

### References:
1. http://www.thevirtualbrain.org/tvb/
2. https://ieeexplore.ieee.org/document/7963378/
3. https://www.ncbi.nlm.nih.gov/pubmed/29060480

