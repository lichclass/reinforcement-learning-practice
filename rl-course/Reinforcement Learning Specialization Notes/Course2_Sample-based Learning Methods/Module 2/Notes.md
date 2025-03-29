### Monte Carlo Method

**Monte Carlo** methods learn directly from interaction.

**PSEUDOCODE: Monte Carlo Prediction, for estimating $V \approx v_\pi$**
	Input: a policy $\pi$ to be evaluated
	Initialize:
		$V(s) \in \mathbb{R}$, arbitrarily, for all $s \in S$
		$Returns(s) \leftarrow$ an empty list, for all $s \in S$
	Loop forever (for each episode):
		Generate an episode following $\pi: S_0, A_0, R_1, A_1, R_2,...,S_{T-1}, A_{T-1}, R_T$
		$G \leftarrow 0$
		Loop for each step of episode, $t = T-1, T-2,...,0:$
			$G \leftarrow \gamma G + R_{t+1}$
			Append $G$ to $Returns(S_t)$
			$V(S_t) \leftarrow average(Returns(S_t)))$

**Incremental Update of the New Estimate** (To avoid  keeping the samples returns in a list)
$$
NewEstimate \leftarrow OldEstimate + StepSize[Target - OldEstimate]
$$

---
### Using Monte Carlo for Prediction

**Monte Carlo Prediction** is used to learn the value function of a policy

**Monte Carlo learning** is computationally efficient

**Implications of Monte Carlo learning**
- We do not need to keep a large model of the environment
- We are estimating the value of an individual state independently of the values of other states
- The computation needed to update the value of each state does not depend on the size of the MDP

---
### Using Monte Carlo for Action Values

![[Screenshot 2025-02-23 at 7.49.55 PM.png]]

**Key Idea:** Action-values help an agent learn the best policy by comparing different actions in the same state. However, if an agent follows a deterministic policy, it may never explore all possible actions, missing potentially better ones.

![[Screenshot 2025-02-23 at 7.53.46 PM.png]]

**Real-World Example:** If you always take the same route home, you’ll never know if a newly built road is faster unless you try it.

**Solution - Exploring Starts:** To ensure every state-action pair is visited, the agent starts in random states with random actions. This way, it explores all possible situations and learns the best decisions over time.

**Monkey Analogy:** Each time the monkey wakes up, it starts in a **random tree** and explores different branches. Over time, it discovers which trees and paths yield the most bananas 🍌.

---
### Using Monte Carlo methods for generalized policy iteration (Monte Carlo - Exploring Starts)

**Generalized Policy Iteration (GPI)** alternates between:

1. **Policy Evaluation** – Estimating how good a policy is.
2. **Policy Improvement** – Updating the policy using the estimated values.

**Monte Carlo in GPI:**

- **Monte Carlo Policy Evaluation**: Estimates value functions using sampled returns from actual episodes.
- **Monte Carlo Policy Improvement**: Updates the policy by selecting actions that maximize expected returns.

By iterating these steps, the agent refines its policy toward optimality **without needing a predefined model**, making it ideal for unknown environments.

**PSEUDOCODE:** 
![[Screenshot 2025-02-23 at 8.22.18 PM.png]]

##### **Algorithm Steps**
1. **Initialize:**
    - Arbitrary policy $\pi(s)$ for all states $s$.
    - Arbitrary action-value function $Q(s,a)$.
    - Empty return lists for all $(s,a)$.
2. **Loop for each episode:**
    - **Exploring Starts:** Start at a random state-action pair $(S_0,A_0)$.
    - Generate a full episode **following policy $\pi$**.
    - Set return $G=0$.
3. **Loop through the episode in reverse:**
    - Compute return: $$ G \leftarrow G + R_{t+1}$$
    - Store GGG in the return list for $(S_t, A_t)$.
    - Update action-value function: $$Q(S_t,A_t)=average(Returns(S_t,A_t))$$
    - Improve policy: $$\pi(S_t)=\underset{a}{argmax}Q(S_t,a)$$
##### **Key Takeaways**

