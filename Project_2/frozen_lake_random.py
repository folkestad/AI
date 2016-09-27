from __future__ import print_function
import gym

env = gym.make('FrozenLake-v0')
episode = 1
reward = 0
while reward != 1:
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done and reward == 1:
            env.render()
            print ("You found a pot of gold in {} episodes.".format(episode))
            break
        if done:
            env.render()
            print ("You fell down a hole.")
            break
    episode += 1
