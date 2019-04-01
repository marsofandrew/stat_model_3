import numpy as np
import matplotlib.pyplot as plt


def plotDensity(values):
    plt.hist(values, density=True, histtype='stepfilled')
    plt.title("Empirical density")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    pass


def plotProbability(unsorted_values):
    values = sorted(unsorted_values)
    uniq_x = sorted(set(unsorted_values))
    fx = list()

    freq = 0
    out_i = 0
    for i in range(len(values)):
        if (i != 0):
            if (values[i - 1] == values[i]):
                continue

        count = 0
        for k in range(i, len(values)):
            if (values[i] == values[k]):
                count += 1
            else:
                break

        freq += count / len(values)
        fx.append(freq)
        out_i += 1

    plt.plot(uniq_x, fx)
    plt.title("Empirical probability")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.show()
    pass
