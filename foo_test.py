import gym
env = gym.make('gym_foo:foo-v0')
env.reset()
env.length = 0.2
env.mucart = 0.7
env.mupole = 0.7
action = 0
for _ in range(400):
    action = 1 - action
    env.render()
    env.step(0) # take a random action
env.close()