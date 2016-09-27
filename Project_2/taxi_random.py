from __future__ import print_function
import gym

env = gym.make('Taxi-v1')
episode = 1
done = False
while not done:
    env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            env.render()
            print ("Drop-off complete in {} episode(s).".format(episode))
            break
    episode+=1
