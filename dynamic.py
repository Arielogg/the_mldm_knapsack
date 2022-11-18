'''
MOUDJAHED Mohamed
Capacité du sac = W
'''
import numpy as np

Lw = [3, 4, 7]
Lv = [1, 2, 10]
W = 10

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

def Dynamic(W) :
    n = len(Lv)
    M = np.zeros((n+1, W+1))
    for i in range(1, len(Lv)+1) :
        for w in range(1, W+1):
            if Lw[i-1] > w :
                M[i, w] = M[i-1, w]
            else :
                M[i, w] = max(M[i-1, w], Lv[i-1] + M[i-1, w-Lw[i-1]])
    return M[n, W]

'''
Version Top Down plus optimisée réduisant le nombre d'appel, en calculant les poids 
seulement si nécessaire.
'''

def m(i, j, M) :
    if i == 0 or j <= 0 :        
        M[i, j] = 0   
        return 0

    if M[i-1, j] == -1 :#m[i-1, j] n'a pas été calculé, il faut appeler la fonction m          
        M[i-1, j] = m(i-1, j, M)

    if Lw[i-1] > j :   #l'article ne peut pas tenir dans le sac                          
        M[i, j] = M[i-1, j]   
    else :
        if M[i-1, j-Lw[i-1]] == -1 : #m[i-1,Lw[i]] n'a pas été calculé, il faut appeler la fonction m          
            M[i-1, j-Lw[i-1]] = m (i-1 , j-Lw[i-1], M)    
        M[i, j] = max(M[i-1, j], M[i-1, j-Lw[i-1]] + Lv[i-1]) 
    return M[i, j]

def TopDown(W) :
    n = len(Lv)
    M = np.ones((n+1, W+1)).dot(-1)
    m(n, W, M)
    return (M[n, W])


'''
TEST
'''
print("Test matrice dynamique :\n")
print(Dynamic(10))
print("\n")
print("Test matrice dynamique TopDown :\n")
print(TopDown(10))




