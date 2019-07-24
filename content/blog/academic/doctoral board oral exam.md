Title: Doctoral Board Oral Exam (PhD)
Date: 2017-8-5
Category: Academic
Tags: doctoral board oral, phd, johns hopkins
Slug: doctoral-board-oral
Authors: Adam Li
Summary: A short walkthrough of my experience with the DBO exam at Johns Hopkins University

# Doctoral Board Oral Exam
<!-- MarkdownTOC autolink="true" -->

- [1. Cable Theory and Compartmental Modeling](#1-cable-theory-and-compartmental-modeling)
	- [Examples of different types of neurons](#examples-of-different-types-of-neurons)
	- [Approach](#approach)
	- [Important Equations](#important-equations)
		- [Unsealed end:](#unsealed-end)
		- [Sealed end:](#sealed-end)
		- [Concatenated Cables:](#concatenated-cables)
		- [Definitions:](#definitions)
		- [Compartmental Models:](#compartmental-models)
	- [Study](#study)
- [2. Generalized Linear Models:](#2-generalized-linear-models)
	- [General Form of Exponential Family Distribution](#general-form-of-exponential-family-distribution)
	- [Normal Linear Regression](#normal-linear-regression)
	- [Logistic Regression](#logistic-regression)
	- [Poisson Regression](#poisson-regression)
	- [Solving GLM Methods:](#solving-glm-methods)
	- [Goodness of Fit](#goodness-of-fit)
- [3. Kalman Filter](#3-kalman-filter)
	- [Stochastic State-Space Model](#stochastic-state-space-model)
	- [Assumptions](#assumptions)
	- [Derivation](#derivation)
	- [Relation to a Least-Squares Problem](#relation-to-a-least-squares-problem)
	- [Relation to a Bayesian Maximum Aposteri Estimation](#relation-to-a-bayesian-maximum-aposteri-estimation)
- [4. Expectation Maximization](#4-expectation-maximization)
	- [Basic Idea](#basic-idea)
- [5. K-Means Algorithm](#5-k-means-algorithm)
	- [Cost Function](#cost-function)
	- [The Algorithm](#the-algorithm)
	- [Initialization](#initialization)
	- [Convergence](#convergence)
- [6. Sensory Pathways and Systems in Neuroscience](#6-sensory-pathways-and-systems-in-neuroscience)
- [7. Motor Pathways and Systems in Neuroscience](#7-motor-pathways-and-systems-in-neuroscience)
- [8. General Topics in Neuroscience](#8-general-topics-in-neuroscience)
- [9. Gaussian Mixture Models](#9-gaussian-mixture-models)
- [FAQ](#faq)

<!-- /MarkdownTOC -->
# 1. Cable Theory and Compartmental Modeling
## Examples of different types of neurons
There are thalamic cells, pyramidal cells, double pyramidal cells, granule cells, purkinje cells. These all have different morphologies and perform different computations.

## Approach
1. Approximate dendrites as uniform membrane cylandiers
2. Synaptic inputs are approximated as 'injected currents'
3. Use the cable equation to create a system of differential equations for each cylinder.


## Important Equations
1. input conductance of semi-infinite cable
2. input conductance of infinite cable

### Unsealed end:
1. cable equation
2. input conductance of finite cable
3. s.s. voltage along cable

### Sealed end:
1. input conductance of the finite cable
2. s.s. voltage along cable

### Concatenated Cables:
1. Compute V(X) along branches, by determining $G_{out}$

### Definitions:
Know definitions and related biology of:
- axial resistance, the resistance to current flow along the uniform cable (along the dendrite)
- membrane resistance, the resistance of current flow out of the dendrite
- membrance capacitance, the capacitance of a patch of membrane surface area
- derive cable equation as a model of concatenated RC circuits

### Compartmental Models:
Be able to derive system of equations into a matrix form for a linear time-invariant system 

Understand how transfer resistances work. Understand how distributing synaptic inputs works. 

Understand how coincidence detection (AND operator), shunting inhibition (AND-NOT operator).

## Study
1. Definitions of cable theory and biological relations
2. Solving single cable equation and different boundary conditions
3. Derivation of cable equation under different boundary conditions
4. Deriving LTI system from compartmental models of cables
5. Derive transfer resistances
6. Derive AND operator (coincidence detection)
7. Derive AND-NOT operator (shunting inhibition)

# 2. Generalized Linear Models:
## General Form of Exponential Family Distribution
Be able to define all the terms, such as: natural paramters, sufficient statistic, natural link function, dispersion parameter

## Normal Linear Regression

## Logistic Regression

## Poisson Regression


## Solving GLM Methods:
1. Penalized Quasi-likelihood
2. Laplace's Method
3. Adaptive Gaussian Quadrature

## Goodness of Fit
1. Chi-square test
2. Kolmogorov Statistic

# 3. Kalman Filter 
## Stochastic State-Space Model
Here, list the linear, time-invariant system with a state evolution equation and measurement/observation equation.

## Assumptions
1. state and observation noises are independent, zero-mean Gaussian white processes with some defined covariances
2. initial state x_0 is a Gaussian R.V. independent of the state/observation noises

## Derivation
Derive the Kalman filter equations for the state update, covarariance estimates

1. Measurement update
2. Time update
3. Combined Update
4. Covariance Update

## Relation to a Least-Squares Problem
Review...

## Relation to a Bayesian Maximum Aposteri Estimation
Review...


# 4. Expectation Maximization
## Basic Idea
By computing the likelihood of your unknown parameters, based on known outcomes. You can perform maximum likelihood estimation to get the best estimate of the unknown parameters


# 5. K-Means Algorithm
## Cost Function
The cost function is attempting to minimize the distortion (distance to centers) for every point in the set of data points, S.

## The Algorithm
'''
Input: k clusters
initialize centers: z_1, ..., z_k \in \real^d and clusters C_1, ..., C_k
repeat until there is no further change in L(z, C):
	for each j (data point): C_j <- {x \in S whose closest center is z_j}
	for each j (data point): z_j <- mean(C_j) 
'''

Walk through for a small example to see how the algorithm works:
(0, 0, 0)
(0, 0.5, 1)
(1, 3, 2)
(4, 5, 6)
(2, 3, 1)
(5, 2, 0)
(0, 1, 0)
(1, 1, 0)
(2, 1, 0)

## Initialization
Initialization of a k-means type algorithm initializes k "means", we call centers at the beginning, and then assigns points into these centers based on the cost function. 

## Convergence
Show that the cost monotonically decreases, so the algorithm will converge at least in the sense of cost decreasing to a non-changing amount.


# 6. Sensory Pathways and Systems in Neuroscience
The different neuronal pathways in the central nervous system, vs the periphery nervous system. 

Visual sensory pathway that leads from the retina all the way to the occipital lobe of the brain.

The somatosensory pathways that lead to the SI, and SII all with nerve sensors from the periphery of your body.

# 7. Motor Pathways and Systems in Neuroscience
How does motor movements get controlled in the brain?

The premotor cortex, and also the motor cortex are at the highest levels of control. We can also include the cerebellum when we talk about motor control.

# 8. General Topics in Neuroscience
Good things to know and remember are:
- Hodgkin Huxley models: a biophysical model that models realistic neuronal firing based on concentration gradients, membrane conductances, membrane potentials and even more.
- Nernst equation: a fundamental equation for determining the resting potential of a membrane in the presence of a concentration gradient of an ion.
- Goldman-Katz equation: a model with multiple ions that determins the resting potential of a membrane (extension of Nernst)
- Action potentials and the chronology of cell actions that are taken

# 9. Gaussian Mixture Models
This is the idea that some data distributions can be the combinations of many different Gaussian models with different means and variance, but superimposed on each other. 

The goal of a gaussian mixture model is to identify the parameters of each of the separate gaussians by a process called Expectation Maximization. In this process, we switch between maximizing the likelihood by iterating on the parameters of the gaussian models and computing a new likelihood function given the new parameters.

# FAQ
1. Q: How long should I study for?
A: I would study for about 2-3 weeks with nothing else going on. You want to be able to do a comprehensive overview of everything first, and then dive deeper into topics that are more likely to come up. You should also do test runs of walking through "open-ended" questions on a white board many times.

The goal here is to practice thinking out loud and being very clear in your communication.

