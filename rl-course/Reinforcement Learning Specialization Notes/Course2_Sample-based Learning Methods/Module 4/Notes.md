#### **SARSA: GPI with TD**

- **SARSA** is an on-policy **Temporal Difference (TD)** method for RL
- The name "Sarsa" reflects the sequence of states and actions it uses for updates: $$(S_t,A_t,R_{t+1},S_{t+1},A_{t+1})$$
- **On-policy** means the policy used for generating data is the same policy being improved and evaluated.
- **General Policy Iteration (GPI)** is the interplay of policy evaluation and policy improvement; SARSA is an instance of GPI, using TD methods for the evaluation part.
- In **Sarsa**, the action value (Q-value) is updated using the next action $A_{t+1}$ chosen by the current policy, which keeps learning aligned with the exact behavior policy in use.
- Because it is on-policy, it typically requires an $\epsilon-greedy$ exploration strategy or similar, ensuring that all actions continue to have some chance of being selected.
- Update Equation: $$Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha(R_{t+1}+\gamma{Q(S_{t+1},A_{t+1})-Q(S_t,A_t)})$$
- **SARSA Pseudocode Algorithm**
![[Screenshot 2025-03-03 at 6.36.03 PM.png]]

---
#### **SARSA in the Windy Grid World**

- **Windy Grid World Environment**: A grid-based environment where certain columns have an upward "wind" effect, pushing the agent up by a specific number of cells, adding complexity to the navigation task.
- **Learning Parameters**:
	- **Exploration Rate ($\epsilon$)**: Set to 0.1, allowing the agent to explore suboptimal actions 10% of the time to balance exploration and exploitation.​
	- **Learning Rate ($\alpha$)**: Set to 0.5, determining the weight given to new information versus existing knowledge.
![[Screenshot 2025-03-03 at 6.35.24 PM.png]]
---
#### **What is Q-Learning? (Off-policy TD Control)**

- First developed in 1989
- First major online RL algorithm
- Pseudocode of the Algorithm
![[Screenshot 2025-03-03 at 6.42.41 PM.png]]
- **Off-policy**: Learns independently of the actions taken by the current policy.
- **Compared to SARSA:**
	- **Q-learning** is off-policy (uses max future Q), while SARSA is on-policy (follows its own policy).
- **Advantages:** Learns optimal policies even with random exploration.
- **Limitations:** Needs extensive exploration and may struggle in large state spaces without function approximation (e.g., Deep Q-Networks)

---
#### Q-learning in the Windy Grid World

- **Q-learning Characteristics**:
	- **Off-Policy Learning:** Q-learning learns the optimal action-value function independently of the agent's current policy, allowing it to from exploratory actions.
	- **Update Rule:** The Q-learning update rule is: $$Q(S_t,A_t) \leftarrow \alpha[R_{t+1} + \gamma{\underset{a}{max}}Q(S_{t+1},a)-Q(S_t,A_t)]$$
	- where $S_t$ and $A_t$ are the current state and action, $R_{t+1}$ is the reward received after taking action $A_t, S_{t+1}$ is the next state, $\alpha$ is the learning rate, and $\gamma$ is the discount factor.
- **Exploration Strategy**: To ensure sufficient exploration of the state-action space, Q-learning often employs an $\epsilon - greedy$ strategy, where with probability $\epsilon$, the agent selects a random action (exploration), and with probability $1-\epsilon$, it selects the action that maximizes $Q(s,a)$ (exploitation).​
![[Screenshot 2025-03-03 at 6.53.49 PM.png]]
---
#### **How is Q-learning off-policy?**

- Q-learning is off-policy without using importance sampling.
- **Off-policy nature:** Q-learning learns the optimal policy independently of the agent's action.
- **Comparison with SARSA**: Unlike **on-policy SARSA**, which updates based on the action actually taken, Q-learning always updates towards the best estimated future value.
- Learning on-policy or off-policy may perform differently in control

---
#### **Expected SARSA**

- **Expected Sarsa** updates $Q(s,a)$ using the **expected value** over all possible next actions rather than a single action.
- **Update Rule:** $$Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha \left[ R_{t+1} + \gamma{\underset{a}{\sum} \pi(a|S_{t+1})Q(S_{t+1},a)-Q(S_t,A_t)} \right]$$
	- Uses **policy probabilities** $\pi(a|S_{t+1})$ instead of just the maximum Q-value
- **Variance reduction:** More stable than Sarsa since it averages over all actions instead of relying on a single sample.
- **On-policy or Off-policy**: Can be either, depending on how the next state's action probabilities are derived.
- **Exploration strategy:** Often uses $\epsilon-greedy$, balancing exploration and exploitation.
- The Expected Sarsa algorithm explicitly computes the expectation under its policy, which is more expensive than sampling but has lower variance.
- Expected Sarsa with a target policy that's greedy with respect to its action-values is exactly Q-learning

