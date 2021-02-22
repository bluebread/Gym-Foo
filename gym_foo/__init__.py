from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_foo.envs:FooEnv',
)

from gym_foo.envs.foo_env import FooEnv
from gym_foo.foo_pool import FooPool