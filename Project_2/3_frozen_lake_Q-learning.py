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
        best_action = 0
        for action in range(len(Q[state])):
            if Q[state][best_action] < Q[state][action]:
                best_action = action
        return best_action

def max_Q(state):
    best_action = 0
    for action in range(len(Q[state])):
        if Q[state][best_action] < Q[state][action]:
            best_action = action
    return Q[state][best_action]

def Q_learning(state, action, new_state, reward):
    Q[state][action] = Q[state][action] + \
        learning_rate * \
            (reward + (disc_factor * max_Q(new_state)) - \
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
while episode < 20000:
    state = env.reset()
    while True:
        action = epsilon_greedy_pick(state, epsilon)
        new_state, reward, done, info = env.step(action)
        Q_learning(state, action, new_state, reward)
        state = new_state
        if done:
            if reward == 1:
                reward_list.append(1)
            else:
                reward_list.append(0)
            break
    episode += 1
    if episode%500 == 0:
        epsilon-=0.005

for state in Q:
    print (state)
file = open('q_learning.txt','w')
for state in Q:
    file.write(str(state)+"\n")
file.close()
env.render()
plt.figure(figsize=(18,10))
plt.plot(reward_list)
plt.xlabel('Episode number')
plt.ylabel('Reward')
plt.show()
