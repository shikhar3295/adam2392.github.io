Title: Optimization: Convex, Nonlinear, Unconstrained and Constrained
Date: 2019-06-18
Category: Machine Learning
Tags: phd, machine learning
Slug: optimization-landscape-overview
Authors: Adam Li
Summary: An overview of optimization frameworks and algorithms under different general settings.

<!-- MarkdownTOC -->

- Background
- Methods
    - Convex
        - Non-smooth
        - Smooth
    - Unconstrained
    - Constrained
    - Nonlinear
        - Unconstrained
        - Constrained
    - Zero-Finding: Newton's Method and the Secant Method
        - Newton Directions, General Newton Method and Quasi-Newton Methods
    - Programming \(Linear, Quadratic and Semidefinite\)
- Stochastic Optimization
- Conclusions
- Current Research and Interesting Papers
    - Accelerated Adaptive Moments \(ADAM\)
    - RMS-Prop
    - Structured Regularizations and Different Forms
- References:

<!-- /MarkdownTOC -->

# Background

Recently, I re-read my notes on convex optimization, nonlinear unconstrained optimization and nonlinear constrained optimization. It's quite fascinating how mathematics can break down very general assumptions into different classes of algorithms with certain convergence, convergence rate and computational cost guarantees. In general all these algorithms are iterative algorithms, that solve a certain optimization problem by taking iterations from a starting vector $x_0$. Obviously, there are other classes of algorithms that can say be solved analytically (i.e. one shot), but we're interested in how to take iterations that converge, converge fast and are computationally efficient. The different classes of algorithms can at a high level be broken down into:

* convex vs nonconvex
* constrained vs unconstrained
* linear vs nonlinear
* differentiable vs non-differentiable (or smooth vs nonsmooth)

In each of these classes of algorithms there are relatively important concepts that are present in all of them such as:

* regularization (i.e. the addition of a l1, l2, or p-norm operator on some variable of interest) to prevent overfitting, include prior knowledge into the model, and improve tractability
* duality (i.e. the idea of solving a related "dual" problem that has nice properties)
* initialization (i.e. $x_0$)
* step length (i.e. $\alpha_t$)
* direction of algorithm iteration (i.e. $g_t$)

In general, one is interested in necessary and/or sufficient conditions for optimality and the following questions:

1. does an algorithm converge and what are the necessary assumptions to do so?
2. what is the convergence rate of an algorithm (i.e. how many iterations to reach a bound on the error rate)?
3. what is the computational cost per iteration of the algorithm (i.e. how many function evaluations, jacobian evaluations, or hessian evaluations does one need)?

What I will not overview is combinatorial and stochastic optimization. I will plan on adding the general concepts once I've reviewed linear, quadratic, and semidefinite programming, as well as stochastic gradient descent. 

# Methods
Here, I preface the landscape of optimization algorithms with the general objective function:

$$minimize_{x \in X} f(x) \ s.t. \ g(x)=0,\ h(x) \le 0$$
$$X \subset \mathbf{R}^n$$
$$f: X -> \mathbf{R}$$
$$g: X -> \mathbf{R}^k$$
$$h: X -> \mathbf{R}^l$$

There are k equality constraints, and l inequality constraints. X is our feasible set, f is our evaluation function (think loss/cost function), g is our equality constraint function, and h is our inequality constraint function. x is our variable of interest that we want in the end that satisfies this minimization problem.

A very general iteration looks something like this:

$$x_{k+1} = x_k - \alpha_k g_k (x_k)$$

where $\alpha$ is the step size, g is the step direction. Note that $\alpha$ can either be a vector, or scalar (depending on if you want to step uniformly, or with varying magnitudes in the direction vector) and g is a in general a vector that denotes the directionality in the space of x (i.e. $R^n$).

## Convex
In this section, we make the assumption that f is convex, and in general the constraint functions are convex. Assuming convexity provides a couple of strong guarantees:

* the minimum we find is a global minimum, so we don't have to say rerun the algorithm with multiple initializations
* in general strong duality applies, so there is a zero duality gap (I think)

There is a whole theory of convex analysis and convex optimization, but here we review the main algorithms that come out of this convex assumption. In general, the algorithms can be broken down into non-smooth vs smooth (where f is either differentiable, or not). If f is not differentiable, a technical detail is that we still assume f is Lipschitz-continuous. 

### Non-smooth
Here, we are dealing with convex functions that are not differentiable. We are able to circumvent the issue with the use of subgradients and proximal operators. This leads to algorithms like:

1. Subgradient Descent Algorithm
This is essentially gradient descent, but using the subgradient. It's a basic algorithm that has guaranteed convergence with some assumptions on the choices of your step sizes, $\alpha_k$.

2. Proximal Gradient Descent Algorithm
This defines a proximal operator that IS differentiable, so that we can take gradients of the proximal operator to define our direction, and then take corresponding steps. This leads to algorithms like the iterative shrinkage threshold operator (ISTA).

*Acceleration (Nesterov)*
Armed with the proximal gradient, one can apply acceleration techniques of the form:

$$ $$

, which leads to algorithms like FISTA (fast ISTA).

### Smooth
Here, we are dealing with convex functions that ARE differentiable (i.e you can take the derivative). Taking the derivative gives you powerful first-order information. This leads to algorithms like:

