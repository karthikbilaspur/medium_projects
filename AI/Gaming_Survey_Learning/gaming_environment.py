import numpy as np
import pandas as pd
from gym import spaces

class GamingEnvironment:
    def __init__(self, data):
        self.data = data
        self.state_space = spaces.Discrete(len(data))
        self.action_space = spaces.Discrete(5)
        self.reward_range = (-10, 10)

    def reset(self):
        self.state = np.random.randint(0, len(self.data))
        return self.state

    def step(self, action):
        next_state = np.random.randint(0, len(self.data))
        reward = self.calculate_reward(self.state, action, next_state)
        done = False
        return next_state, reward, done, {}

    def calculate_reward(self, state, action, next_state):
        # Reward function based on survey data
        respondent = self.data.iloc[state]
        if action == 0 and respondent['gaming_frequency'] == 'daily':
            return 10
        elif action == 1 and respondent['gaming_frequency'] == 'occasional':
            return 5
        # ...
        else:
            return -5