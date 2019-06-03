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
    - Most General Linear Gaussian Model
    - General Expectation Maximization
    - Kalman Filter/Smoothing
- Important Models And Connections With Control Theory
    - Static Models \(i.e. time is not a factor\)
        - Continuous State
        - Discrete State
    - Dynamical Models \(i.e. time is a factor\)
        - Continuous State - Kalman Filter Models
        - Discrete State - Hidden Markov Models
    - Non-Gaussian Models \(i.e. noise terms are no longer normally distributed\)
    - Control Theory Type Problems
- Conclusions
- References:

<!-- /MarkdownTOC -->

# Background

Recently, I re-read this 1999 paper on Linear Gaussian models and I am pretty amazed at how deep this paper is in unifying the different common data analysis methods and linear models under one framework. We think of principal component analysis (PCA), or Gaussian mixture models (GMM), or Kalman filter models (KF) all as disparate ways to model data, but this review is able to bring them under the umbrella of the Expectation Maximization (EM). I wanted to highlight for myself (and anyone reading) the key high level concepts and insights and also extend these to talk about control systems.

At a very simplifying level, linear gaussian models are heavily used in all branches of engineering from control systems, to data analysis. Expectation maximization is an iterative learning algorithm for learning some optimal parameters in a probabilistic model.

# Methods
## Most General Linear Gaussian Model
Here is the most general form of the linear latent state-space model.

$$\dot{x}(t) = Ax(t) + Bu(t) + w$$
$$y(t) = Cx(t) + Du(t) + v$$

where: $w \approx N(0,Q)$ and $v \approx N(0,R)$ are the state and output noise terms that we assume to be normally distributed (i.e. Gaussian).

The dimensionality of the terms are:
* $x, w \in R^{n}$
* $y, v \in R^{p}$
* $u \in R^{k}$

Some jargon for folks:
* x is the state variable, generally considered "hidden", or part of the "latent space" (i.e. some subspace of your data that you don't know)
* y is the observation variable, generally considered measured, or observed (i.e. signals in your data)
* u is our control signal, that we input
* A is our state transition matrix governing how states change 
* B is our control matrix
* C is our observation matrix
* D is our feedthrough matrix
* w and v are our random variable noise terms that we may (sometimes) assume Normally distributed

Then the A, B, C, D matrices have their respecting dimensionality. In general, we assume y is observed and measured.

## General Expectation Maximization
The general expectation maximization boils down to two distinct steps: 1) Computing the expecation under a certain generative model (i.e. computing the expected states and covariances) and 2) Maximizing the likelihood given the states (i.e. computing the optimal parameters). In the general Gaussian model, these parameters are $\theta = \{A, C, B, D, Q, R\}$. 

## Kalman Filter/Smoothing
The general Kalman filter assumes Gaussian noise, which we have here. Filtering is the problem of predicting the state $x(t)$ given all the observations up to time t. Smoothing is the problem of predicting the state $x(t)$ given all the observations we have (i.e. over entire window of observation of length T).

# Important Models And Connections With Control Theory
## Static Models (i.e. time is not a factor)
Here, we are dealing with just data points (i.e. sets of x's, y's), so there is no notion of time dependency. This simplifies the general model, so that A = 0. 

General inference on model:

$$P(x | y) = \frac{P(y|x)P(x)}{P(y)} = \frac{N(Cx, R) N(0, I)}{N(0, CC^T + R)}$$
$$P(x|y) = N(\beta y, I - \beta C), \ \beta=C^T(CC^T + R)^{-1}$$

### Continuous State
Here, we presume that the state space is continuous (i.e. x is a continuous variable).

1. (Sensible) Principal Component Analysis (PCA)
PCA is probably one of the most common dimensionality reduction techniques, which at the end of the day (for you lin alg folks) boils down to Singular Value Decomposition (SVD). Here we assume the following:
* the observation noise R is a multiple of the identity matrix (i.e. $R=\alpha I$)

Note that because R is not 0, then we have some noise in the state variables, so this is very similar to probabilistic PCA. 

When $\alpha$ goes to 0, then the noise on the states goes to 0, while Q is still finite. This means that the only noise we assume in our model comes from our observations of the data. A naive approach would simply take the observed covariance matrix of our data, apply SVD to obtain the singular vector matrices and the singular values. The columns of C then are the principle components of PCA. The values of our latent space vector x are the principle values (i.e. singular values of our covariance matrix).

2. Maximum Likelihood Factor Analysis
In factor analysis, we assume the following:
* that the observation covariance matrix, R, is diagonal
* state noise Q is the identity matrix 

