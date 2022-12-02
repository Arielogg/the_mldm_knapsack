from itertools import combinations
from extract import read_knapsack, read_optimal

def comb(a) :
    combinaison = sum([list(map(list, combinations(a, i))) for i in range(len(a) + 1)], [])
    sumvalues = []
    for i in combinaison :
        sumvalues.append(sum(i))

    #retourne une liste de toutes les combinaisons possibles
    #et une liste de la somme de chaque combinaison
    return combinaison,sumvalues

def Middle(Lv, Lw, W, optimal) :
    indices = []
    #On récupère les indices
    for i in range(len(Lw)):
        indices.append(i)

    #On divise notre ensemble d'éléments en deux ensembles d'éléments A et B
    ALw,ALv = [Lw[:2], Lv[:2]]
    BLw,BLv = [Lw[2:], Lv[2:]]
    #On divise nos indices en deux
    indices1 = indices[:2]
    indices2 = indices[2:]
    
    #calcule des poids et des valeurs de tous les sous-ensembles de chaque ensemble
    Acomweight,Asumweight = comb(ALw)
    Acombvalues,Asumvalues = comb(ALv)

    Bcomweight,Bsumweight = comb(BLw)
    Bcombvalues,Bsumvalues = comb(BLv)

    #On récupère la combinaisons de nos indices
    indicesA,s1 = comb(indices1)
    indicesB,s2 = comb(indices2)
    
  
    #On cherche à trouver le sous-ensemble de B de plus grande valeur 
    #de sorte que le poids combiné est inférieur à W
    max = 0
    SacV = []
    SacD = []
    for Aw,Av,Ai in zip(Asumweight, Asumvalues, indicesA) :
        for Bw,Bv,Bi in zip(Bsumweight, Bsumvalues, indicesB) :
            if (Bv+Av) > max and (Bw+Aw) <= W :
                max = Bv+Av
                maxindices = Ai + Bi

    taken = []
    for i in range(len(Lv)):
        if i in maxindices :
            taken.append(1)
        else :
            taken.append(0)

    print("The best value is : ",max,"Value optimal : ",optimal, "précision :",max/optimal*100,"%")
    print(taken)

    return max

# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(capacity_path)

# Calling the value greedy
values = list(map(int, values))
weights = list(map(int, weights))

knap = Middle(values, weights, capacity, optimal)

