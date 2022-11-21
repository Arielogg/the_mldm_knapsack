#param : nombre d'itération, faire deux listes, une autre listes avec n random par exemple le premier ->4 k[4]->1
# boucle n -> qui va faire le truc random
import random
with open("../AdvancedAlgorithm/knapPI_1_2000_1000_1", "r") as Data:

    x = 0
    n = 0
    values = []
    weight = []

    for i in Data:
        x+=1
        j = i.replace("\n","")
        k = j.split(" ")
        #print(k)
        if (x == 1):
            n = int(k[0])
            capacity = int(k[1])
            #print("n = "+ k[0])
            #print("capacity = "+ k[1])

        else :
            if (x <=n+1):
                values.append(int(k[0]))
                weight.append(int(k[1]))
    def randomize(weight,values,capacity) :
        #le nombre de chemin random qu'il va prendre
        it=10000
        # creation de la variable qui renverra le meilleur choix
        bestChoice = []
        bestValue = 0
        bestWeight = 0
        for tour in range (it) :
            # liste de nombre aléatoire de taille n,corresponds a indice du tableau
            ran = random.sample(range(n), n)
            #print(ran)
            # creation des variables temporaire de poids,valeur
            tempweight = 0
            tempvalue = 0
            #servira de liste temporaire qui conservera la meilleur chemin
            a = []
            # initialisation de notre liste a
            for i in range(n):
                a.append(0)
            #print(a)
            #boucle qui va parcourir tout les elem de ma liste ran
            for i in range(0,n-1) :
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
            #print(bestValue)
        print("val : " + str(bestValue))
        print("weight : " + str(bestWeight))
        print("solution vect : " + str(bestChoice))

    randomize(weight, values, capacity)