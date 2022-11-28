
#Lien pour la modélisation d'arbres
#https://pixees.fr/informatiquelycee/n_site/nsi_term_projet_4.html

## ----------------------------------------------------------
## Mise en place des arbres binaires pour la modélisation
## ----------------------------------------------------------

class Arbre:
    def init(self,valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

    def insert_g(self,valeur):
        if self.gauche == None:
            self.gauche = Arbre(valeur)
        else:
            node = Arbre(valeur)
            node.gauche = self.gauche
            self.gauche = node

    def insert_d(self,valeur):
        if self.droite == None:
            self.droite = Arbre(valeur)
        else:
            node = Arbre(valeur)
            node.droite = self.droite
            self.droite = node

    def get_valeur(self):
        return self.valeur
    
    def get_gauche(self):
        return self.gauche

    def get_droite(self):
        return self.droite
    
## -------------------------
## Récupération des données
## -------------------------

with open("low-dimensional/f7_l-d_kp_7_50","r") as Data:
#with open("instances_01_KP/large_scale/knapPI_1_10000_1000_1","r") as Data:
    x = 0
    n = 0
    capacity = 0
    values = []
    weight = []
    for i in Data:
        x+=1
        j = i.replace("\n","")
        k = j.split(" ")
        if (x == 1):
            n = int(k[0])
            capacity = int(k[1])
            #print("n = "+ k[0])
            #print("capacity = "+ k[1])

        else :
            if (x <=n+1):
                values.append(int(k[0]))
                weight.append(int(k[1]))
                
    #print(values)
    #print(weight)

## -------------------
## Variables globales
## -------------------

    upper = 100000000 # "upper" equals +infinite
    comb = []
    for i in range(n):
        comb.append(2)

## --------------------------------
## Fonction d'affichage de l'arbre
## --------------------------------

    def affiche(A):
        if A!=None:
            return (A.get_valeur(), affiche(A.get_gauche()), affiche(A.get_droite()))

## ----------
## Algorithm
## ----------
        
    def resoudre(list,k):
        global upper
        global values
        global weight
        #print (str(upper))
        #print (str(list))
        somme_w = 0
        c = 0
        u = 0
        x = 0
        ######
        
        while ((x != n) and (somme_w + weight[x] <= capacity)):
            if (list[x] != 0):
                somme_w = somme_w + weight[x]
                c = c - values[x]
            x += 1
        u = c
        #print("u="+str(u))
        if (u < upper):
            upper = u
            print("nouveau upper = "+str(upper))
        max_next = 0
        while(x!=n):
            if (list[x] != 0):
                if (values[x]/weight[x] >= max_next):
                    max_next = values[x]/weight[x]
            x += 1
        c = c - max_next * (capacity-somme_w)
        #print("c="+str(c))

        
        ######
        if (c > upper): # Si c > upper -> on ne cherche pas plus bas
            #print("On kill")
            return []
        else : # Sinon on explore en dessous
            #print("On continue")
            if k == n:
                return list
            else :
                list[k] = 0
                y = resoudre(list,k+1)
                if (y != []):
                    return y
                list[k] = 1
                return resoudre(list,k+1)

## ---------------------
## Appel de la fonction
## ---------------------

    z = resoudre(comb,0)
    print(str(z))
    print("valeur = "+str(-upper))