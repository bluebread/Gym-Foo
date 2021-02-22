import gym
env = gym.make('gym_foo:foo-v0')
env.reset()
env.mucart = 1.0
env.mupole = 1.0
action = 0
for _ in range(400):
    action = 1 - action
    env.render()
    env.step(0) # take a random action
env.close()