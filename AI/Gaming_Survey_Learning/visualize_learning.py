import matplotlib.pyplot as plt
import numpy as np

def visualize_reward_history(reward_history):
    plt.figure(figsize=(10, 6))
    plt.plot(reward_history)
    plt.title('Reward History')
    plt.xlabel('Episodes')
    plt.ylabel('Reward')
    plt.show()

def visualize_q_table(q_table_data):
    plt.figure(figsize=(10, 10))
    plt.imshow(q_table_data, cmap='hot', interpolation='nearest')
    plt.title('Q-table Values')
    plt.xlabel('Actions')
    plt.ylabel('States')
    plt.show()