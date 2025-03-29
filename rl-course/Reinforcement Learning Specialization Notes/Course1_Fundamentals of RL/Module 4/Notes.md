
---
#### Specifying Policies

**Policies** tell an agent how to behave in their environment.

**Deterministic policies** maps each state to a single action,
$$\pi(s)=a$$

| State | Action |
| :---: | :----: |
| $s_0$ | $a_1$  |
| $s_1$ | $a_0$  |
| $s_2$ | $a_0$  |

**Stochastic policy** assigns probabilities to each action in each state,
$$\pi(a|s)$$

![[Pasted image 20250216174700.png]]
**Note:** Probabilities can be different in each state
![[Pasted image 20250216200609.png]]

Summary:
- A policy maps the current state onto a set of probabilities for taking each action
- Policies can only depend on the current state
---
#### Value Functions

**Value Functions** estimate future return under a specific policy.

**State-Value function** is the future reward an agent can expect to receive starting from a particular i.e. the state-value function is the expected return from a given state.
$$
v(s) := \mathbb{E}[G_t|S_t=s]
$$

**Action-Value function** describes what happens when the agent first selects a particular action. The action value of a state is the expected return if the agent selects action A and then follows policy $\pi$.
$$
q_\pi(s,a) := \mathbb{E}_\pi[G_t|S_t=s, A_t=a]
$$
---
#### Bellman Equality Derivation

**Bellman Equations** define a a relationship between the value of a state, or state-action pair, and its possible successors.

**State-value Bellman Equation**
$$
\begin{eqnarray}
v_\pi &:=& \mathbb{E}_\pi[G_t|S_t=s] \\
&=& \mathbb{E}_\pi[R_{t+1}+\gamma G_{t+1}|S_t=s] \\
&=& \sum_a \pi(a|s) \sum_{s'} \sum_{r} p(s',r|s,a)[r+\gamma\mathbb{E}_\pi[G_{t+1}|S_{t+1}=s']] \\
&=& \sum_a \pi(a|s) \sum_{s'} \sum_{r} p(s',r|s,a)[r + \gamma v_\pi(s')]
\end{eqnarray}
$$
**Action-value Bellman Equation**
$$
\begin{eqnarray}
q_\pi(s,a) &:=& \mathbb{E}_\pi [G_t|S_t=s,A_t=a] \\
&=& \sum_{s'} \sum_{r} p(s',r|s,a)[r + \gamma \mathbb{E}_\pi[G_{t+1}|S_{t+1}=s']] \\
&=& \sum_{s'} \sum_{r} p(s',r|s,a)[r + \gamma \sum_{a'} \pi(a'|s') q_\pi(s', a')]
\end{eqnarray}
$$
Summary:
- The current time-step's state/action values can be written recursively in terms of future state/action values.
---
#### Why Bellman Equations

You can use the Bellman Equations to solve for a value function by writing a system of linear equations.

We can only solve small MDPs directly, but Bellman Equations will factor into the solutions we see later for large MDPs

---
#### Optimal Policies



An **optimal policy** $\pi_*$ is as good as or better than all the other policies. The policy with the highest possible value function in all states. It also achieves the highest value possible in every state.
![[Pasted image 20250216184004.png]]
Note: At least one optimal policy always exists, but there may be more than one

---
#### Optimal Value Functions

Recall that,
	$\pi_1 \geq \pi_2$ if and only if $v_{\pi_1}(s) \geq v_{\pi_2}(s)$ for all $s \in S$

then, the value of the optimal policy is defined to be the largest of all the computed values.

**Denoted as $v_*$ for state-value function**
$$
v_{\pi_*} := \mathbb{E_{\pi_*}}[G_t|S_t=s] = \underset{\pi}{max}\text{ }v_\pi(s) \text{ for all } s \in S
$$
**Denoted as $q_*$ for action-value function**
$$
q_{\pi_*}(s,a) = \underset{\pi}{max } \text{ } q_\pi(s,a)
 \text{ for all } s \in S \text{ and } a \in A$$

**The Bellman Optimality Equation for $v_*$**
$$
v_*(s) = \underset{a}{max} \sum_{s'} \sum_{r} p(s',r|s,a)[r + \gamma v_*(s')]
$$
**The Bellman Optimality Equation for $q_*$**
$$
q_*(s, a) = \sum_{s'} \sum_{r} p(s', r|s, a)[r+\gamma \text{ $\underset{a'}{max}$ }q_*(s', a)]
$$
The **Bellman Optimality Equations** relate the value of a state, or state-action pair, to its possible successors under any optimal policy.

---
#### Using Optimal Value Functions to Get Optimal Policies

![[Pasted image 20250216195817.png]]
![[Pasted image 20250216200301.png]]
Summary:
- Once we have the optimal state value function, it's relatively easy to work out the optimal policy.
- If we have the optimal action-value function, working out the optimal policy is even easier.
