import random
import gym

class FooPool(list):
    space = {
        'gravity':      (9.8, 9.8),
        'masscart':     (0.5, 1.5),
        'masspole':     (0.05, 0.15),
        'mucart':       (0.0, 0.5),
        'mupole':       (0.0, 0.5),
        'force_mag':    (5.0, 15.0),
        'length':       (0.2, 1.2),
    }

    def __init__(self, size=0, seed=None):
        super(FooPool, self).__init__()
        random.seed(seed)

        for _ in range(size):
            env = gym.make('gym_foo:foo-v0')
            env.reset()

            for attr in self.space:
                a, b = self.space[attr]
                r = random.uniform(a, b)
                setattr(env, attr, r)

            self.append(env)


# Example
if __name__ == '__main__':
    pool = FooPool(10)
    n = 0
    for env in pool:
        print("env%d" % n)
        for attr in pool.space:
            print("\t%s: %f" % (attr, getattr(env, attr)))
        n += 1