
---
#### Policy Evaluation vs. Control

**Policy Evaluation** - the task of determining the state-value function $v_\pi$ for a specific policy $\pi$

**Control** - The task of finding a policy to obtain as much reward as possible. In other words, finding a policy which maximizes the value function.

**Dynamic Programming** techniques can be used to solve both these tasks, if we have access to the dynamics function $\mathbb{P}$

---
#### Iterative Policy Evaluation (Prediction)

It has two versions:
- Two arrays storing the **old state-values** and **new state-values**
- **In-place** update of every state-value in every state

**PSEUDOCODE: Iterative Policy Evaluation, for estimating $V \approx v_\pi$**

1. Input $\pi$, the policy to be evaluated (Initialize the arrays to 0)
		$V \leftarrow \overset{\rightarrow}{0}, V' \leftarrow \overset{\rightarrow}{0},$
2. Loop:
		$\delta \leftarrow 0$
		Loop for each $s \in S$:
			$V'(s) \leftarrow \sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r+\gamma V(s')]$
			$\delta \leftarrow max(\delta, |V'(s) - V(s)|)$
		$V \leftarrow V'$
	until $\delta < \theta \text{ a small positive number}$
3. Output $V \approx v_\pi$

**NOTE:** $\theta$ is used to evaluate the difference between the old state-value and the new state-value i.e. if you set the theta into a very small number, it means if there is no little change in between the old and new state-value, it means it already converged.

Summary:
- We can turn the Bellman equation into an update rule, to iteratively compute value functions.
---
#### Policy Improvement (Control)

**Control** refers to the task of improving a policy

Recall:
$$
\pi_*(s) := \underset{a}{argmax} \sum_{s'} \sum_{r} p(s',r|s,a)[r+\gamma v_*(s')]
$$

The new policy is a strict improvement over $\pi$ , unless $\pi$ is already optimal

**Policy Improvement Theorem** - tells us that a greedified policy is a strict improvement.
$$
\begin{eqnarray}
\text{(1) } q_\pi(s, \pi'(s)) &\geq& q_\pi(s, \pi(s)) \text{ for all } s \in \rightarrow \pi' \geq \pi \\
\text{(2) }q_\pi(s, \pi'(s)) &>& q_\pi(s, \pi(s)) \text{ for at least one } s \in \rightarrow \pi' \geq \pi
\end{eqnarray}
$$
(2) means that $\pi'$ is strictly better if the value is strictly greater in at least one state.

Use the Value function under a given policy, to produce a better policy

---
#### Policy Iteration

Recall (Policy Improvement Theorem):
$$
\pi' := \underset{a}{argmax} \sum_{s'} \sum_{r} p(s',r|s,a)[r + \gamma v_{\pi}(s')]
$$
$\pi'$ is strictly better than $\pi$, unless $\pi$ was already optimal

![[Pasted image 20250219161429.png]]

**PSEUDOCODE: Policy Iteration (using iterative policy evaluation) for estimating $\pi \approx \pi_*$**

1. Initialization
		$V(s) \in \mathbb{R} \text{ and } \pi(s) \in \mathbb{A}(s) \text{ arbitrarily for all } s \in S$
2. Policy Evaluation
	Loop:
		$\delta \leftarrow 0$
		Loop for each $s \in S$:
			$V'(s) \leftarrow \sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r+\gamma V(s')]$
			$\delta \leftarrow max(\delta, |V'(s) - V(s)|)$
		$V \leftarrow V'$
		until $\delta < \theta \text{ a small positive number determining the accuracy of estimation}$
3. Policy Improvement
	policy-stable $\leftarrow$ true
	For each $s \in S$:
		old-action $\leftarrow \pi(s)$
		$\pi(s) \leftarrow \underset{a}{argmax} \sum_{s', r}p(s',r|s,a)[r + \gamma V(s')]$
		If old-action $\neq \pi(s)$, then policy-stable $\leftarrow$ false
	If policy-stable, then stop and return $V \approx v_*$ and $\pi \approx \pi_*$; else go to 2

**Policy Iteration** works by alternating **policy evaluation** and **policy improvement**.

Policy iteration follows a sequence of better and better policies and value functions until it reaches the optimal policy and associated value function.

---
#### Flexibility of the Policy Iteration Framework

**Value Iteration** allows us to combine policy evaluation and improvement into a single update

**Asynchronous** dynamic programming methods give us the freedom to update states in any order

**Generalized Policy Iteration** unifies classical DP methods, value iteration, and asynchronous DP

**PSEUDOCODE: Value Iteration, for estimating $\pi \approx \pi_*$**

Algorithm parameter: small threshold $\theta > 0$ determining accuracy of estimation
Initialize $V(s)$, for all $s \in S^+$, arbitrarily except that $V(terminal)=0$

Loop:
	$\delta \leftarrow 0$
	Loop for each $s \in S$:
		$v \leftarrow V(s)$
		$V(s) \leftarrow \underset{a}{max} \sum_{s',r} p(s',r|s,a)[r+\gamma V(s')]$
		$\delta \leftarrow max(\delta, |v - V(s)|)$
until $\delta < \theta$

Output a deterministic policy, $\pi \approx \pi_*$, such that
	$\pi(s) = \underset{a}{argmax} \sum_{s',r}p(s',r|s,a)[r+\gamma V(s')]$

**Value Iteration** updates using the action that maximizes the current value estimate compared to Iterative Policy Evaluation which updates the value according to a fixed policy.

---
#### Efficiency of Dynamic Programming

**Monte Carlo Method (Sampling Alternative for Policy Evaluation)** 

The Monte Carlo Method is a computational technique that uses random sampling to solve problems that might be deterministic but are too complex for analytical solutions. It is widely used for numerical integration, optimization, and simulating systems with many variables or uncertain parameters. 

Ex. Imagine you want to know the average outcome of a complicated board game, but the game has too many possibilities to calculate by hand. Instead, you play the game many times and record the results. The Monte Carlo method is like this—it uses lots of random "plays" or samples to estimate what will happen on average.

**Brute-Force Search**

Brute-force search is a straightforward problem-solving technique that systematically checks all possible candidates to find a solution. It doesn't rely on heuristics or shortcuts, which means that while it's simple and guarantees finding the answer if one exists, it can become computationally expensive and inefficient as the size of the search space grows.

Ex. Think of brute-force search like trying every key on a key ring to open a door. It checks every possibility until it finds the correct one. While this method is simple and guarantees a solution if one exists, it can be very slow when there are many possibilities, because it doesn't take any shortcuts.

**Bootstrapping**

Bootstrapping in this context is similar to improving your estimate of a situation by using what you already know. Instead of waiting to see the full outcome, you update your predictions step by step, using current estimates to inform new ones. This can make the process faster and more efficient because you don't have to wait until the end of a long process (like an entire game) to start learning and improving your predictions.

Summary
- Bootstrapping can save us from performing a huge amount of unnecessary work