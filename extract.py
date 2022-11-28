import numpy as np

def read_knapsack(filepath):
    items = np.loadtxt(filepath, delimiter=' ')
    values = items[1:, 0].astype(int)
    weights = items[1:, 1].astype(int)
    capacity = items[0, 1].astype(int)
    return values, weights, capacity

def read_optimal(filepath):
    optimal = np.loadtxt(filepath)
    return optimal