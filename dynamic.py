'''
MOUDJAHED Mohamed
Capacité du sac = W
'''
import numpy as np
from extract import read_knapsack, read_optimal

'''
Programmation dynamique
algorithme vu en cours

Explication brève :
- Les valeurs de la matrice sont initialisées à 0
- Pour remplir une valeur dans la matrice il y'a deux situations :
  i) Le poid Lw[i] > w : On ne peut rien ajouter de plus, la valeur du dessus est reprise (M[i-1, w])
  ii) Sinon : La valeur sera le maximum entre celle du dessus (M[i-1, w]) et M[i-1, w - Lw[i]] + Lv[i]
      Pourquoi "M[i-1, w - Lw[i]] + Lv[i]" ? 
        -> Il s'agit de la valeur à la capacité maximale déjà calculée + la valeur à ajouter
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
Version Top Down plus optimisée réduisant le nombre d'appel, en calculant les poids 
seulement si nécessaire.
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
