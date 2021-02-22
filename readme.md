# Gym Foo

This is based on CartPole-v0 in OpenAI Gym. I am lazy to give it a better name.

Installation:

    $ cd /gym-foo/..
    $ pip install -e gym-foo

How to get the enviroment:

```python
import gym
env = gym.make('gym_foo:foo-v0')
```

How to use FooPool to get diverse enviroments:

```python
from gym_foo import FooPool

pool = FooPool(10) # size 10
for env in pool:
    # Do something in a new enviroment ...
```

Default sampling interval of arguments of CartPole simulator:
|   Argument    |   Interval    |       Description           |
| ------------- | ------------- | --------------------------- | 
|   gravity     |   (9.8, 9.8)  |   gravity constant          |
|   masscart    |   (0.5, 1.5)  |   mass of cart              |
|   masspole    |   (0.05, 0.15)|   mass of pole              |
|   mucart      |   (0.0, 0.5)  |   friction of cart moving   |
|   mupole      |   (0.0, 0.5)  |   friction of pole rotating |
|   force_mag   |   (5.0, 15.0) |   pushing force             |
|   length      |   (0.2, 1.2)  |   length of pole            |