- **Exploring starts** ensures **all actions are tried** at least once.
- Uses **sample-based learning** (no need for transition probabilities).
- **Policy improves over time** by selecting actions with the highest estimated return.
- Works well in **model-free** environments like Blackjack.

---
### Epsilon-soft policies

An **epsilon-soft policy** balances **exploitation (choosing the best action)** and **exploration (trying random actions)** by ensuring every action has a **non-zero probability** of being chosen.

Formula:
- Optimal action probability: $$\pi(a_*|s)=1-\epsilon \frac{\epsilon}{|A|}$$
- Other actions: $$\pi(a|s)=\frac{\epsilon}{|A|}$$
**Monkey Analogy**
Imagine you're a monkey trying to find **the best banana tree** 🍌🌳.
#### **🐵 Without Epsilon-Soft Policy (Greedy Monkey)**
- You **always go to the same tree** because it gave you bananas before.
- But what if there's a **better tree nearby**?
- You **never explore**, so you **might be missing the juiciest bananas**! 😢
#### **🐵 With Epsilon-Soft Policy (Smart Monkey)**
- **Most of the time** ($\sim 1-\epsilon$), you go to your **favorite tree**.
- **Sometimes** ($\sim \epsilon$), you **try a different tree** to check if it has better bananas.
- This way, you **still eat bananas daily**, but **you also discover new, better trees** over time! 🍌🎉

**PSEUDOCODE:**
![[Pasted image 20250223212404.png]]

### **Algorithm Steps: MC Control for ϵ\epsilonϵ-Soft Policies**
1. **Initialize:**
    
    - Set an **arbitrary $\epsilon$-soft policy** $\pi(s)$ for all states sss.
    - Initialize the **action-value function** $Q(s,a)$ arbitrarily.
    - Create **empty return lists** for all $(s,a)$.
2. **Loop for each episode:**
    
    - **Generate an episode** following the current policy $\pi$:$$S_0, A_0,R_1,A_1,R_2,...,S_T,A_T,R_T$$ 
    - Set return $G=0$.
3. **Loop through the episode in reverse:**
    
    - Compute return: $$G \leftarrow \gamma G+R_{t+1}$$
    - Store $G$ in the return list for $(S_t, A_t)$.
    - Update action-value function: $$Q(S_t,A_t)=average(Returns(S_t,A_t))$$
    - Improve policy: $$A^* = \underset{a}{argmax}Q(S_t,a)$$ $$\pi(a|S_t) =
\begin{cases} 
  1 - \epsilon + \frac{\epsilon}{|A(S_t)|}, & \text{if } a = A^* \\
  \frac{\epsilon}{|A(S_t)|}, & \text{otherwise}
\end{cases}
$$
    - 
1. **Repeat until convergence.**

---
#### Additional Fixes for Epsilon-soft Monte Carlo

1. **Ensure that the policy dictionary is properly structured before updating it**
```
# Initialization
policy = defaultdict(lambda: {0: 0.5, 1: 0.5})

# Inside Monte Carlo Update
if state not in policy:
	policy[state] = {0: 0.5, 1: 0.5}
```
2. **Returns are not tracked separately for each episode (First-Visit MC Not implemented)**
```
# Inside Monte Carlo Update
G = 0
visited = set()

for state, action, reward in reversed(episode):
	G = reward + G
	if (state, action) not in visited: # First Visit Check
		visited.add((state, action))
		returns[(state, action)].append(G)
		Q[state][action] = np.mean(returns[(state, action)])
```
3. **ϵ Does Not Decay (Agent Keeps Exploring Too Much)**
```
# Inside training loop
for episode_num in range(num_episodes):
	epsilon = max(epsilon_min, epsilon_start * (epsilon_decay ** episode_num))
```

---
### Why does off-policy learning matter?

**On-Policy** improve and evaluate the policy being used to select actions.

**Off-Policy** improve and evaluate a different policy from the one used to select actions.

#### Understanding Off-Policy Learning

**Behavior Policy vs. Target Policy**
- **Behavior Policy:** 
	- The policy that the agent follows to interact with the environment and collect data. 
	- The policy that we are choosing actions from
	- The policy that generates experience (i.e., the actions the agent actually takes while exploring)
	- Denoted by, $$b(a|s)$$
