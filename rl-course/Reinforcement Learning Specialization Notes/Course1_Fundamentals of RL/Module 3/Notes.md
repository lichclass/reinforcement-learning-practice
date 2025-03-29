---

---
---
#### Markov Decision Processes

The k-armed bandit problem does not account for the fact that different situations require different actions. 

Actions influence future situations.

**Agent** - The learner and the decision maker

**Environment** - The thing that the agent interacts

**States** - The set of information that an agent has about the environment at a given time

**The Markov Decision Process Framework**
![[Pasted image 20250213162224.png]]

**The dynamics of an MDP**

Same with the k-arms bandit problem, the outcomes are stochastic (i.e. random). When the agent takes an action in a state, there are many possible next states and rewards. Formalism:
![[Pasted image 20250213162711.png]]
**NOTE:** Future states and rewards depends only from the present state. (i.e. Definition of the Markov Property)

---
#### Examples of Markov Decision Problems

Example: Recycling Robot

A recycling robot that collects empty soda cans. It can detect soda cans and pick them up using its grippers.

![[Pasted image 20250213163204.png]]
**NOTE:** 
- The action ***recharge*** can only be accessed when the battery is ***low***
- $\mathbb{S}$ is defined as the set of states
- $\mathbb{A}$ is defined as the set of actions for a particular state

**Dynamics of the Recycling Robot**
![[Pasted image 20250213163705.png]]

---
#### Goal of Reinforcement Learning

**The goal of an agent is to maximize the expected return.**

**Return** -  the sum of all rewards that the agent expects to receive when following the policy from the state to the end of the episode.

**Episode** - the recording of actions and states that an agent performed from a start state to an end state. The episode is independent of how the previous episode ended, thus, each episode is unique.

In episodic tasks, the agent-environment interaction breaks up into episodes.

**Return (Non-stochastic):** 
$$G_t := R_{t+1}+R_{t_2}+R_{t+3}+...R_T$$
**Return (Stochastic):**
$$\mathbb{E}[G_t] := \mathbb{E}[R_{t+1}+R_{t_2}+R_{t+3}+...R_T]$$---
#### Continuing Tasks

**Episodic Tasks:**
- Interaction breaks naturally into episodes
- Each episode ends in a **terminal state**
- Episodes are independent
$$G_t := R_{t+1}+R_{t+2}+R_{t+3}+...+R_T$$

**Continuing Tasks:**
- Interaction goes on **continually**
- No terminal state
$$G_t := R_{t+1} + R_{T+2} + R_{t+3} + ...$$

One solution to continuing tasks, **Discounting**...
$$
\begin{eqnarray}
G_t &:=& R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} +...+ \gamma^{k-1} R_{t+k} + ... \\
&=& \sum^\infty_{k=0} \gamma^kR_{t+k+1}
\end{eqnarray}
$$
**Discount** the rewards in the future by $\gamma$ where $0 \leq \gamma < 1$

**Discounting** is used to ensure returns are finite


**Effects of** $\gamma$ **on agent Behavior**

**when, $\gamma = 0$ (Short-sighted agent)**
$$G_t = R_{t+1}$$
Agent only cares about the immediate reward

**when, $\gamma \rightarrow 1$ (Far-sighted agent)**

Agent takes future rewards into account more strongly


**Recursive Nature of Returns**
$$
\begin{eqnarray}
G_t &:=& R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} +... \\
&=& R_{t+1} + \gamma(R_{t+2} + \gamma R_{t+3} + ...) \\
&=& R_{t+1} + \gamma G_{t+1}
\end{eqnarray}
$$