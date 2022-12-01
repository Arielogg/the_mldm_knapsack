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
    
def accuracy(sol):
    optimal = extract.read_optimal("low-dimensional-optimum/f2_l-d_kp_20_878")
    acc = sol[0]/optimal * 100
    return acc

def onehot(sol, val, wt, W):
    n = len(val)
    onehot = [0]*n
    for i in range(len(sol[1])):
        onehot[sol[1][i]] = 1
    return onehot

def main():
    val, wt, W = extract.read_knapsack("low-dimensional/f2_l-d_kp_20_878")
    n = len(val)
    sol = knapsack(W, wt, val, n)
    print("accuracy: ", accuracy(sol))
    print(sol)
    print("one-hot-coded solution: ", onehot(sol, val, wt, W))
    print("Total recursive steps: ", c)

if __name__ == "__main__":
    main()
