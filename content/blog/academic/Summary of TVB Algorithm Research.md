Title: Using The Virtual Brain to Understand Algorithms
Date: 2018-06-01
Category: Academic
Tags: tvb, phd
Slug: whitaker-summary-experience
Authors: Adam Li
Summary: To summarize my Whitaker/Chateaubriand research experience abroad in Marseille, France.
status: draft

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
- Conclusions
- Future Considerations
        - References:

<!-- /MarkdownTOC -->
# Background
## 1. Epilepsy

## 2. Computational Modeling

## 3. Algorithms


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

# Concepts
## 1. TVB vs Network Data Analysis


## 2. Using TVB To Augment Neural Datasets For Deep Learning



# Conclusions

# Future Considerations

### References:
1. 

