from __future__ import print_function
import gym
import sys
import random

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

env = gym.make('FrozenLake-v0')
epsilon = 0.1
Q = []
for i in range(16):
    Q.append([0.5, 1, 0.5, 0.5])
reward = 0

goal_found = False
episode = 1
while not goal_found:
    state = env.reset()
    while True:
        env.render()
        action = epsilon_greedy_pick(state, epsilon)
        state, reward, done, info = env.step(action)
        if done and reward == 1:
            env.render()
            print ("You found a pot of gold in {} episodes.".format(episode))
            goal_found = True
            break
        if done:
            env.render()
            print ("You fell down a hole.")
            break
    episode += 1
