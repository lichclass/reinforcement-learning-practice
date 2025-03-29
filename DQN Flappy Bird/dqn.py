import torch
from torch import nn
import torch.nn.functional as F

class DQN(nn.Module):

    def __init__(self, state_dim, action_dim, hidden_dim=256):
        super(DQN, self).__init__()

        # Input layer to hidden layer
        self.fc1 = nn.Linear(state_dim, hidden_dim) 
        # Hidden layer to output layer
        self.fc2 = nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        # Apply ReLU activation to hidden layer
        x = F.relu(self.fc1(x)) 
        return self.fc2(x)

