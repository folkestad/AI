from __future__ import print_function
import gym
import sys
import random
import matplotlib.pyplot as plot

def Q(state, action):
    if action == 0:
        return states[state][0]
    elif action == 1:
        return states[state][1]
    elif action == 2:
        return states[state][2]
    elif action == 3:
        return states[state][3]

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

def max_Q(state):
    action_index = 0
    for action_i in range(len(states[state])):
        if Q(state, action_index) < Q(state, action_i):
            action_index = action_i
    return action_index

def Q_learning(state, action, new_state, reward):
    states[state][action] = states[state][action]+ \
        learning_rate*(reward+disc_factor*max_Q(new_state) \
            -states[state][action])

env = gym.make('FrozenLake-v0')
episode = 1
epsilon = 0.1
learning_rate = 0.1
disc_factor = 0.99
states = []
for i in range(16):
    states.append([0.5, 1, 0.5, 0.5])
reward = 0

while reward != 1:
    state = env.reset()
    for i in range(100):
        env.render()
        action = epsilon_greedy_pick(state, epsilon)
        new_state, reward, done, info = env.step(action)
        Q_learning(state, action, new_state, reward)
        state = new_state
        if done and reward == 1:
            env.render()
            print ("You found a pot of gold in {} episodes.".format(episode))
            for state in states:
                print (state)
            print ()
            break
        if done:
            env.render()
            print ("You fell down a hole.")
            break
    episode += 1
