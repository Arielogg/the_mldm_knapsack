from itertools import combinations

Lw = [3, 4, 7]
Lv = [1, 2, 10]
W = 10

def comb(a) :
    combinaison = sum([list(map(list, combinations(a, i))) for i in range(len(a) + 1)], [])
    sumvalues = []
    for i in combinaison :
        sumvalues.append(sum(i))

    #retourne une liste de toutes les combinaisons possibles
    #et une liste de la somme de chaque combinaison
    return combinaison,sumvalues

def cal() :
    #On divise notre ensemble d'éléments en deux ensembles d'éléments A et B
    ALw,ALv = [Lw[:2], Lv[:2]]
    BLw,BLv = [Lw[2:], Lv[2:]]
    
    #calcule des poids et des valeurs de tous les sous-ensembles de chaque ensemble
    Acomweight,Asumweight = comb(ALw)
    Acombvalues,Asumvalues = comb(ALv)

    Bcomweight,Bsumweight = comb(BLw)
    Bcombvalues,Bsumvalues = comb(BLv)
  
    #On cherche à trouver le sous-ensemble de B de plus grande valeur 
    #de sorte que le poids combiné est inférieur à W
    max = 0
    SacV = []
    SacD = []
    for Aw,Av in zip(Asumweight, Asumvalues) :
        for Bw,Bv in zip(Bsumweight, Bsumvalues) :
            if (Bv+Av) > max and (Bw+Aw) <= W :
                max = Bv+Av

    return max


print(cal())