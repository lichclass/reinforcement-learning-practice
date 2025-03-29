
---
### The K-armed bandit problem

In the k-armed bandit problem, we have an agent who chooses between "k" actions and receives a reward based on the action it chooses.

It is a fundamental problem in reinforcement learning, often used to study exploration vs. exploitation trade-offs.

Example: Medical Trial
- Agent = Doctor
- k (actions) = 3
	- The doctor prescribes 3 treatments: blue, red, yellow treatment
- Reward = welfare of the patient upon receiving treatment
---
#### Action-Values

To know which action is the best, we must define the value of taking each action. These values are Action-Values i.e. action-value function:
$$q_*(a) := \mathbb{E}[R_t|A_t=a], \forall \in \{1,...,k\}$$
where,
- $\mathbb{E}[R_t|A_t=a]$, expected reward in a time step given action $a$
- $\forall \in \{1,...,k\}$, for each possible action

The equation is defined as (the sum of all possible rewards)
$$q_*(a) := \mathbb{E}[R_t|A_t=a] = \sum_r p(r|a)r$$
The goal is to maximize the expected reward
$$\underset{a}{argmax} q_*(a)$$
Example: Medical Trial
![[Pasted image 20250213001812.png]]

---
#### Learning Action Values

In the medical trial problem, the doctor will run many trials to learn about each treatment. Each day they could use all the previously collected data to estimate which treatment is believed to be the best.

The value of an action is the expected reward when that action is taken.
$$q_*(a):=\mathbb{E}[R_t|A_t=a]$$
- $q_*(a)$ is not known, so we estimate it using ***sample-average method***
$$
\begin{eqnarray}
Q_t(a) &:=& \frac{\text{sum of rewards when $a$ taken prior to $t$}}{\text{number of times $a$ taken prior to $t$}} \\ 
Q_t(a) &=& \frac{\sum^{t-1}_{i=1}R_i}{t-1}
\end{eqnarray}
$$
![[Pasted image 20250213003800.png]]
In reality, doctors will always choose the best treatment after running some trials. In this case, the doctor will choose **Yellow (0.75)** as it has the highest estimate. This method is called **Greedy Action Selection**
![[Pasted image 20250213004051.png]]

---
#### Estimating Action Values Incrementally

**Incremental update rule**

The **incremental update rule** is used to compute the **running average of action-value estimates** efficiently without storing all past rewards.
$$
\begin{eqnarray}
Q_{n+1} &=& \frac{1}{n}\sum^n_{i=1}R_i \\
&=& Q_n+\frac{1}{n}(R_n-Q_n)
\end{eqnarray}
$$
$$NewEstimate \leftarrow OldEstimate + StepSize[Target-OldEstimate]$$
$$Q_{n+1}=Q_n+\alpha_n(R_n+Q_n)$$
where,
- $\alpha_n \rightarrow [0,1]$
- In the step-size average, it is $\alpha_n=\frac{1}{n}$

**Non-stationary Bandit Problem**

In the medical trial, some treatment, say Treatment B (Blue) is more effective during winter months. The agent (Doctor) doesn't know this, but would like to adapt.

Solution: **Fixed Step Size** 
- Through this, the recent rewards affect more than older rewards.
- **Decaying Past Rewards:**
$$Q_{n+1}=(1-\alpha)^nQ_1+\sum^n_{i=1}\alpha(1-\alpha)^{n-i}R_i$$
- Or simply using this equation, and set the step_size to a **Fixed Number**:
$$Q_{n+1}=Q_n+\alpha_n(R_n+Q_n)$$
---
#### Exploration and Exploitation Trade-off

- **Exploration** - improve knowledge for long-term benefit
- **Exploitation** - exploit knowledge for short-term benefit

How do we choose to **explore** and when to **exploit**? 

**Method 1:** Epsilon-Greedy Action Selection

$$
A_t \leftarrow
\begin{cases}
	\underset{a}{argmax} \text{ } Q_t(a) & \text{with probability $1-\epsilon$} \\
	a \sim Uniform(\{a_1...a_k\}) & \text{with probability $\epsilon$}
\end{cases}
$$
The **ε-greedy action selection** method balances **exploration and exploitation** by choosing the **greedy action** (the one with the highest estimated reward) with probability $1-\epsilon$ and selecting a **random action** with probability $\epsilon$. This ensures the agent explores occasionally to discover better actions while mostly exploiting the best-known option.

**Method 2:** Optimistic Initial Values
Ex. Medical Trials
$$
\begin{eqnarray}
Q_1(P) = 2.0 \\
Q_1(Y) = 2.0 \\
Q_1(B) = 2.0 \\
\end{eqnarray}
$$
**Optimistic Initial Values** encourage exploration by initializing action-value estimates Q(a)Q(a)Q(a) to **high values** instead of zero or random guesses. Since early actions tend to have lower rewards, the agent is driven to explore different arms to **"correct" the overestimation**, leading to better long-term learning in **stationary** environments.

**Method 3:** Upper Confidence Bound Action Selection
$$
\begin{eqnarray}
A_t &:=& argmax \left[ Q_t(a) + c\sqrt{\frac{ln t}{n_t(a)}} \right] \\
&:=& argmax \left[ Q_t(a) + c\sqrt{\frac{ln \text{ timestamps}}{\text{time action a taken}}} \right]
\end{eqnarray}
$$
where,
- $c$ is a confidence level hyperparameter that controls the exploration-exploitation trade-off
	- **Larger $c$** → More exploration: The algorithm prioritizes trying less-explored actions more often.
	- **Smaller $c$** → More exploitation: The algorithm focuses more on the best-known actions.

The **Upper Confidence Bound (UCB)** action selection method balances **exploration and exploitation** by selecting actions based on both their estimated value $Q_t(a)$ and an exploration bonus. The bonus, $c\sqrt{\frac{ln t}{n_t(a)}}$ ,favors actions with **high uncertainty** (i.e., those taken fewer times), ensuring that under-explored actions are tried more often. This approach is particularly effective in **stationary bandit problems**, as it systematically reduces uncertainty over time while favoring high-reward actions.