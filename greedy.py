'''
GUERRA ADAMES Ariel
Script containing TBD
'''

import numpy as np
from extract import read_knapsack, read_optimal
import problem_generator as pg

def b_sort(sorted_one, other_one):
    """Standard implementation of the bubble sort algorithm adapted to
    the 0/1 knapsack problem.
    Parameters
    ----------
    sorted_one : array-like of shape (n_samples,). The feature which
                will drive the sorting algorithm in the knapsack
                (weights or values).
    other_one : array-like of shape (n_samples,). The other feature.
    Returns
    -------
    sorted_items : array-like. The sorted list of items.
    """
    ind = np.array(np.arange(len(sorted_one)))  # Creates registry of indexes
    for i in range(len(sorted_one)):     # Iterator goes through every item of the list
        for j in range(0, len(sorted_one) - i - 1):         # Range of the array is from 0 to len-i-1
            if sorted_one[j] > sorted_one[j + 1]:  # Swap the elements if the element found is greater than the prev.
                sorted_one[j], sorted_one[j + 1] = sorted_one[j + 1], sorted_one[j]
                other_one[j], other_one[j + 1] = other_one[j + 1], other_one[j]
                ind[j], ind[j + 1] = ind[j + 1], ind[j]
    sorted_items = np.stack((sorted_one, other_one, ind), axis=1)
    return sorted_items


def value_greedy(vals, weigh, cap:int, opt:int = 0):
    """Implementation of a value-oriented greedy algorithm to solve
    the 0/1 knapsack problem.
    Parameters
    ----------
    vals : array-like of shape (n_samples,). List of the monetary value
            of the items to be arranged in the knapsack.
    weigh : array-like of shape (n_samples,). list of corresponding weights
            of the items to be arranged in the knapsack.
    cap:    integer. Capacity of the knapsack.
    opt:    integer. Optimal value of the items to be arranged.
    Returns
    -------
    knap_sol : array-like. The one-hot coded solution of the chosen items.
    """

    ### VALUE-WISE GREEDY ####
    in_sack_w, in_sack_v = 0, 0  # Empty weight and value counters
    knap_sol = np.empty(len(vals))  # Empty solution vector
    sorted_items = np.flipud(b_sort(vals, weigh))  # Sorts the items value-wise, descending order.
    for i in range(len(sorted_items)):  # Iterates through every item
        if in_sack_w+sorted_items[i,1] <= cap:  # Check if the weight limit can be reached in this iter.
            in_sack_w += sorted_items[i,1]  # Sums weight
            in_sack_v += sorted_items[i,0]  # Sums value
            knap_sol[int(sorted_items[i,2])] = 1  # Found a value for the solution. Added.
        else:
            knap_sol[int(sorted_items[i,2])] = 0  # Weight limit reached. Nothing changed
    wasted_value = opt - in_sack_v

    ### PRINTING SOLUTIONS ###
    print("VALUE-ORIENTED GREEDY ALGORITHM RESULTS: ")
    print("Was able to fit %d€ worth of stuff in the knapsack. "
          "The optimal value was %d€"%(in_sack_v, opt))
    print("Was able to fit %d kg. The knapsack had a capacity of "
          "%d kg"%(in_sack_w, capacity))
    print("Unprofited value: %d€"%(wasted_value))
    print("One-hot coded solution: "+str(knap_sol))
    print()
    return knap_sol


def weight_greedy(vals, weigh, cap:int, opt:int = 0):
    """Implementation of a weight-oriented greedy algorithm to solve
    the 0/1 knapsack problem.
    Parameters
    ----------
    vals : array-like of shape (n_samples,). List of the monetary value
            of the items to be arranged in the knapsack.
    weigh : array-like of shape (n_samples,). list of corresponding weights
            of the items to be arranged in the knapsack.
    cap:    integer. Capacity of the knapsack.
    opt:    integer. Optimal value of the items to be arranged.
    Returns
    -------
    knap_sol : array-like. The one-hot coded solution of the chosen items.
    """
    ### WEIGHT-WISE GREEDY ####
    in_sack_w, in_sack_v = 0, 0 # Empty weight and value counters
    knap_sol = np.empty(len(vals))  # Empty solution vector
    sorted_items = b_sort(weigh, vals)  # Sorts the items weight-wise, ascending order.
    for i in range(len(sorted_items)):  # Iterates through every item
        if in_sack_w+sorted_items[i,0] <= cap:  # Check if the weight limit can be reached in this iter.
            in_sack_w += sorted_items[i,0]  # Sums weight
            in_sack_v += sorted_items[i,1]  # Sums value
            knap_sol[int(sorted_items[i,2])] = 1  # Found a value for the solution. Added.
        else:
            knap_sol[int(sorted_items[i,2])] = 0  # Weight limit reached. Nothing changed
    wasted_value = opt - in_sack_v

    #### PRINTING SOLUTIONS ###
    print("WEIGHT-ORIENTED GREEDY ALGORITHM RESULTS: ")
    print("Was able to fit %d€ worth of stuff in the knapsack. "
          "The optimal value was %d€"%(in_sack_v, opt))
    print("Was able to fit %d kg. The knapsack had a capacity of "
          "%d kg"%(in_sack_w, capacity))
    print("Unprofited value: %d€"%(wasted_value))
    print("One-hot coded solution: "+str(knap_sol))
    print()
    return knap_sol

def fractional_greedy(vals, weigh, cap:int, opt:int = 0):
    """Implementation of a weight-oriented greedy algorithm to solve
    the 0/1 knapsack problem.
    Parameters
    ----------
    vals : array-like of shape (n_samples,). List of the monetary value
            of the items to be arranged in the knapsack.
    weigh : array-like of shape (n_samples,). list of corresponding weights
            of the items to be arranged in the knapsack.
    cap:    integer. Capacity of the knapsack.
    opt:    integer. Optimal value of the items to be arranged.
    Returns
    -------
    knap_sol : array-like. The one-hot coded solution of the chosen items.
    """
    ### RATIO-WISE GREEDY ####
    in_sack_w, in_sack_v = 0, 0  # Empty weight and value counters
    knap_sol = np.empty(len(vals))  # Empty solution vector
    val_wei_ratio = vals/weigh  # Calculates value-weight ratios of each item
    sorted_items = np.flipud(b_sort(val_wei_ratio, weights))  # Sorts the items ratio-wise, descending order.
    for i in range(len(sorted_items)):  # Iterates through every item
        if in_sack_w+sorted_items[i,1] <= cap:  # Check if the weight limit can be reached in this iter.
            in_sack_w += sorted_items[i,1]  # Sums weight
            knap_sol[int(sorted_items[i,2])] = 1  # Found a value for the solution. Added.
        else:
            knap_sol[int(sorted_items[i,2])] = 0  # Weight limit reached. Nothing changed
    # wasted_value = opt - in_sack_v

    #### PRINTING SOLUTIONS ###
    print("FRACTIONAL GREEDY ALGORITHM RESULTS: ")
    # print("Was able to fit %d€ worth of stuff in the knapsack. "
    #       "The optimal value was %d€"%(in_sack_v, opt))
    print("Was able to fit %d kg. The knapsack had a capacity of "
          "%d kg"%(in_sack_w, capacity))
    # print("Unprofited value: %d€"%(wasted_value))
    print("One-hot coded solution: "+str(knap_sol))
    print()
    return knap_sol

# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(capacity_path)

# Calling the value greedy
knap = value_greedy(values, weights, capacity, optimal)
knap2 = weight_greedy(values, weights, capacity, optimal)
ratioknap = fractional_greedy(values, weights, capacity, optimal)