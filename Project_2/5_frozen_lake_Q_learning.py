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
        if Q_states[state][best_action] < Q_states[state][action]:
            best_action = action
    return Q_states[state][best_action]

def Q_learning(state, action, new_state, reward):
    Q[state][action] = Q[state][action] + \
        learning_rate * \
            (reward + (disc_factor * max_Q(new_state)) - \
                Q[state][action])

def read_states():
    Q_states = []
    try:
        file = open('q_learning.txt', 'r')
        text = file.read()
        text_lines = text.split("\n")
        for i in range(len(text_lines)-1):
            text_lines[i] = text_lines[i].replace("[","")
            text_lines[i] = text_lines[i].replace("]","")
            action_values = text_lines[i].split(",")
            state = []
            for a_v in action_values:
                state.append(float(a_v.replace(" ","")))
            Q_states.append(state)
        file.close()
        return Q_states
    except:
        print ("Could not read file.")
        sys.exit(0)

env = gym.make('FrozenLake-v0')
epsilon = 0.1
learning_rate = 0.1
disc_factor = 0.99

Q = []
for i in range(16):
    Q.append([0.5, 1, 0.5, 0.5])

Q_states = read_states()
for state in Q_states:
    print (state)

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

for state in Q:
    print (state)
env.render()
plt.plot(reward_list)
plt.xlabel('Episode number')
plt.ylabel('Reward')
plt.show()
