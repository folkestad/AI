from __future__ import print_function
import gym
import sys
import random
import matplotlib.pyplot as plt

def epsilon_greedy_pick(state, epsilon): #picks direction with largest reward
    random_int = random.random()
    if random_int < epsilon:
        return random.randint(0, len(Q[state])-1)
    else:
        max_action = 0
        for action in range(len(Q[state])):
            if Q[state][max_action] < Q[state][action]:
                max_action = action
        return max_action

def max_Q(state):
    max_action = 0
    for action in range(len(Q[state])):
        if Q[state][max_action] < Q[state][action]:
            max_action = action
    return Q[state][max_action]

def Q_learning(state, action, next_state, next_action, reward):
    Q[state][action] = Q[state][action] + \
        learning_rate * \
            (reward + (disc_factor * Q[next_state][next_action]) - \
                Q[state][action])

env = gym.make('FrozenLake-v0')
epsilon = 0.1
learning_rate = 0.1
disc_factor = 0.99
Q = []
for i in range(16):
    Q.append([0.5, 1, 0.5, 0.5])

reward = 0
reward_list = []
episode = 1
while episode < 10000:
    state = env.reset()
    action = epsilon_greedy_pick(state, epsilon)
    for i in range(100):
        next_state, reward, done, info = env.step(action)
        next_action = epsilon_greedy_pick(next_state, epsilon)
        Q_learning(state, action, next_state, next_action, reward)
        action = next_action
        state = next_state
        if done:
            if reward == 1:
                reward_list.append(1)
            else:
                reward_list.append(0)
            break
    episode += 1

for state in Q:
    print (state)
env.render()
plt.plot(reward_list)
plt.xlabel('Episode number')
plt.ylabel('Reward')
plt.show()
