import numpy as np

def read_knapsack(filepath):
    items = np.loadtxt(filepath, delimiter=' ')
    weights = items[:, 0]
    values = items[:, 1]
    return weights, values, capacity

def read_optimal(filepath):
    optimal = np.loadtxt(filepath)
    return optimal