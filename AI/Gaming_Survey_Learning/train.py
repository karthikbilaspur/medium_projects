import numpy as np
import pandas as pd
from env.gaming_environment import GamingEnvironment
from agent.q_learning_agent import QLearningAgent

def train_agent(env, agent, episodes):
    reward_history = []
    q_table_data = []
    for episode in range(episodes):
        state = env.reset()
        done = False
        rewards = 0
        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update_q_table(state, action, reward, next_state)
            state = next_state
            rewards += reward
        reward_history.append(rewards)
        q_table_data.append(agent.q_table.copy())
    return reward_history, q_table_data