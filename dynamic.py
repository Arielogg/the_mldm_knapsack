'''
MOUDJAHED Mohamed
W = the capacity of the bag
'''
import numpy as np
from extract import read_knapsack, read_optimal

'''

Dynamic program algorithm that we have seen in class

Brief explanation :
- The values of the matrix are initialized to 0
- There are two ways to fill the matrix with a value :
  i) If the weight Lw[i] >w : We can't add anything else, we take back the upper value (M[i-1, w])
  ii) Else : The chosen value wil be the maximum between the upper one M[i-1, w] et M[i-1, w - Lw[i]] + Lv[i]
      Why "M[i-1, w - Lw[i]] + Lv[i]" ? 
          -> It is the value with the highest capacity that has been calculated + the value we add
 '''

def Dynamic(Lv, Lw, W, optimal) :
    n = len(Lv)
    W = int(W)
    M = np.zeros((n+1, W+1))
    for i in range(1, n+1) :
        for w in range(1, W+1):
            if Lw[i-1] > w :
                M[i, w] = M[i-1, w]
            else :
                M[i, w] = max(M[i-1, w], Lv[i-1] + M[i-1, w-Lw[i-1]])
    print("The best value is : ",M[n, W],"Value optimal : ",optimal, "précision :",M[n,W]/optimal*100,"%")
    return M[n, W]

'''
Top Down version - this version is more optimized and reduces the number of call, by calculating only if necessary
'''

def m(i, j, M, Lw, Lv) :
    if i == 0 or j <= 0 :        
        M[i, j] = 0   
        return 0

    if M[i-1, j] == -1 :#m[i-1, j] n'a pas été calculé, il faut appeler la fonction m          
        M[i-1, j] = m(i-1, j, M, Lw, Lv)

    if Lw[i-1] > j :   #l'article ne peut pas tenir dans le sac                          
        M[i, j] = M[i-1, j]   
    else :
        if M[i-1, j-Lw[i-1]] == -1 : #m[i-1,Lw[i]] n'a pas été calculé, il faut appeler la fonction m          
            M[i-1, j-Lw[i-1]] = m (i-1 , j-Lw[i-1], M, Lw, Lv)    
        M[i, j] = max(M[i-1, j], M[i-1, j-Lw[i-1]] + Lv[i-1]) 
    return M[i, j]

def TopDown(Lv, Lw, W, optimal) :
    n = len(Lv)
    W = int(W)
    M = np.ones((n+1, W+1)).dot(-1)
    m(n, W, M, Lw, Lv)
    print("The best value is : ",M[n, W],"Value optimal : ",optimal, "précision :",M[n,W]/optimal*100,"%")
    return (M[n, W])

# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(capacity_path)

# Calling the value greedy
values = list(map(int, values))
weights = list(map(int, weights))

knap = Dynamic(values, weights, capacity, optimal)
knap2 = TopDown(values, weights, capacity, optimal)
