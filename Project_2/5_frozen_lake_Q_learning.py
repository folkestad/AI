from __future__ import print_function
import gym
import sys
import random
import matplotlib.pyplot as plt

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

def max_Q(state):
    action_index = 0
    for action_i in range(len(Q_states[state])):
        if Q(state, action_index) < Q(state, action_i):
            action_index = action_i
    return Q_states[state][action_index]

def Q_learning(state, action, new_state, reward):
    states[state][action] = states[state][action] + \
        learning_rate * \
            (reward + (disc_factor * max_Q(new_state)) - \
                states[state][action])

def read():
    global Q_states
    # try:
    file = open('q_learning.txt', 'r')
    text = file.read()
    text_lines = text.split("\n")
    for i in range(len(text_lines)-1):
        text_lines[i] = text_lines[i].replace("[","")
        text_lines[i] = text_lines[i].replace("]","")
        action_values = text_lines[i].split(",")
        state = []
        for a_v in action_values:
            #print ("*",a_v,"*")
            state.append(float(a_v.replace(" ","")))
        Q_states.append(state)
    file.close()
    # except:
    #     print ("Could not read file.")
    #     sys.exit(0)

env = gym.make('FrozenLake-v0')
epsilon = 0.1
learning_rate = 0.1
disc_factor = 0.99

states = []
for i in range(16):
    states.append([0.5, 1, 0.5, 0.5])

Q_states = []
read()
for i in Q_states:
    print (i)

reward = 0
reward_list = []
episode = 1
while episode < 7000:
    state = env.reset()
    for i in range(100):
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

for state in states:
    print (state)
env.render()
plt.plot(reward_list)
plt.xlabel('Episode number')
plt.ylabel('Reward')
plt.show()
