import sys
import math
import extract
sys.setrecursionlimit(10**8)

c = 0
def knapsack(mW, weights, values, n):
    global c
    c += 1
    if(n == 0 or mW == 0):
        return [0, []]
    
    if(weights[n-1] > mW):
        return knapsack(mW, weights, values, n-1)
    
    set1 = knapsack(mW-weights[n-1], weights, values, n-1)
    set2 = knapsack(mW, weights, values, n-1)

    if(set1[0] + values[n-1] > set2[0]):
        set1[1].append(n-1)
        set1[0] += values[n-1]
        return set1
    else:
        return set2
    

def main():
    val, wt, W = extract.read_knapsack("low-dimensional/f1_l-d_kp_10_269")
    n = len(val)
    print(knapsack(W, wt, val, n))
    print("Total recursive steps: ", c)

if __name__ == "__main__":
    main()
