Title: Bayesian Analysis: An Overview
Date: 2019-06-18
Category: Machine Learning
Tags: phd, machine learning
Slug: bayesian-landscape-overview
Authors: Adam Li
Summary: An overview of Bayesian analysis and the general approaches to solving Bayesian problems.
status: draft

<!-- MarkdownTOC autolink="true" -->

- [Background](#background)
- [Methods](#methods)
    - [Analytical Solution](#analytical-solution)
        - [The Power of the Normal Distribution](#the-power-of-the-normal-distribution)
        - [Conjugate Priors](#conjugate-priors)
    - [Variational inference \(VI\)](#variational-inference-vi)
        - [Evidence Lower Bound \(ELBO\)](#evidence-lower-bound-elbo)
    - [Markov Chain Monte Carlo \(MCMC\)](#markov-chain-monte-carlo-mcmc)
        - [Gibbs Sampling](#gibbs-sampling)
        - [Importance Sampling](#importance-sampling)
        - [Hamiltonian Monte Carlo \(HMC\)](#hamiltonian-monte-carlo-hmc)
- [Conclusions](#conclusions)
    - [Variational Autoencoder \(VAE\)](#variational-autoencoder-vae)
    - [Combining MCMC and VI](#combining-mcmc-and-vi)
    - [](#)
- [References:](#references)

<!-- /MarkdownTOC -->

# Background
In any sort of data analysis, you generally formulate a model that answers some question based on an estimation of a variable. 

Kullman-Leiback Divergence (KL)

# Methods
Here, I talk about some extensions to Gaussian linear models and relate them to our linear models through the lens of probability and statistics; specifically: variational inference and markov chain monte carlo. These are the main techniques in the estimation of an intractable posterior distribution. Here, we'll assume you have basic Bayesian working knowledge and comfortable with the statistics involved.

The setup of the problem is similar to that of Linear Gaussian Models.

$$\dot{x}(t) = f(x(t)) + g(u(t)) + w$$
$$y(t) = h(x(t)) + v$$

where: $w \approx Q(\theta)$ and $v \approx R(\gamma)$ are the state and output noise terms that we assume to be distributed with some distribution $Q,R$ parametrized by $\theta, \gamma$. In addition, now $f, g, h$ are all potentially nonlinear functions analogs of A, B, C. If we define some priors on the distribution of noise for the latent variables, we can perform Bayesian inference given our observed signals, y. That is, we are interested in estimating:

$$P(x|y) \approx P(y|x) P(x)$$

Note, that in convention with literature, P(y|x) is our likelihood of the model and P(x) is our assumed prior distribution on our latent state variable. 

## Analytical Solution

### The Power of the Normal Distribution

### Conjugate Priors

## Variational inference (VI)
* Variational inference (VI) proceeds by: * 
Fitting the parameters of a family of tractable distributions (e.g. independent Gaussians) to approximate the posterior. For more details, see my blog post on a summary of VI and MCMC.

### Evidence Lower Bound (ELBO)

## Markov Chain Monte Carlo (MCMC)
* Markov Chain Monte Carlo proceeds by: * 
Creating a Markov chain that has convergent properties to the true posterior. Samples are drawn from the "proposal" distribution and are either kept, or rejected based on various algorithms (e.g. important sampling, Gibbs sampling, Hamiltonian Monte Carlo, etc.). For more details, see my blog post on a summary of VI and MCMC.

### Gibbs Sampling

### Importance Sampling

### Hamiltonian Monte Carlo (HMC)

# Conclusions

## Variational Autoencoder (VAE)
TBD

## Combining MCMC and VI
TBD

## 

# References:
1. "Deep Variational Bayes Filter." https://arxiv.org/abs/1605.06432
2. "Deep Koopman Model." https://arxiv.org/pdf/1805.07472.pdf
3. "Kalman VAE." https://arxiv.org/pdf/1710.05741.pdf
4. https://www.cs.princeton.edu/courses/archive/fall11/cos597C/lectures/variational-inference-i.pdf
5. https://www.cs.cmu.edu/~epxing/Class/10708-15/notes/10708_scribe_lecture14.pdf
6. https://blog.evjang.com/2016/08/variational-bayes.html
