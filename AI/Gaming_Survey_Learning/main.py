import numpy as np
import pandas as pd
from env.gaming_environment import GamingEnvironment
from agent.q_learning_agent import QLearningAgent
from utils.visualize_learning import visualize_q_table, visualize_reward_history

def main():
    # Load data
    data = pd.read_csv('data/gaming_survey.csv')

    # Create environment
    env = GamingEnvironment(data)

    # Create agent
    agent = QLearningAgent(env)

    # Train agent
    reward_history = []
    q_table_data = []
    for episode in range(1000):
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

    # Visualize learning
    visualize_q_table(np.array(q_table_data)[-1])
    visualize_reward_history(reward_history)

if __name__ == '__main__':
    main()