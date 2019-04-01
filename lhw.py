import math as mt
from scipy.stats import uniform


# continious uniform distribution
def rnuni(a, b):
    return (b - a) * uniform.rvs() + a


# continious normal distribution : Box-Muller method
secondX = 0
isReady = False


def rnnorm1(mu, sigma):
    global isReady
    global secondX

    if (isReady):
        isReady = False
        return mu + sigma * secondX
    else:
        isReady = True
        u1, u2 = uniform.rvs(size=2)
        firstX = (-2 * mt.log(u2)) ** (1 / 2) * mt.cos(2 * mt.pi * u1)
        secondX = (-2 * mt.log(u2)) ** (1 / 2) * mt.sin(2 * mt.pi * u1)
        return mu + sigma * firstX


# continious normal distribution : limit central teorem
def rnnorm2(mu, sigma, N):
    R = sum([uniform.rvs() for i in range(N)])
    return mu + sigma * (R - 0.5 * N) * 6 / (3 * N) ** (1 / 2)


# continious exponential distribution
def rnexp(betta):
    return -betta * mt.log(uniform.rvs())


# continious chiSquare distribution
def rnchsq(N):
    return sum([rnnorm1(0, 1.) ** 2 for i in range(N)])


# continious central Student distribution
def rnstud(N):
    return rnnorm1(0, 1.) / (rnchsq(N) / float(N)) ** (1 / 2)
