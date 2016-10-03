from __future__ import print_function
import gym
import random
import matplotlib.pyplot as plt

#====================== Helpers ====================================================================
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

def Q(state, action):
    return states[state][action]

def Q_learning(state, action, next_state, next_action, reward):
    states[state][action] = states[state][action] + \
        learning_rate * \
            (reward + (disc_factor * states[next_state][next_action]) - \
                states[state][action])

#====================== Algorithm ==================================================================

env = gym.make('Taxi-v1')
epsilon = 0.1
learning_rate = 0.1
disc_factor = 0.99
states = []
for i in range(500):
    states.append([0,0,0,0,0,0])

episode = 0
reward_list = []
while episode < 5000:
    tot_reward = 0
    state = env.reset()
    action = epsilon_greedy_pick(state, epsilon)
    for i in range(100):
        next_state, reward, done, info = env.step(action)
        next_action = epsilon_greedy_pick(next_state, epsilon)
        Q_learning(state, action, next_state, next_action, reward)
        action = next_action
        state = next_state
        tot_reward += reward
        if done:
            reward_list.append(tot_reward)
            break
    episode += 1

for state in states:
    print (state)
avg_reward = 0
counter = 0
for i in range(len(reward_list)-1, len(reward_list)-101, -1):
    avg_reward+=reward_list[i]
    counter+=1
print ("avg_reward of last 100 {} and length {}".format(avg_reward, counter))
env.render()
plt.figure(figsize=(18,10))
plt.plot(reward_list)
plt.xlabel('Episode number')
plt.ylabel('Reward')
plt.show()
