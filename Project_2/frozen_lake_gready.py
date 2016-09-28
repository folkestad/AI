from __future__ import print_function
import gym
import sys

env = gym.make('FrozenLake-v0')
sys.exit(0)
while True:
    observation = env.reset()
