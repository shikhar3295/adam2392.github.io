Title: Doctoral Board Oral Exam - PhD
Date: 2017-8-05
Category: Academic
Tags: academic, dbo, phd
Authors: Adam Li
Summary: A post about my experience through the Doctoral Board Oral exam in my PhD at Johns Hopkins University.

# Doctoral Board Oral Exam
<!-- MarkdownTOC -->

- 1. Cable Theory and Compartmental Modeling
	- Examples of different types of neurons
	- Approach
	- Important Equations
	- Study
- 2. Generalized Linear Models:
	- General Form of Exponential Family Distribution
	- Normal Linear Regression
	- Logistic Regression
	- Poisson Regression
	- Solving GLM Methods:
	- Goodness of Fit
- 3. Kalman Filter
	- Stochastic State-Space Model
	- Assumptions
	- Derivation
	- Relation to a Least-Squares Problem
	- Relation to a Bayesian Maximum Aposteri Estimation
- 4. Expectation Maximization
	- Basic Idea
- 5. K-Means Algorithm
	- Cost Function
	- The Algorithm
	- Initialization
	- Convergence
- 6. Sensory Pathways and Systems in Neuroscience
- 7. Motor Pathways and Systems in Neuroscience
- 8. General Systems in Neuroscience
- 9. Gaussian Mixture Models
- FAQ

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

## Relation to a Bayesian Maximum Aposteri Estimation



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


## Convergence
Show that the cost monotonically decreases, so the algorithm will converge at least in the sense of cost decreasing to a non-changing amount.


# 6. Sensory Pathways and Systems in Neuroscience

# 7. Motor Pathways and Systems in Neuroscience

# 8. General Systems in Neuroscience

# 9. Gaussian Mixture Models


# FAQ
1. Q: Where should I stay? 
A: 

2. Q: I only have a day in Seoul, where should I go?
A: 

