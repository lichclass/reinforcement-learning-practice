
#### **K-Armed Bandit Problem**

- An agent selects one of **k** actions and receives a reward.
- It models the **exploration vs. exploitation** trade-off in reinforcement learning.


#### **Action-Values**

- Action-value function represents the expected reward for an action:
$$
q_*(a) := \mathbb{E}[R_t|A_t=a]=\underset{r}{\sum}p(r|a)r
$$
- The objective is to select actions that maximize expected reward:
$$
\underset{a}{\text{arg max }} q_*(a)
$$

#### **Learning Action Values**

- Ex. The doctor conducts multiple trials to **estimate** the best treatment.
- **Sample-average method** estimates action-values:
$$
Q_t(a) = \frac{\sum_{i=1}^{t-1}R_i}{t-1}
$$
- **Greedy Action Selection:** Always selecting the highest estimated reward.


#### **Incremental Action-Value Estimation**

- **Incremental Update Rule** efficiently updates action values without storing all past rewards:
$$
Q_{n+1} = Q_n + \frac{1}{n}(R_n-Q_n)
$$
- **Fixed Step Size** is used in **non-stationary** problems:
$$
Q_{n+1} = Q_n + \alpha(R_n-Q_n)
$$

#### **Exploration and Exploitation Trade-off**

- **Exploration** - Tries new actions for potential long-term gains.
- **Exploitation** - Chooses the best-known action for short-term rewards.

#### **Exploration Strategies**

1. **Epsilon-Greedy Action Selection**
	- Selects the best action with probability $1 - \epsilon$
	- Selects a random action with probability $\epsilon$
	- Ensures occasional exploration
2. **Optimistic Initial Values**
	- Start **Q-values high** to encourage exploration
	- Example:$$ Q_1(P) = Q_1(Y) = Q_1(B) = 2.0 $$
	- Agent explores because early rewards are lower.
3. **Upper Confidence Bound (UCB) Selection**
	- Selects actions using: $$ A_t = \text{arg max } \left[ Q_t(a) + c \sqrt{\frac{\text{ln t}}{n_t(a)}} \right]  $$
	- $c$ controls exploration:
		- **High c** $\rightarrow$ More exploration.
		- **Low c** $\rightarrow$ More exploitation.
	- **Balances exploration and exploitation dynamically**
	

---
### **CUES**

- Q1. What are **non-stationary problems**? 
	- **ANSWER:** It is a problem where the environment's reward distribution **changes over time**.