#### **Monte Carlo Methods**
- **Definition**: Monte Carlo (MC) methods learn directly from interaction with the environment by estimating values from sampled episodes.
- **Monte Carlo Prediction**: Estimates the value function of a given policy using episode returns.
- **Incremental Update:** Uses the formula: $$NewEstimate \leftarrow OldEstimate + StepSize \times (Target-OldEstimate)$$![[Screenshot 2025-03-01 at 9.22.01 PM.png]]

---
#### **Using Monte Carlo for Prediction (Advantages)**
- Doesn't require a model of the environment
- Estimates state values independently
- Computationally efficient as it doesn't depend on the size of the MDP

---
#### **Using Monte Carlo for Action Values**
- **Challenge:** A deterministic policy may not explore all actions.
- **Solution - Exploring Starts:**
	- Ensures all state-action pairs are visited by starting from random states and actions.
- **Real-World Example:** Taking the same route home prevents discovering a potentially faster one.
- **Analogy:** A monkey starting in a different tree each time learns the best banana-yielding paths.

---
#### **Monte Carlo in Generalized Policy Iteration (GPI)**
- **Policy Iteration Cycle:**
	1. **Policy Evaluation:** Estimate how good the policy is.
	2. **Policy Improvement** - Update policy based on estimated values.
- **Monte Carlo in GPI:**
	- **Policy Evaluation:** Uses sampled returns to estimate value functions.
	- **Policy Improvement:** Selects actions that maximize expected returns.
![[Screenshot 2025-03-01 at 9.27.57 PM.png]]

---
#### **Epsilon-Soft Policies**
- **Balances:**
	- **Exploitation:** Choosing the best-known action
	- **Exploration:** Trying random actions with some probability.
- **Formula:**
	- Optimal action probability: $$\pi(a_*|s)=1-\epsilon+\frac{\epsilon}{|A|}$$
	- Other actions: $$\pi(a|s)=\frac{\epsilon}{|A|}$$
- **Monkey Analogy**
	- **Greedy Monkey:** Always chooses the same banana tree and might miss better options.
	- **Smart Monkey:** Mostly chooses the best tree but occasionally explores new ones.

---
#### **Epsilon-Soft Monte Carlo Control**
![[Screenshot 2025-03-01 at 9.32.18 PM.png]]**Additionals, Common Fixes:**
1. Ensure policy dictionary is structured correctly:
```
policy = defaultdict(lambda: {0: 0.5, 1: 0.5})
```
2. **Implement First-Visit MC** to track returns separately:
```
visited = set()
for state, action, reward in reversed(episode):
	if(state, action) not in visited:
		visited.add((state, action))
		returns[(state, action)].append(G)
```
3. **Decay epsilon over time:**
```
epsilon = max(epsilon_min, epsilon_start * (epsilon_decay ** episode_num))
```

---
#### **Why Does Off-Policy Learning Matter?**
- **On-Policy:** Improves and evaluates the same policy that selects actions.
- **Off-Policy:** Evaluate a different policy from the one generating actions.

**Behavior Policy vs. Target Policy**
- **Behavior Policy** ($b$): The policy that collects data.
- **Target Policy** ($\pi$): The policy being improved.
- **Benefits:**
	- Learns from past data.
	- Balances exploration and exploitation.
	- Enables faster policy improvement.

---
#### **Importance Sampling**
- **Definition:** Estimates expectations using samples from a different probability distribution.
- **Formula:** $$\mathbb{E}_\pi[X] \approx \frac{1}{n} \underset{i=1}{\sum^n}x_i \rho(x_i), \rho(x)=\frac{\pi(x)}{b(x)}$$
- **Key Takeaway:** Allows RL agents to evaluate and improve policies using past data.

---
#### **Off-Policy Monte Carlo Prediction**
- Uses importance sampling to estimate values from a different behavior policy.
- Off-Policy Trajectories: $$\rho_{t:T-1} := \underset{k=t}{\prod^{T-1}} \frac{\pi(A_k|S_k)}{b(A_k|S_k)}$$
![[Screenshot 2025-02-24 at 1.35.27 PM.png]]
![[Screenshot 2025-03-01 at 9.43.39 PM.png]]

---
#### **Batch Reinforcement Learning**
- **Definition:** Learns from a fixed dataset instead of interacting with the environment.
- **Challenges:**
	- **Distributional Shift:** Differences between training data and real-world scenarios.
	- **Limited Exploration:** Cannot try new actions beyond the dataset.
- **Applications:**
	- **Healthcare:** Learning treatment policies from patient data.
	- **Industry:** Optimizing Maintenance using equipment data.