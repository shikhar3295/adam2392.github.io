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
- Conclusions for Gaussian Linear Models
        - Dynamic Version of PCA/KMeans?
- Extensions of Gaussian Linear Models
    - Low Rank Tensors \(to generalize space, time and other variable dimensions!\)
    - Deep Kalman Filter
        - Caveats of the DKF
    - Deep Extend To Control \(EC2\)
    - Deep Variational Bayes Filter
    - Deep Koopman Model
        - Quick Koopman Theory Overview
        - Now the Deep Koopman Model
    - Deep Kalman Variational Autoencoders \(DKVAE\)
    - Possibilities for Improved Deep State Space Models \(DSSM\)
- References:

<!-- /MarkdownTOC -->

# Background

Recently, I re-read this 1999 paper on Linear Gaussian models and I am pretty amazed at how deep this paper is in unifying the different common data analysis methods and linear models under one framework. We think of principal component analysis (PCA), or Gaussian mixture models (GMM), or Kalman filter models (KF) all as disparate ways to model data, but this review is able to bring them under the umbrella of the Expectation Maximization (EM). I wanted to highlight for myself (and anyone reading) the key high level concepts and insights and also extend these to talk about control systems.

At a very simplifying level, linear gaussian models are heavily used in all branches of engineering from control systems, to data analysis. Expectation maximization is an iterative learning algorithm for learning some optimal parameters in a probabilistic model. In this blog post, I attempt to review the main overarching concepts that I believe are important and then also provide some recent work that draws upon the theory of linear gaussian modeling. Specifically, I look at tensor modeling (i.e. a generalization of a linear time-invariant state space model), deep neural networks to provide end-to-end learning of a state space system and variations of these deep state space models. The goal of this post is to provide the reader with a broad overview of the fundamentals that drive linear modeling to the recent state-of-the-art advancements in deep learning that draw from "older" fundamentals.

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

# Conclusions for Gaussian Linear Models
In this post, I attempt to summarize some of the main points in the Roweis paper that I thought were relevant to someone with knowledge in Linear Algebra, Probability & Statistics and Linear Dynamical Systems. The nice thing is that all these very common algorithms and methods can be framed using Expectation Maximization. This point of view links together control theory, linear dynamical systems and machine learning. It points to how general linear Gaussian models are and how general Expectation Maximization is. 

### Dynamic Version of PCA/KMeans?
What happens if we assume a dynamical model, but instead the output noise is zero (i.e. Q=0)? Here, our states are completely determinable if we have our C matrix. For a linear dynamical system, we can perform PCA to obtain our principle components, which can comprise of our C matrix (i.e. how to go from principle values to observed space). For Hidden Markov Models, we can instead perform vector quantization (i.e. KMeans) to obtain our columns of C. Now, we have to actually estimate the A matrix, which is a first-order Markov dynamic matrix (i.e. governing how states change from time t to t+1). Here it boils down to a simple autoregressive (AR(1)) model in continuous time, or first order Markov chain in the discrete space.

# Extensions of Gaussian Linear Models
Here, I talk about some extensions to Gaussian linear models and relate them to our linear models through the lens of probability and statistics; specifically: variational inference and markov chain monte carlo. These are the main techniques in the estimation of an intractable posterior distribution. Here, we'll assume you have basic Bayesian working knowledge and comfortable with the statistics involved.

The setup of the problem is similar to that of Linear Gaussian Models.

$$\dot{x}(t) = f(x(t)) + g(u(t)) + w$$
$$y(t) = h(x(t)) + v$$

where: $w \approx Q(\theta)$ and $v \approx R(\gamma)$ are the state and output noise terms that we assume to be distributed with some distribution $Q,R$ parametrized by $\theta, \gamma$. In addition, now $f, g, h$ are all potentially nonlinear functions analogs of A, B, C. If we define some priors on the distribution of noise for the latent variables, we can perform Bayesian inference given our observed signals, y. That is, we are interested in estimating:

$$P(x|y) \approx P(y|x) P(x)$$

Note, that in convention with literature, P(y|x) is our likelihood of the model and P(x) is our assumed prior distribution on our latent state variable. 

* Variational inference (VI) proceeds by: * 
Fitting the parameters of a family of tractable distributions (e.g. independent Gaussians) to approximate the posterior. For more details, see my blog post on a summary of VI and MCMC.