X are considered the factors, and the key assumption assuming R is diagonal means that the model wants to put all the covariance structure in our observed data (i.e. y variables) into the unique coordinates of R. Note that if R is diagonal, then the off-diagonals (i.e. the covariances) are equal to 0. 

3. Summary
In both static modeling procedures, where we assume our latent space and observations are static, we can solve them using EM by using the general inference equations described above for the static model. P(x|y) gives you the inference estimates of states (i.e. x) for a given set of parameters (in this case: C and R). Then for a given set of states (i.e. x), we can maximize wrt the log-likelihood of our model to recover new estimates of C and R. This is the EM algorithm! 

Quite fascinating that they wrapped this under one umbrella when most people normally look at solving for example PCA using SVD.

### Discrete State
Here, we presume x is a discrete variable.
1. Gaussian Mixture Models
If x is a discrete probability distribution controlled by the distribution of the noise, w. The mean $\mu$ and covariance Q parametrize the distribution of x. Now x is modeled by:

$$x = WTA(w)$$

where WTA is the winner take all function applied to the vector w, so x becomes a unit vector of size n. Now the interpretation of x is the mixture weights (i.e. how much each data point y belongs to each cluster). The columns of matrix C represent the cluster means. This is solved via EM also.

2. Vector Quantization (K-means) Models
When the observation noise approaches 0 (i.e. R approaches 0), then we arrive at the k-means algorithm formulation, which can be solved via EM also. So now, P(x|y) is a single point, since there is no noise in the y term, and it is all governed by the noise in the k clusters defined in the state term. 

## Dynamical Models (i.e. time is a factor)
Here, we now deal with the fact that time is a factor in our model. So A is no longer the 0 matrix. 

### Continuous State - Kalman Filter Models
The model is generated according to the general model with the noise terms all being independently and identically distributed. This is just solved via the Kalman filter and smoothing algorithms.

If all parameters are known, can employ a Maximum Likelihood approach to estimate the states.

If the parameters are unknown, then EM can be used to iterate on the parameters.

### Discrete State - Hidden Markov Models
Now, we consider when the states are discrete, which lead to Hidden Markov Models. The model for the states is:

$$x(t+1) = WTA(Ax(t)+w)$$

Here, if we constrain Q to be the identity matrix, then it will have the same covariances for all Gaussians. With traditional Hidden Markov models, we usually define a state transition matrix (e.g. normalized columns), which defines how probable different state transitions are from an initial state. Solving for the most likely state sequence employs the famous Viterbi algorithm. Solving the filtering and smoothing problems, then employ EM traditionally.

## Non-Gaussian Models (i.e. noise terms are no longer normally distributed)
This results in a famous class of algorithm known as Independent Component Analaysis. This is a generalization of the PCA. Here, we have a nonlinearity applied to the state model:

$$x = g(w)$$

This converts a Gaussian prior (i.e. noise variable w) into a non-Gaussian prior for the state variable x. Now, x is considered our "blind sources" and y is our observed data. In classical ICA, R is assumed to be infinitesimal, and C is square and full-rank. C is considered a "mixing matrix", that is how to mix the sources to "recover" our observed data.

## Control Theory Type Problems
In control theory and linear systems, we are generally interested in the following problems:

* Given the general model and outputs measured y, how do we estimate a control input u(t) that controls the dynamics of the state? That is, how do we control the eigenvalues of the system? 
    * This results in things like state-feedback and the notion of controllability.
* Given the general model, how can we estimate the values of the states if we know the rest of the parameters (A, B, C, D)?
    * This results in observers and the notion of observability.
* Given the general model, how can we estimate an optimal u(t) that follows some constraints and minimizes some cost functional on u? (e.g. constraint on the magnitude of u, or the sparseness of u, etc.)
    * This is known as optimal control. It can be deterministic, or stochastic. 

Note that the Kalman filter/smoothing procedure is an optimal observer under Gaussian noise assumptions. The EM algorithm can be used in general in conjunction with Kalman filter/smoothing to estimate the parameters (A, B, C, D).

# Conclusions
In this post, I attempt to summarize some of the main points in the Roweis paper that I thought were relevant to someone with knowledge in Linear Algebra, Probability & Statistics and Linear Dynamical Systems. The nice thing is that all these very common algorithms and methods can be framed using Expectation Maximization. This point of view links together control theory, linear dynamical systems and machine learning. It points to how general linear Gaussian models are and how general Expectation Maximization is. 

# References:
1. Roweis S. et al. "A Unifying Review of Linear Gaussian Models".http://mlg.eng.cam.ac.uk/zoubin/papers/lds.pdf
