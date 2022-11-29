import numpy as np
from extract import read_knapsack, read_optimal
from math import *


def m(i, j, M, Lw, Lv) :
    if i == 0 or j <= 0 :        
        M[i, j] = 0   
        return 0
    
    #m[i-1, j] n'a pas été calculé, il faut appeler la fonction m          
    if M[i-1, j] == -1 :
        M[i-1, j] = m(i-1, j, M, Lw, Lv)

    #l'article ne peut pas tenir dans le sac
    if Lw[i-1] > j :                            
        M[i, j] = M[i-1, j]   
    else :
    #m[i-1,Lw[i]] n'a pas été calculé, il faut appeler la fonction m
        if M[i-1, j-Lw[i-1]] == -1 :           
            M[i-1, j-Lw[i-1]] = m (i-1 , j-Lw[i-1], M, Lw, Lv)    
        M[i, j] = max(M[i-1, j], M[i-1, j-Lw[i-1]] + Lv[i-1]) 
    return M[i, j]


#La précision de votre algorithme dépendra de sigma !
def Poly(Sigma, Lv, Lw, W, optimal) :
    n = len(Lv)
    W = int(W)

    #La valeur maximale 
    maxVal = max(Lv) 

    #Facteur d'ajustement
    k = (maxVal * Sigma) / n
    print(k)

    #Initialisation de la matrie
    M = np.ones((n+1, W+1)).dot(-1) 

    #On arrondit toutes les valeurs de v sur le multiple de  k juste au dessus
    Lv2 = [ceil(i/k) for i in Lv]
    print (Lv2)

    #On applique l'approche dynamique avec notre nouvelle liste de valeur
    m(n, W, M, Lw, Lv2)

    precision = M[n,W]/optimal*100
    print("The best value is : ",M[n, W],"Value optimal : ",optimal, "précision :",precision,"%")
    
    return M[n, W]


################################################
#                    TEST                      #
################################################

# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(capacity_path)

# Calling the value greedy
values = list(map(int, values))
weights = list(map(int, weights))

knap = Poly(0.5, values, weights, capacity, optimal)