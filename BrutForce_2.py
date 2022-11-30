from itertools import combinations
from extract import read_knapsack, read_optimal


#retourne une liste de toutes sommes des combinaisons
def sumcomb(a) :
    combinaison = sum([list(map(list, combinations(a, i))) for i in range(len(a)+1)], [])
    sumvalues = []
    for i in combinaison :
        sumvalues.append(sum(i))

    
    return sumvalues

#retourne une liste de toutes les combinaisons possibles
def comb(a) :
    combinaison = sum([list(map(list, combinations(a, i))) for i in range(len(a)+1)], [])
    
    return combinaison

#retourne 1 si les listes a et b ont une valeur commune sinon 0
def same(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return 1
    else:
        return 0


def BrutForce_MKP(Lv, Lw, W1, W2, optimal) :
    #Liste des indices des objets
    O = []
    for i in Lv :
        O.append(i)
 
    #calcule des poids et des valeurs 
    sumweight = sumcomb(Lw)
    sumvalues = sumcomb(Lv)
    
    #combinaison des indices
    combobjet = comb(O)
    
    #On récupère toutes les combinaisons possibles
    #((sumweight1, sumweight2),(sumvalues1, sumvalues2))
    #En prenant bien en compte qu'on ne peut pas mettre un objet dans deux sacs
    #Puis on prend la meilleur combinaison possible
    Valmax = 0
    for sw1,sv1,co1 in zip(sumweight, sumvalues, combobjet) :
       for sw2,sv2,co2 in zip(sumweight, sumvalues, combobjet) :
           if(same(co1,co2)==0) :
                if sw1 <= W1 and sw2 <= W2 and sv1+sv2 > Valmax :
                    Valmax = sv1+sv2

    print(Valmax)
    return Valmax



# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(capacity_path)

# Calling the value greedy
values = list(map(int, values))
weights = list(map(int, weights))

print(optimal)
knap = BrutForce_MKP(values, weights, 30, capacity, optimal)
