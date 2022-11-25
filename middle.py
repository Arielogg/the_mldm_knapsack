from itertools import combinations
from extract import read_knapsack, read_optimal

def comb(a) :
    combinaison = sum([list(map(list, combinations(a, i))) for i in range(len(a) + 1)], [])
    sumvalues = []
    for i in combinaison :
        sumvalues.append(sum(i))

    # Return a list of all the posible combination
    # and a list of the sum of the values for each combination
    return combinaison,sumvalues

def Middle(Lv, Lw, W, optimal) :
    #On divise notre ensemble d'éléments en deux ensembles d'éléments A et B
    # We devide our objects in 2 sets named A and B
    ALw,ALv = [Lw[:2], Lv[:2]]
    BLw,BLv = [Lw[2:], Lv[2:]]
    
    # Calculation of the weights and the values of all the subset of each set
    Acomweight,Asumweight = comb(ALw)
    Acombvalues,Asumvalues = comb(ALv)

    Bcomweight,Bsumweight = comb(BLw)
    Bcombvalues,Bsumvalues = comb(BLv)
  
    #On cherche à trouver le sous-ensemble de B de plus grande valeur 
    #de sorte que le poids combiné est inférieur à W
    # We are looking for the best subset of B in terms of value such as the combination 
    # the assossiated weights is inferior to the capacity of the bag
    max = 0
    SacV = []
    SacD = []
    for Aw,Av in zip(Asumweight, Asumvalues) :
        for Bw,Bv in zip(Bsumweight, Bsumvalues) :
            if (Bv+Av) > max and (Bw+Aw) <= W :
                max = Bv+Av

    print("The best value is : ",max,"Value optimal : ",optimal, "précision :",max/optimal*100,"%")
    return max

# Declaring item and capacity paths
items_path = 'low-dimensional/'+'f1_l-d_kp_10_269'
capacity_path = 'low-dimensional-optimum/'+'f1_l-d_kp_10_269'

# Reading the values
values, weights, capacity = read_knapsack(items_path)
optimal = read_optimal(capacity_path)

# Calling the greedy value
values = list(map(int, values))
weights = list(map(int, weights))

knap = Middle(values, weights, capacity, optimal)

