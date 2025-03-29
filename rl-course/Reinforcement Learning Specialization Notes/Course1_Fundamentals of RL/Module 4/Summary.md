
---
#### **Specifying Policies**
- A **policy** determines an agent's behavior by mapping states to actions.
- **Deterministic policy:** Maps each state to a single action: $$\pi(s) = a$$
- **Stochastic policy:** Assigns probabilities to each action in each state: $$\pi(a|s)$$
- Policies only depend on the current state
---
#### **Value Functions**
- Value functions estimate **future return** under a specific policy.
- **State-Value Function** $(v(s))$: $$v(s) = \mathbb{E}[G_t|S_t=s]$$
	- Expected return from a given state
- **Action-Value Function** ($q_\pi(s,a)$): $$q_\pi(s,a) := \mathbb{E}_\pi[G_t|S_t=s,A_t=a]$$
	- Expected return if the agent selects action $a$ and then follows policy $\pi$
---
#### **Bellman Equations**
- Defines relationships between values of states and their possible successors.
- **State-Value Bellman Equation** (recursive formula for $v_\pi(s)$): $$v_\pi(s)=\underset{a}{\sum} \pi(a|s) \underset{s',r}{\sum}p(s',r|s,a)[r+\gamma{v_\pi(s')}]$$
- **Action-Value Bellman Equation** (recursive formula for $q_\pi(s,a)$): $$q_\pi(s,a)=\underset{s',r}{\sum}p(s',r|s,a)[r+\gamma{\underset{a'}{\sum}}\pi(a'|s')q_\pi(s',a')]$$
- The Bellman Equations allow values of the current state/action to be expressed recursively in terms of future values.
---
#### **Why Use Bellman Equations?**
- They allow solving value functions as a system of linear equations
- **Direct Solutions** are only feasible for small Markov Decision Processes (MDPs)
- **Approximations** are needed for large-scale problems

---
#### **Optimal Policies**
- An **optimal policy $\pi_*$** achieves the **highest value function** in all states.
- At least **one optimal policy always exists**, though there may be multiple

---
#### **Optimal Value Functions**
- A policy $\pi_1$ is better than $\pi_2$ if: $$v_{\pi_1}(s) \geq v_{\pi_2}(s), \forall s \in S$$
- **Optimal state-value function $v_*(s)$**: $$v_*(s) = \underset{\pi}{\text{max }}v_\pi(s)$$
- **Optimal action-value function $q_*(s,a)$**: $$q_*(s,a) = \underset{\pi}{\text{max }} q_\pi(s,a)$$
- **Bellman Optimality Equations**:
	- For **state-value $v_*$**: $$v_*(s) = \underset{a}{max} \underset{s',r}{\sum}p(s',r|s,a)[r+\gamma{v_*(s')}]$$
	- For **action-value $q_*$**: $$q_*(s,a) = \underset{s',r}{\sum}p(s',r|s,a)[r+\gamma{\underset{a'}{\text{ max }}} q_*(s',a')]$$
---
#### **Using Optimal Value Functions to Determine Optimal Policies**
- If we have $v_*$ **(Optimal state-value function)**, we can derive the optimal policy.
- If we have $q_*$ **(Optimal action-value function)**, deriving the optimal policy is even easier.