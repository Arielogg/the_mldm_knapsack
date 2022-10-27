import numpy as np

def read_knapsack(filepath):
    items = np.loadtxt(filepath, delimiter=' ')
    values = items[1:, 0]
    weights = items[1:, 1]
    capacity = items[0, 1]
    return values, weights, capacity

def read_optimal(filepath):
    optimal = np.loadtxt(filepath)
    return optimal