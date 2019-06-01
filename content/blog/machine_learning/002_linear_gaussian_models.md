Title: Linear Gaussian Models
Date: 2019-06-18
Category: Machine Learning
Tags: phd, machine learning
Slug: gaussian-generative-models
Authors: Adam Li
Summary: An overview of linear gaussian models and how in general, they fall under the learning procedure (system idenfitication) of Expectation-Maximization.

<!-- MarkdownTOC -->

- Background
- Methods
- Conclusions
- References:

<!-- /MarkdownTOC -->

# Background

Recently, I re-read this 1999 paper on Linear Gaussian models and I am pretty amazed at how deep this paper is in unifying the different common data analysis methods and linear models under one framework. We think of principal component analysis (PCA), or Gaussian mixture models (GMM), or Kalman filter models (KF) all as disparate ways to model data, but this review is able to bring them under the umbrella of the Expectation Maximization (EM). 




# Methods

.. math::

  \alpha = 10^2

$$\dot{x}(t) = Ax(t) + w$$
$$y(t) = Cx(t) + v$$

where: $w \approx N(0,Q)$ and $v \approx N(0,R)$ are the state and output noise terms that we assume to be normally distributed (i.e. Gaussian).

# Conclusions

# References:
1. Roweis S. et al. "A Unifying Review of Linear Gaussian Models".http://mlg.eng.cam.ac.uk/zoubin/papers/lds.pdf
