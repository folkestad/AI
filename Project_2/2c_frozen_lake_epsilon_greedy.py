from __future__ import print_function
import gym
import sys
import random

def Q(state, action):
    return states[state][action]

def epsilon_greedy_pick(state, epsilon): #picks direction with largest reward
    random_int = random.random()
    if random_int < epsilon:
        return random.randint(0, len(states[state])-1)
    else:
        action_index = 0
        for action_i in range(len(states[state])):
            if Q(state, action_index) < Q(state, action_i):
                action_index = action_i
        return action_index

env = gym.make('FrozenLake-v0')
episode = 1
epsilon = 0.2
states = []
for i in range(16):
    states.append([0.5, 1, 0.5, 0.5])
reward = 0

while reward != 1:
    state = env.reset()
    for i in range(100):
        env.render()
        action = epsilon_greedy_pick(state, epsilon)
        #print ("{} {} {}".format(action, env.action_space, state))
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
