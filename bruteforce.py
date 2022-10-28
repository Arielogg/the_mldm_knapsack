with open("f1_l-d_kp_10_269","r") as Data:

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
    def binaire(number):
        q = -1
        resul = []
        while q != 0:
            q = number // 2
            r = number % 2
            resul.append(r)
            number = q
        return resul


    def val(bestChoice):
        sum = 0
        for k in range(n):
            if (bestChoice[k] == 1):
                sum = sum + values[k]
        return sum
    def brutforce(values,weight,capacity):
        data = n  # recup le nombre d'objet
        tab = []  #we will stock the binary table
        bestChoice = []
        bestval=0
        a=[]
        totval=0
        for i in range(n):
            a.append(0)
        for i in range(0, pow(2, data)):  # for 1 to 2^n
            tab=binaire(i)#for obtain the binary number of i
            tempval = 0  # will stock the value
            tempweight = 0  # will stock the weight
            while (len(tab)!=len(a)) : #we will have table : 1 the object in the bag 0 not in the bag
                tab.insert(0,0)
            a=tab
            for k in range (n) :
                if(tab[k]==1) : #the object is in bag
                    tempval = values[k] + tempval
                    tempweight = tempweight + weight[k]
                if(tempweight<=capacity and tempval>bestval):
                    bestChoice=a
                    bestval=tempval
        print(val(bestChoice))
        return bestChoice
    brutforce(values,weight,capacity)