- **Target Policy:** 
	- The policy we want to evaluate or improve. 
	- The policy that we are learning
	- It defines the probability of selecting an action given a state
	- If we want to learn the optimal policy for Blackjack, $\pi$ represents the best learned strategy.
	- Denoted by, $$\pi(a|s)$$
**Why it matters?**
- It can learn from historical data. It can train on past experiences instead of relying on fresh data.
- Better exploration-exploitation tradeoff. Behavior policy explores while the target policy improves.
- Faster policy improvement. Learns optimal actions even if they weren't chosen in training.

---
### Importance Sampling

**Importance sampling** uses samples from probability distribution to estimate the expectation of a different distribution. Crucial for off-policy learning, where the goal is to evaluate or **improve a target policy** using **data collected form a different behavior policy.**

Formula: $$\mathbb{E}_\pi[X] \approx \frac{1}{n} \sum^n_{i=1}x_i \rho(x_i), \text{ where } \rho(x)=\frac{\pi(x)}{b(x)}, x=(A_t|S_t)$$

**Key Takeaway:** Importance sampling helps RL agents **evaluate & improve policies using past data** without restarting learning.

---
### Off-Policy Monte Carlo Prediction

**What is Importance Sampling?**
Estimates the value functions for a policy π with samples collected previously from an older policy π

**Off-Policy Trajectories** $$\rho_{t:T-1} := \prod^{T-1}_{k=t} \frac{\pi(A_k|S_k)}{b(A_k)|S_k}$$
**Off-Policy Value** $$\mathbb{E}_b[\rho_{t:T-1}G_t|S_t=s]=v_\pi(s)$$

**PSEUDOCODE**
![[Screenshot 2025-02-24 at 1.35.27 PM.png]]

### **Algorithm Steps: Off-Policy Every-Visit Monte Carlo Prediction**

1. **Initialize:**
    
    - Set **arbitrary value estimates** $V(s)$ for all states $s$.
    - Create **empty return lists** for each state sss, denoted as $Returns(s)$.
2. **Loop for each episode:**
    
    - **Generate an episode** following the **behavior policy $b$:** $$S_0,A_0,R_1,S_1,A_1,R_2,...,S_T,A_T,R_T$$
    - Set return $G=0$ and weight factor $W=1$.
3. **Loop through the episode in reverse:**
    
    - Compute return: $$G \leftarrow \gamma{WG}+R_{t+1}$$
    - Store $G$ in the return list for $S_t$​.
    - Update value function: $$V(S_t)=average(Returns(S_t))$$
    - Adjust importance sampling weight: $$W \leftarrow W \times \frac{\pi(A_t|S_t)}{b(A_t|S_t)}$$
    - **Stop updating if $W=0$ (i.e., when the behavior policy probability $b(A_t|S_t)$ is 0.**
4. **Repeat until convergence.**

Note: The **weight factor $W$** in **Off-Policy Every-Visit Monte Carlo** is a correction term used to **adjust for the difference between the behavior policy** $b$ (which collects data) and the **target policy** $\pi$ (which we want to evaluate).

---
### Batch Reinforcement Learning

### **Understanding Batch Reinforcement Learning**

- **Definition:** Batch reinforcement learning involves learning policies from a fixed dataset of experiences, rather than through online interaction with the environment.​

### **Key Points Discussed by Emma Brunskill**

1. **Offline Data Utilization:**
    
    - Emphasizes the importance of leveraging pre-collected data, especially in scenarios where real-time data collection is expensive or impractical.​
2. **Challenges in Batch RL:**
    
    - **Distributional Shift:** The mismatch between the data distribution in the batch and the distribution encountered when deploying the learned policy.​
    - **Exploration Limitations:** Since the data is fixed, the agent cannot explore new actions beyond what is present in the dataset.​
3. **Applications of Batch RL:**
    
    - Useful in fields like healthcare, where patient data can be used to inform treatment policies without conducting new experiments.​
    - Applicable in industrial settings where equipment data can help optimize maintenance schedules without additional downtime.​

Understanding batch reinforcement learning is crucial for developing policies that are both effective and safe, especially in environments where online exploration is limited or risky.​