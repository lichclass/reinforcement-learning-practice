#### **Policy Evaluation vs. Control**
- **Policy Evaluation:** Determines the state-value function $v_\pi$ for a given policy $\pi$
- **Control:** Find a policy that maximizes the value function.
- **Dynamic Programming (DP):** can be used for both if the dynamics functions $\mathbb{P}$ is available.

---
### **Iterative Policy Evaluation (Prediction)**
- Uses the **Bellman equation** iteratively to compute value functions.
- Two update methods:
	- **Two arrays:** One stores old state-values, another stores new state-values.
	- **In-place updates:** Each state-value is updated immediately.
- **Convergence Criterion:** Stops when the change in values is below a small threshold $\theta$
![[Screenshot 2025-03-01 at 8.57.53 PM.png]]

---
#### **Policy Improvement (Control)**
- **Goal:** Improve the policy based on value estimates.
- **Policy Improvement Theorem**:
	- If a policy $\pi'$ is greedy with respect to $v_\pi$, then is is as **as good or better** than $\pi$.
	- If $q_\pi(s,\pi'(s)) > q_\pi(s,\pi(s))$ in at least one state, then $\pi'$ is strictly better.
- **Outcome:** A better policy can be generated using the value function.

---
#### **Policy Iteration**
- Alternates between:
	1. **Policy Evaluation:** Compute $v_\pi$ for the current policy.
	2. **Policy Improvement:** Generate a better policy using $v_\pi$.
- **Convergence:** The process stops when the policy remains unchanged, meaning it has reached the optimal policy $\pi_*$.
![[Screenshot 2025-03-01 at 9.02.49 PM.png]]

---
#### **Flexibility of the Policy Iteration Framework**
- **Value Iteration**:
	- Merges policy evaluation and improvement into a single step.
	- Updates each state using the **best possible action** instead of a fixed policy.
- **Asynchronous DP:**
	- Allows updating states in **any order**, making computations more flexible.
- **Generalized Policy Iteration (GPI):**
	- A unification of **value iteration, policy iteration, and asynchronous DP**
![[Screenshot 2025-03-01 at 9.05.35 PM.png]]

---
#### **Efficiency of Dynamic Programming**
- **Monte Carlo Method:**
	- Uses **random sampling** instead of explicit DP calculations
	- Example: Instead of calculating all possible outcome of a board game, Monte Carlos plays multiple games and averages results.
- **Brute-Force Search:**
	- Checks **all possible actions**, ensuring correctness but is computationally expensive.
	- Example: Trying every key on a key ring to unlock a door.
- **Bootstrapping**:
	- **Uses current estimates** to improve predictions, rather than waiting for the final outcome.
	- **Saves computation** by updating step by step instead of waiting for full episode results.