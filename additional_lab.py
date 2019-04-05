#!/usr/bin/python
import lhw as distributions

DATA_SIZE = 10000
N = 10  # the degree of freedom


def count_observed_amount_in_parts(data: list, fractals: list):
    if len(data) < 1:
        raise ValueError("need more elements in data than zero")
    data.sort()
    amount_of_data = []
    index = 0
    for fractal in fractals:
        amount = 0
        while data[index] < fractal:
            amount += 1
            index += 1
        amount_of_data.append(amount)
    amount_of_data.append(len(data) - index - 1)
    return amount_of_data


def count_hi_square(observed: list, expected: list):
    hi_square = 0
    for i in range(len(expected)):
        hi_square += (observed[i] - expected[i]) ** 2 / (expected[i])
    return hi_square


def count_expected_amount_in_parts(fractals):
    return [1.0 / (len(fractals) + 1) * DATA_SIZE for i in range(len(fractals) + 1)]


def get_fractals(parts, n):
    # it doesn't have a formula, soб I counted it by the special table https://planetcalc.ru/5019/
    # TODO: remake to 20
    return [-1.81, -1.37, -1.09, -0.88, -0.7, -0.54, -0.4,
            -0.26, -0.13, 0, 0.13, 0.26, 0.4, 0.54, 0.7, 0.88, 1.09, 1.37, 1.81]


# pirson 467
def main():
    data = [distributions.rnstud(N) for i in range(DATA_SIZE)]
    fractals = get_fractals(20, N)
    expected = count_expected_amount_in_parts(fractals)
    observed = count_observed_amount_in_parts(data, fractals)
    print("hi square =", count_hi_square(observed, expected))


if __name__ == '__main__':
    main()
