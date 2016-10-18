from __future__ import print_function
import gym

env = gym.make('Taxi-v1')
episode = 1
done = False
while not done:
    state = env.reset()
    print("======== Episode {} ========".format(episode))
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        if done:
            env.render()
            print ("Drop-off complete in {} episode(s).".format(episode))
            break
    episode+=1
