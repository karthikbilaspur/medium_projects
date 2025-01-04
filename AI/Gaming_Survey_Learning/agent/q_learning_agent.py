import numpy as np

class QLearningAgent:
    def __init__(self, env, exploration_rate=0.1, learning_rate=0.1):
        self.env = env
        self.q_table = np.zeros((env.state_space.n, env.action_space.n))
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate

    def get_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        self.q_table[state, action] += self.learning_rate * (reward + 0.9 * np.max(self.q_table[next_state]) - self.q_table[state, action])
