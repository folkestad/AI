from __future__ import print_function
import gym

env = gym.make('FrozenLake-v0')
episode = 1
goal_found = False

while not goal_found:
    state = env.reset()
    print("======== Episode {} ========".format(episode))
    while True:
        env.render()
        action = env.action_space.sample()
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
