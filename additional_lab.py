#!/usr/bin/python
import lhw as distributions

DATA_SIZE = 10000


# pirson 467

def main():
    data = [distributions.rnstud(10) for i in range(DATA_SIZE)]
    print(sum(data)/len(data))


if __name__ == '__main__':
    main()
