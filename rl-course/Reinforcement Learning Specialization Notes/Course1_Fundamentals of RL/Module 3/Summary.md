
#### **Markov Decision Processes (MDPs)**

- Extends the k-armed bandit problem to account for different actions in different situations.
- **Agent:** Learner and decision-maker.
- **Environment:** The external system the agent interacts with.
- **States:** Information available to the agent at a given time.

#### **MDP Dynamics**

- Similar to k-armed bandits but includes **stochastic outcomes**.
- Actions lead to multiple possible next states and rewards.
- **Markov Property:** Future states and rewards depend only on the present state.

#### **Example: Recycling Robot**

- A robot collects soda cans and makes decisions based on battery levels.
- **States (S)** and **Actions (A)** define its decision-making process.
- **Key Rule:** Recharge action is only available when the battery is low.

#### **Goal of Reinforcement Learning**

- **Maximize expected return:** The sum of all rewards from following a policy.
- **Episode:** A sequence of interactions from a start to a terminal state.
	- **Return (Non-stochastic):** $G_t = R_{t+1} + R_{t+2} + ... + R_T$
	- **Return (Stochastic):** $\mathbb{E}[G_t] = \mathbb{E}[R_{t+1} + R_{t+2} ... + R_T]$

#### **Episodic vs. Continuing Tasks**

- **Episodic Tasks**
	- Interaction breaks into separate **episodes**
	- Each episode ends in a **terminal state**
	- Episodes are independent
- **Continuing Tasks**
	- No terminal state; interaction goes on indefinitely
	- **Solution: Discounting future rewards**

#### **Discounting Future Rewards**

- **Formula:** $$G_t = R_{t+1} + \gamma{R_{t+2}} + \gamma^2{R_{t+2}} + ... + \gamma^{k-1}{R_{t+k}} + ...$$
- Discount factor ($\gamma$) ensures that future rewards are **finite.**
- **Effect of $\gamma$:**
	- $\gamma = 0$: **Short-sighted** agent, focuses only on immediate rewards.
	- $\gamma = 1$: **Far-sighted** agent, values long term rewards.

#### **Recursive Nature of Returns**

- Return can be expressed recursively: $$G_t = R_{t+1} + \gamma{G_{t+1}}$$
- This property is **essential for dynamic programming solutions** in RL.