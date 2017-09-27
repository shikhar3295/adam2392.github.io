Title: Important Concepts for Computational Modeling
Date: 2017-9-27
Category: Academic
Tags: phd, journals, reviews, computational modeling,
Slug: fundamental-computational-modeling
Authors: Adam Li
Summary: To keep a log of important concepts in computational modeling. 

<!-- MarkdownTOC -->

- Background
- Concepts
    - 1. Numerical Integration
    - 2. Deterministic and Stochastic Differential Equations
    - 1. Deterministic vs Stochastic

<!-- /MarkdownTOC -->
# Background
Computational modeling involves setting up mathematical equations that represent some sort of statics, or dynamics within a system. You want to simulate these equations to understand behavior, fixed points, bifurcations and changes wrt parameter values.

# Concepts
## 1. Numerical Integration
Numerical integration involves solving system of differential equations via numerical methods. This is in general split into deterministic vs stochastic differential equations. Here we will also split the two.

### Deterministic Differential Equations
1) Euler's Method


2) Runge-Kutta Method(s)?

### Stochastic Differential Equations
Heun methods seem to be more accurate, but more time consuming vs the Milstein method.
1) Heun Method
Simple discretization leading to Stratonovich integral. It is a "predictor-corrector method" because given value of X at time $t_n$, obtain predictors with Euler integration scheme, then correct it using Heun's correction.

Details to be filled in.

2) Milstein Method
Uses the derivative of the diffusion coefficients

### Considerations:
1) Convergence


### References:
1. Comparison of stochastic integration https://arxiv.org/pdf/1102.4401.pdf
2. 

## 2. Deterministic and Stochastic Differential Equations
### Deterministic Differential Equations
An example would be a population growth model. 

$dx_t = Kx_t dt,\ x(0)=x_0$, with K being some constant.

However, if we have some inherent randomness, then maybe we can't assume $x_0$ is deterministic constant, but perhaps a random variable.

### Stochastic Differential Equations
An example would be a population growth model. 

$dX_t(w) = KX_t(w) dt,\ X_0(w)$, with K being some constant and $X_t(w)$ is a random variable, which comes from the initial condition. K could also be random.

$dX_t(w) = (Kdt + dW_t(w))X_t(w) dt,\ X_0(w)$, where $dW_t(w)$ is some noise process that adds randomness to K.

This leads us to the general SDE. 

$dX_t(w) = f_t(X_t(w))dt + \sigma_t(X_t(w))dW_t(w),\ X_0(w)$, where f is the deterministic drift of the SDE. $\sigma_t$ is the diffusion coefficient, and $dW_t(w)$ is the noise process. 

We can rewrite the SDE in integral form, which leads us to the Stratonovich integral and the Ito integral.

$X_t(w) = X_0(w) + \int_t_0 f_s(X_s(w)) ds + \int_t_0 \sigma_s(X_s(w)) dW_s(w)$

Ito integral =>
Stratonovich integral =>

### References:

## 1. Deterministic vs Stochastic
### References:
### Summary / Conclusions:

### Important Notes: