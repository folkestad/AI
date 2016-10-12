from __future__ import print_function
import gym
import sys
import random

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

env = gym.make('FrozenLake-v0')
episode = 1
epsilon = 0.1
Q = []
for i in range(16):
    Q.append([0.5, 1, 0.5, 0.5])
reward = 0

while reward != 1:
    state = env.reset()
    for i in range(100):
        env.render()
        action = epsilon_greedy_pick(state, epsilon)
        state, reward, done, info = env.step(action)
        if done and reward == 1:
            env.render()
            print ("You found a pot of gold in {} episodes.".format(episode))
            break
        if done:
            env.render()
            print ("You fell down a hole.")
            break
    episode += 1