* Markov Chain Monte Carlo proceeds by: * 
Creating a Markov chain that has convergent properties to the true posterior. Samples are drawn from the "proposal" distribution and are either kept, or rejected based on various algorithms (e.g. important sampling, Gibbs sampling, Hamiltonian Monte Carlo, etc.). For more details, see my blog post on a summary of VI and MCMC.

## Low Rank Tensors (to generalize space, time and other variable dimensions!)
In a Linear Gaussian state space model, in general you are assuming that x, y, u are vectors, while A, B, C are matrices of their respective dimensions. Tensors are higher order generalizations of matrices (e.g. matrices are 2D arrays, while tensors are N-D arrays). So in the context of neural recording data where you have a suite of electrode signals that vary over time, one can think of the system as a 3D tensor (channels X channels X time); this is opposed to a normal linear time-invariant system (i.e. constant A matrix), which would just be represented as a 2D tensor (channels X channels) because time is invariant. Now, just viewing this system as a 3D tensor does not really give much room for improvement because now you are just dealing with a linear time-varying system with N^2 T parameters (N=#channels, T=#time). 

However, in the TVART paper from Rajesh Rao's group, they assume that the system's state transition matrix, A, lies in a low rank tensor. Specifically, this gives the system only a few "unique" A matrices (i.e. system state transition matrices) to choose from at any particular window of data. The number of these unique A matrices is determined by the assumption of the "low-rank" of this tensor. 

One of the shortcomings of this method is that there is no easy way to determine the "low-rankness" of a dataset prior to analyzing it. I imagine that the way to proceed is to use some heuristic measure, such as Bayesian Information Criterion / Aikake's Information Criterion. 

Assuming you have a good choice of the rank, then you can apply some traditional regularizations, such as l1 and l2 regularizations to enforce sparsity and smoothness in the different dimensions of the A 3D tensor (i.e. either in channel space, or in time space). Then the optimal tensor is solved for via convex optimization. The paper uses a combination of conjugate gradient and proximal gradient with Nesterov acceleration for the smooth, and non-smooth objective functions respectively. A review of these optimization terms hopefully can be covered in another blog post on optimization: convex, nonlinear and constrained.

## Deep Kalman Filter
In the paper on the deep Kalman Filter, the authors derive a deep neural network that is a Kalman filter analog. They explicitly assume that the latent state is modeled by a Normal distribution (i.e. $x ~ N(\mu, \Sigma)$) with possible nonlinear interactions between time steps, and that the observations are distributed according to some family of distributions (e.g. Bernoulli if observations are binary).

The neural network architectures that seem to work are the: i) q-RNN (filtering) and ii) q-BRNN (smoothing), which are just recurrent and bi-directional recurrent neural network architectures. They perform variational learning of the latent state parameters by maximizing a derived evidence lower bound (ELBO). In the Variational AutoEncoder paper, they talk about how to perform stochastic gradient descent by performing the re-parameterization trick on the Normal distribution.

They introduce the notion of performing counterfactual inference by introducing an extra variable that the network conditions on. For example, you can include a vectorized variable that determines whether or not you took a drug at time t, or whether or not a specific action was taken. Then during testing, you can modify the conditional variable action and perform forward prediction to determine the x(t+1), ..., x(t+T) steps which predicts what "would have" happened if you took a certain action.

### Caveats of the DKF
In experiments, they show that the DKF does not extract information about time-derivatives very well, which in general lead to problems with forward prediction.

## Deep Extend To Control (EC2)
In this paper, they combine optimal control theory and deep learning.

## Deep Variational Bayes Filter
In this paper, they argue that a suite of previous methods that use a VAE-style for time series is optimized for reconstruction mainly (i.e. not prediction). This will just compress the data in the best possible manner, while allowing the data to still be reconstructed. However, there is no explicit optimization for prediction. In addition, previous methods may not explicitly include the necessary mini-batch data for the model to infer time-derivatives, thus weakening prediction as well.

First, we want to reparametrize the transition model:

$$x(t+1) = f(x(t), u(t), \beta(t))$$

## Deep Koopman Model
### Quick Koopman Theory Overview
For the reader (and myself), I assume we have no idea what the Koopman operator is. So first, I will overview some of the basic concepts here, so that I can introduce the Deep Koopman model. See https://www.mit.edu/~arbabi/research/KoopmanIntro.pdf for a great in-depth overview. One should be relatively comfortable with the theory of linear dynamical systems and matrix analysis (specifically the idea of state transition matrices, linearity and eigenvalues/eigenvectors). Recall a linear dynamical system without input:

$$\dot{x}(t) = Ax(t)$$

where A is our linear operator of the form $T: \mathbf{R}^n -> \mathbf{R}^n$.

The idea of the Koopman operator is that any data we collect in a real-world scenario are "observables" of our system that are a function of the underlying state (g). So the Koopman operator is a linear transformation (U) that acts on the state transition operator (A). An eigenvalue decomposition of the Koopman operator yields (possibly infinite-dimensional) eigenfunctions that span the observable space, so now all observables of a dynamical system are linear combinations of the eigenfunctions of the Koopman operator. This is quite fascinating because the idea is that you can break down nonlinear system phenomena in terms of linear Koopman eigenfunctions (nonlinear approximation by linear functions)! 

$$Ug(x) = g o T(x)$$

For example, we can look at:
1. Limit Cycles:
This is a nonlinear system property because no linear dynamical system (i.e. x(t+1) = Ax(t)) can generate limit cycles. A limit cycle is parametrized by a period, T. So one can perform Fourier decomposition:

$$g(x(t)) = \sum_{k=0}^{\infty} a_j e^{ikt2\pi / T}$$

The $a_j$ are Fourier coefficients and the exponential term can be constructed as the eigenfunctions of the Koopman operator with eigenvalues $\lambda_k = ik2\pi / T$ (interestingly when eigenvalues are of this form, you have degenerate discrete time-sampling in the sense that you can lose controllability, or observability of dynamical system). 

2. Hyperbolic Fixed Points
3. Basins of Attraction (stable limit cycles)

Now in general, you can perform Koopman mode decomposition on a vector of observables (no one just observes one data point). You get:

$$U^t g(x) = \sum_{k=0}^{\infty} g_k e^{\lambda_k t} \phi_k(x)$$

where U is our Koopman operator, g is our observable function of our state, x is our state vector, $g_k$ are the Koopman modes of the observable g at the eigenvalue $\lambda_k$, $\phi_k$ are the eigenfunctions at their respective eigenvalue.

### Now the Deep Koopman Model
In this paper, they parametrize the observable function using a deep neural network, and then explicitly model the decoding as a Koopman operator to learn the mappings of a latent state back into the observable data. In addition, they add special training scheme of penalizing the loss over consecutive predictive steps, so that the model learns a stable mapping that attempts to keep low error rates over many consecutive predictions.

TBD

## Deep Kalman Variational Autoencoders (DKVAE)
In this paper, the authors formulate yet another variation of the VAE framework that is somewhat similar to the DVBF model, but with a few differences and improvements. Recall that the model for the DVBF was for locally linear transitions:

$$x(t+1) = A(t)x(t) + B(t)u(t) + C(t)w(t)$$
$$y(t) = H(t)x(t) + y(t)$$

Here, the variational parameters that parametrize the variational family is $v(t) = \{A(t)^{i}, B(t)^{i}, C(t)^{i}\}$.

In the DKVAE, the model adds an additional pseudo-latent state, which is of low-dimension between the high dimensional observation space and the linear state space model. 

TBD

## Possibilities for Improved Deep State Space Models (DSSM) 
It seems that a reoccuring theme right now in deep learning is the integration of older techniques (i.e. Linear State Space Models LSSM) with deep neural networks. Since deep neural networks can act as universal function approximators, that are also able to be trained end-to-end using stochastic gradient descent on data, then many challenges in traditional LSSM that had intractable setups can potentially be overcome. Granted, you will need enough data for each situation you are thinking of, but in theory one can really extend the power of DSSM to provide improved interpretability of a deep learning model.

# References:
1. Roweis S. et al. "A Unifying Review of Linear Gaussian Models".http://mlg.eng.cam.ac.uk/zoubin/papers/lds.pdf
2. "Deep Kalman Filter."  https://arxiv.org/abs/1511.05121
3. "Deep Variational Bayes Filter." https://arxiv.org/abs/1605.06432
4. "Deep Koopman Model." https://arxiv.org/pdf/1805.07472.pdf
5. "Kalman VAE." https://arxiv.org/pdf/1710.05741.pdf
6. "Time Varying Autoregression with Low-Rank Tensors (TVART)."
7. "Introduction to Koopman Theory." https://www.mit.edu/~arbabi/research/KoopmanIntro.pdf