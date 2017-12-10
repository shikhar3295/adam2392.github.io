Title: Important Papers for Fundamentals in Computational Neuroscience / Data Science
Date: 2017-9-25
Category: Academic
Tags: phd, journals, reviews
Slug: fundamental-papers
Authors: Adam Li
Summary: To keep a log of important papers I read about and how they are relevant.
<!-- MarkdownTOC -->

- Papers
    - 1. Wilson-Cowan Neural Mass Model
    - 2. Kalman Filter Model
    - 3. Expectation Maximization
    - 4. Information Bottleneck Method
    - 5. Opening the Black Box of Deep Neural Networks Via Information
    - 6. Reinforcement Learning: An Overview
    - 7. Deep Reinforcement Learning: An Overview
    - 8. Variational Inference:

<!-- /MarkdownTOC -->

# Papers
## 1. Wilson-Cowan Neural Mass Model
### Summary / Conclusions:

### Important Notes:

## 2. Kalman Filter Model
### Summary / Conclusions:

### Important Notes:

## 3. Expectation Maximization
### Summary / Conclusions:

### Important Notes:

## 4. Information Bottleneck Method
http://www.cs.huji.ac.il/labs/learning/Papers/allerton.pdf
### Summary / Conclusions:
Let us define X as input signal, and Y as desired output.

Here, they were interested in deriving a quantitative method for optimizing 1) compression rate of a signal and 2) the choice of representation of the original signal.

Previous theory looked at minimizing the rate of compression given a constraint on expected distortion of the original signal (with new compression). This was solved via iterative algorithm (similar to EM), but lacked generality to find optimal representatives, which minimize the expected distortion (not just compression) of the signal. 

The new theory looks at minimizing the rate of compression given a constraint on the amount of information we can keep about Y using X. This produces an iterative algorithm that also can be solved iteratively. It also shows that 1) the Kullback-Leibler divergence is the relevant distortion measure for the information bottleneck setting, and 2) optimization of representation of signal and the signal compression can be done together.

This work can be used in applications to information processing problems (e.g. deep learning).

### Important Notes:
Mutual information is defined as:

$I(X;Y) = D_{KL}[P(x,y)||P(x)P(y)] = \sum_{x\in X, y\in Y} P(x,y) log(\frac_{P(x,y)}_{P(x)P(y)})$
$= \sum_{x\in X, y\in Y}P(x,y) log(\frac_{P(x|y)}_{P(x)}) = H(X) - H(X|Y)$

, where $D_{KL}(p||q)$ is the Kullback-Liebler divergence of distributions p and q, and $H(X)$ and $H(X|Y)$ are entropy and conditional entropies, respectively.

We want the optimal representations of signal X with respect to output label Y. Sufficient statistics are maps/partitions of X, S(X) that captures all the information X has about Y. The mutual information given Y is equal. 

$I(S(X); Y) = I(X; Y)$

We can allow the map to be stochastic, with encoder P(T|X) and allow map to capture as much as possible of I(X;Y), not necessarily all of it $I(S(X); Y) \leq I(X; Y)$. Define $t \in T$ as compressed representations of $x \in X$, stochastically, $p(t|x)$. The following optimization problem finds a balance between compression of X and prediction of Y.

$min_{p(t|x),p(y|t),p(t)}\ {I(X;T) - \beta I(T;Y)}$

## 5. Opening the Black Box of Deep Neural Networks Via Information
Reference: https://arxiv.org/pdf/1703.00810.pdf
### Summary / Conclusions:
In this paper, the authors extend their analysis of DNN using information theory. They answered the following questions:

1. The SGD layer dynamics in the Information plane.
First the layers increase $I(T_i;Y)$, and then later decrease $I(X; T_i)$, which corresponds to increasing the information about Y and then later compressing the representation (empirical error minimization & representation compression phase).
2. The effect of the training sample size on the layers.
It seems that sample size does not have an effect on empirical error minimization, but does have an effect on the representation compression. Smaller sample sizes has overfitting, which has been seen as overfitting the sample noise. 
3. What is the benefit of the hidden layers?
Adding hidden layers reduces the number of training epochs. It also seems to accelerate compression, but adding extra width does not seem to help. With layered diffusion of the SGD optimization (backpropagation), it seems that there is an exponential decrease in epochs with K hidden layers.

4. What is the final location of the hidden layers?


5. Do the hidden layers form optimal IB representations?
It seems that the hidden layers converge to the optiaml IB representations. However, we can see that there can be clearly many different layers that correspond to the same IB representation.

Another important hypothesis/conjecture they make is that: attempts to interpret single weights, or even single neurons in such networks can be meaningless because there is a large number of different networks that can achieve optimal performance. This makes sense in terms of how the brain is structured; the brain does not form the same pathway for learning something new between different people, but form a unique network for optimal performance. 
### Important Notes:
First, they estimated the mutual information of the layers with the input and with the labels $I(X;T_i)$ and $I(T_i;Y)$. 

## 6. Reinforcement Learning: An Overview
Reference: https://pdfs.semanticscholar.org/b373/b0c6e3b4fef4ac0534965708fc382343f8dc.pdf

### Summary / Conclusions:

### Important Notes:


## 7. Deep Reinforcement Learning: An Overview
Reference:

## 8. Variational Inference: 
### Summary / Conclusions
Variational inference
### Important Notes 
