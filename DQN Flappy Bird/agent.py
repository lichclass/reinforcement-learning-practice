import flappy_bird_gymnasium
import gymnasium
from dqn import DQN
from experience_replay import ReplayMemory
import itertools
import yaml
import random
import torch
from torch import nn

class Agent:
    
    def __init__(self, hyperparameter_set):
        with open('hyperparameters.yml', 'r') as stream:
            all_hyperparameter_sets = yaml.safe_load(stream)
            hyperparameters = all_hyperparameter_sets[hyperparameter_set]

        self.replay_memory_size = hyperparameters['replay_memory_size']
        self.mini_batch_size = hyperparameters['mini_batch_size']
        self.epsilon_init = hyperparameters['epsilon_init']
        self.epsilon_decay = hyperparameters['epsilon_decay']
        self.epsilon_min = hyperparameters['epsilon_min']
        self.network_sync_rate = hyperparameters['network_sync_rate']
        self.learning_rate_a = hyperparameters['learning_rate_a']
        self.discount_factor_g = hyperparameters['discount_factor_g']

        self.loss_fn = nn.MSELoss()
        self.optimizer = None
        
    def run(self, is_training=True, render=False):
        # env = gymnasium.make("FlappyBird-v0", render_mode="human", use_lidar=False)
        env = gymnasium.make("CartPole-v1", render_mode="human" if render else None)

        num_states = env.observation_space.shape[0] # Shows the number of states
        num_actions = env.action_space.n # Shows the number of actions

        rewards_per_episode = []
        epsilon_history = []

        policy_dqn = DQN(num_states, num_actions)

        if is_training:
            memory = ReplayMemory(self.replay_memory_size)
            epsilon = self.epsilon_init

            target_dqn = DQN(num_states, num_actions)
            target_dqn.load_state_dict(policy_dqn.state_dict())

            step_count=0

            self.optimizer = torch.optim.Adam(policy_dqn.parameters(), lr=self.learning_rate_a)


        for episode in itertools.count():
            state, _ = env.reset()
            state = torch.tensor(state, dtype=torch.float32)
            terminated = False
            episode_reward = 0.0

            while not terminated:
                # Select an action
                if is_training and random.random() < epsilon:
                    action = env.action_space.sample()
                    action = torch.tensor(action, dtype=torch.int64)
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(dim=0)).squeeze().argmax()

                # Processing:
                new_state, reward, terminated, _, info = env.step(action.item())
                new_state = torch.tensor(new_state, dtype=torch.float32)

                # Accumulate Reward
                episode_reward += reward

                if is_training:
                    memory.append((state, action, new_state, reward, terminated))
                    step_count += 1
                
                # Move to the new state
                state = new_state
                
            rewards_per_episode.append(episode_reward)

            epsilon = max(epsilon * self.epsilon_decay, self.epsilon_min)
            epsilon_history.append(epsilon)

            if len(memory) >= self.mini_batch_size:
                mini_batch = memory.sample(self.mini_batch_size)
                self.optimize(mini_batch, policy_dqn, target_dqn)

                if step_count > self.network_sync_rate:
                    target_dqn.load_state_dict(policy_dqn.state_dict())
                    step_count=0

            print(f'Episode: {episode}, Reward: {episode_reward}, Epsilon: {epsilon}')

    def optimize(self, mini_batch, policy_dqn, target_dqn):
        for state, action, new_state, reward, terminated in mini_batch:
            
            if terminated:
                target = reward
            else:
                with torch.nn.no_grad():
                    target_q = reward * self.discount_factor_g * target_dqn(new_state).max()

            current_q = policy_dqn(state)

            loss = self.loss_fn(current_q, target_q)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

if __name__ == '__main__':
    agent = Agent('cartpole1')
    agent.run(is_training=True, render=True)