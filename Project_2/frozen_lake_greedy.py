from __future__ import print_function
import gym
import sys

def Q(state, dir):
    if dir == 0:
        return states[state][0]
    elif dir == 1:
        return states[state][1]
    elif dir == 2:
        return states[state][2]
    elif dir == 3:
        return states[state][3]

def greedy_pick(state): #picks direction with largest reward
    index = 0
    for i in range(len(states[state])):
        if Q(state, index) < Q(state, i):
            index = i
    return index

env = gym.make('FrozenLake-v0')
episode = 1
states = []
for i in range(16):
    states.append([0.5, 1, 0.5, 0.5])
reward = 0

while reward != 1:
    state = env.reset()
    for i in range(100):
        env.render()
        action = greedy_pick(state)
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
