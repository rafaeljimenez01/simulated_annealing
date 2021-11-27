import csv as csv
import numpy as np
import more_itertools as mit
import random
from copy import deepcopy
import math

np.random.seed(15)

iterations = 100000

N = 128
T = 3356

k = 0


def path_cost(path, N, dist):
    c = 0

    for i in range(0, N - 1):
        x1 = path[i]
        x2 = path[i + 1]

        c = c + dist[x1][x2]

    return c


def neighbor(path):
    pick_1 = random.randint(0, N - 1)
    pick_2 = random.randint(0, N - 1)

    path[pick_1], path[pick_2] = path[pick_2], path[pick_1]

    return path


def read_csv(file_name):
    file = open(file_name)
    csvreader = csv.reader(file)
    matrix_2d = []

    for row in csvreader:
        current = []
        for element in row:
            current.append(int(element))

        matrix_2d.append(current)

    return matrix_2d


if __name__ == '__main__':
    print("TEST")
    distances = read_csv("cities_128.csv")

    iterable = range(N)
    current = list(np.random.permutation(iterable))

    print(current)

    current_cost = path_cost(current, N, distances)
    print('Cost of starting path: ', current_cost)

    while k < iterations:
        new = neighbor(deepcopy(current))
        new_cost = path_cost(new, N, distances)

        if new_cost < current_cost:
            current = deepcopy(new)
            current_cost = new_cost
        else:
            # Compute the delta in energy
            delta = new_cost - current_cost
            if delta > 0:
                if random.random() < math.exp(-delta / T):
                    current = deepcopy(new)
                    current_cost = new_cost
            else:
                current_cost = new_cost

        print(k, current_cost, new_cost, T)
        T = T * 0.9999
        k += 1

    print('Cost of final path: ', current_cost)