1. Gradient Descent
2. Conjugate Gradient Descent
3. 

## Unconstrained
In this section, we comment on the idea of unconstrained optimization. That is the objective function does not have g, or h terms (equality, or inequality constraints). In general, this leads to two classes of algorithms:

* line-search methods (e.g. Armijo line-search and Wolfe conditional line search)
* trust-region methods

For convex and linear optimization problems, generally you don't need such methods, so we restrict overview until we reach the section on Nonlinear optimization.

## Constrained
In this section, we allow for constraints either in the form of equality, and/or inequality constraints. The idea of adding constraints is really fascinating because in most (almost all) real world problems, you can formulate a loss function to optimize (based on some metric) that generally has constraints built in! This is due to the nature of the problem. For example, if you want to optimize usage of fuel in a car, you are constrained by the amount of fuel you can even have and the fact that fuel can never be negative! In general, adding constraints helps the optimization problem achieve better solutions. In order to analyze a constrained optimization problem, the strategy is to perform a "conversion" into an unconstrained problem. This leads to the definition of a Lagrangian function (draws upon physics):

$$L(x,y,\lambda,\mu) = $$

There is a wealth of theory behind constraint optimization with some of the basics drawing from the idea of Lagrange multipliers (that handle equality constraints). One can generalize this notion (it's quite beautiful actually) to inequality constraints, which then handle all possible constraints you might have. This generalization leads to the notion of the Karusch-Kuhn-Tucker (KKT) conditions for optimality. The KKT conditions are:

* stationarity:
* primal feasibility:
* dual feasibility:
* complementary slackness: 

In general, these define necessary conditions for optimality, and in some special cases, they can define also sufficient conditions. Basically, with KKT conditions, you can convert any constrained optimization problem into an unconstrained version with the Lagrangian.

I don't actually talk about the algorithms here because they get quite complex, but I will cover them in the "Programming (Linear, Quadratic and Semidefinite)" section in the future.

## Nonlinear
In this section, we now deal with the possibility of nonlinear functions f, and possibly nonlinear constraint functions. This then leads to the problem that in general, we can not find a global minima of the optimization problem. We simply find local minimums that may, or may not be a useful solution and possibly rerun the algorithms with multiple intializations. 

### Unconstrained
1. Line-Search Methods
The purpose of line search methods is to define a direction of search first and then perform a line search to determine a good step size. The procedure is as follows:

* solve for a descent direction $B_k$. In general, it is difficult to get this for high-dimensional systems exactly because you can't compute the Hessian.
* perform a line search to determine the step size $\alpha_k$.

Here, we review two main line search methods: 
* exact line search: Armijo line search (backtracking line search) and 
* inexact line search with satisfied Wolfe conditions.

The wolfe conditions are conditions for choosing a step length, $\alpha_k$, given a descent direction $p_k$:

* (Armijo rule) $f(x_k + \alpha_k p_k) \le f(x_k) + c_1 \alpha_k p_k^T \Nabla f(x_k)$
* (curvature condition) -p_k^T \Nabla f(x_k + \alpha_k p_k) \le -c_2 p_k^T \Nabla f(x_k)

Armijo rule ensures that the step length decreases f sufficiently. The curvature condition ensures that the slope has been reduced sufficiently. With the strong Wolfe conditions, there is a different curvature condition:

* $|p_k^T \Nabla f(x_k + \alpha_k p_k)| \le c_2 |p_k^T \Nabla f(x_k)|$

with $0 < c_1 < c_2 < 1$. If $p_k$ is a descent direction, then we just need to satisfy:

$$p_k^T \Nabla f(x_k) < 0$$

with $p_k = -\Nabla f(x_k)$ as the gradient direction, or with $p_k = - H^{-1} \Nabla f(x_k)$ with H being positive definite as the Newton-Raphson direction. 

2. Trust Region Methods
The purpose of trust region methods is to define a region that is "trustworthy" to move in the direction of a local optima. The idea is to first perform a "line search" and then determine the direction of search. A trust region algorithm solves a subproblem that uses the gradient information and Hessian (or approximation) information.

### Constrained
See section on Programming. 

## Zero-Finding: Newton's Method and the Secant Method
1. Secant method
This method essentaially uses an iteration of secant lines and their roots to better approximate a root of the original function of interest, f. It is similar to a finite-difference approximation of Newton's method.

$$x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}$$

2. Newton's method

$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$

This Newton's method can be approximated when Jacobians and Hessians are too expensive, by using the class of quasi-newton methods, such as the BFGS method.

### Newton Directions, General Newton Method and Quasi-Newton Methods
TBD

## Programming (Linear, Quadratic and Semidefinite)
TBD

# Stochastic Optimization
This section deserves a header of its own because of its widespread usage nowadays in training deep neural networks and actually any optimization problem that can't necesesarily fit into RAM. 
TBD

# Conclusions

# Current Research and Interesting Papers
## Accelerated Adaptive Moments (ADAM)
TBD

## RMS-Prop
TBD

## Structured Regularizations and Different Forms
TBD

# References:
1. Cvx Course, JHU. https://sites.google.com/site/danielprobinson/convex-optimization
2. "Convex Optimization." https://web.stanford.edu/~boyd/cvxbook/
3. 

