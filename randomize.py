import random
import numpy as np
import time
from extract import read_knapsack, read_optimal

#param : nombre d'itération, faire deux listes, une autre listes avec n random par exemple le premier ->4 k[4]->1
# boucle n -> qui va faire le truc random

def randomize(weight,values,capacity,iter=10000) :
    """Naïve random implementation of the 0/1 knapsack problem.
    Parameters
    ----------
    values : array-like of shape (n_samples,). List of values of items
                to be put in the knapsack.
    weight : array-like of shape (n_samples,). List of weights of items
                to be put in the knapsack.
    capacity : maximum weight possibly held by the knapsack.
    iter : int. number of random iterations to test.
    Returns
    -------
    bestChoice : array-like of shape (n_samples,). One-hot coded list of
                    selected items
    bestweight : int. Total weight of selected items.
    bestval : int. Total value of selected items.
    """
    # creation de la variable qui renverra le meilleur choix
    bestChoice = []
    bestValue, bestweight = 0, 0

    for tour in range(iter):
        ran = random.sample(range(len(values)), len(values))  # liste de nombre aléatoire de taille n,corresponds a indice du tableau
        # creation des variables temporaire de poids,valeur
        tempweight, tempvalue = 0, 0
        # initialisation de notre liste a, servira de liste temporaire qui conservera la meilleur chemin
        a = np.zeros(len(values))

        #boucle qui va parcourir tout les elem de ma liste ran
        for i in range(0,len(values)-1) :
            #j sera égale a l'indice renvoyer dans la liste de random
            j=ran[i]
            tempweight = tempweight + weight[j]
            if(tempweight<capacity) :
                #on le met dans le sac
                a[j]=1
                #on ajoute la valeur de j
                tempvalue=tempvalue+values[j]

            else :
                if(bestValue< tempvalue):
                    #on soustrait le poids mis en trop et on l'attribue a notre poids final
                    bestWeight = tempweight - weight[j]
                    #on attribue la valeur finale
                    bestValue = tempvalue
                    #bestChoice deviens a
                    bestChoice=a

    # print("val : " + str(bestValue))
    # print("weight : " + str(bestWeight))
    # print("solution vect : " + str(bestChoice))
    return bestChoice, bestWeight, bestValue


# Declaring item and capacity paths
items_path = 'low-dimensional/' + 'f1_l-d_kp_10_269'
optimal_path = 'low-dimensional-optimum/' + 'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(optimal_path)

tic = time.time()
solution, bestweight, bestval = randomize(weights, values, capacity, 10000)
toc = time.time()-tic
toc = toc*1000

print("Execution time: %s miliseconds" % toc)
print("Solution vector: \n" + str(solution))
print("Value of the objects in the knapsack: %d €" % bestval)
print("Optimal value: %d €" % optimal)