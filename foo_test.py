# import gym
# env = gym.make('gym_foo:foo-v0')
# env.reset()
# env.length = 0.2
# env.mucart = 0.7
# env.mupole = 0.7
# action = 0
# for _ in range(400):
#     action = 1 - action
#     env.render()
#     env.step(0) # take a random action
# env.close()

def test_env(env):
    action = 0
    for _ in range(400):
        action = 1 - action
        env.render()
        env.step(action) # take a random action
    env.close()

import gym
from gym_foo import FooPool

pool = FooPool(3)
n = 0
for env in pool:
    print("env%d" % n)
    for attr in pool.space:
        print("\t%s: %f" % (attr, getattr(env, attr)))
    n += 1
    test_env(env)
