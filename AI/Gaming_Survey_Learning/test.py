import numpy as np
import pandas as pd
from env.gaming_environment import GamingEnvironment
from agent.q_learning_agent import QLearningAgent

def test_agent(env, agent, episodes):
    reward_history = []
    for episode in range(episodes):
        state = env.reset()
        done = False
        rewards = 0
        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)
            state = next_state
            rewards += reward
        reward_history.append(rewards)
    return reward_history