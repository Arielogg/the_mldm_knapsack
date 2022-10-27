import numpy as np
from extract import read_knapsack, read_optimal
from os import listdir

def B_sort(sorted_one, other_one):
    """Standard implementation of the bubble sort algorithm adapted to
    the 0/1 knapsack problem.
    Parameters
    ----------
    sorted_one : array-like of shape (n_samples,). The feature which will drive the
                sorting algorithm in the knapsack (weights or values).
    other_one : array-like of shape (n_samples,). The other feature.
    Returns
    -------
    sorted_items : array-like. The sorted list of items.
    """

    # Iterator goes through every item of the list
    for i in range(len(sorted_one)):
        for j in range(0, len(sorted_one) - i - 1):

            # Range of the array is from 0 to len-i-1
            # Swap the elements if the element found
            # is greater than the adjacent element
            if sorted_one[j] > sorted_one[j + 1]:
                sorted_one[j], sorted_one[j + 1] = sorted_one[j + 1], sorted_one[j]
                other_one[j], other_one[j + 1] = other_one[j + 1], other_one[j]
    sorted_items = np.stack((sorted_one, other_one), axis=1)
    return sorted_items

def value_greedy(values, weights):
    #Arrange the items in a decreasing order of value
    sorted_items = B_sort(values, weights)
    sorted_items = np.flip(sorted_items, 0)

    return

# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
weights, values = read_knapsack(items_path)
capacity = read_optimal(capacity_path)

value_greedy(values, weights)