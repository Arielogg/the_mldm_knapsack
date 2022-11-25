    
## -------------------------
## We take back the data
## -------------------------

# Modify this line of code to choose the data file

with open("instances_01_KP/low-dimensional/f7_l-d_kp_7_50","r") as Data:
#with open("instances_01_KP/large_scale/knapPI_1_10000_1000_1","r") as Data:

    # Initialization
    
    x = 0 # an increment to go over the data
    n = 0 # number of values in the data
    capacity = 0 # the capacity of the bag
    values = [] # the list of the values
    weight = [] # the list of the weight

    
    for i in Data:
        x+=1
        j = i.replace("\n","")
        k = j.split(" ")

        # We extract the value of n and the capacity of the bag in the first row
        if (x == 1):
            n = int(k[0])
            capacity = int(k[1])
            #print("n = "+ k[0])
            #print("capacity = "+ k[1])

        # We extract the weight and the values on the other rows
        else :
            if (x <=n+1):
                values.append(int(k[0]))
                weight.append(int(k[1]))

## -------------------
## Global variables
## -------------------

    upper = 100000000 # The upper variable. This value virtually equals +infinite
    # This value will define 
    comb = [] # "The solution :
    # This list contains an integer for each objet we have :
    # - 2 means that we still don't know if we're going to put the element
    #   in the bag at the end
    # - 1 means that we are sure that we will put the corresponding object in the bag at the end
    # - 0 means that we are sure we won't put the corresponding object in the bag at the end

    # First we fill the list with n values 2
    for i in range(n):
        comb.append(2)


## ----------
## Algorithm
## ----------
        
    def resoudre(list,k):
        # We take back the values, weights and the upper value
        global upper
        global values
        global weight
        somme_w = 0 # The progressive sum of the weight
        x = 0 # An increment that will allow us to go over the list of objects

        u = 0 # The sum of minus the values of the objects we use in each iteration
        c = 0 # Equals u plus the average of the weiht of the remaning available objects
        # Both of these values will allow us to know if we have to break the branch or not


        # While we are not on the last object and while we are not over the capacity of the bag :
        while ((x != n) and (somme_w + weight[x] <= capacity)):
            # If the object can/must be in the bag
            if (list[x] != 0):
                # Then we add the weight of the object to the sum of the weight
                somme_w = somme_w + weight[x]
                # And we add the negation of the object's value to c
                c = c - values[x]
            # We go to the next object
            x += 1
            
        # Once we got u we are looking for the value of u we compute c
        u = c
        # But first we compare u to the upper value, if it is lower, then upper become u
        if (u < upper):
            upper = u
            
        # We initialize the value that is missing to have c, it will be the next object with the best value/weight
        max_next = 0
        # While we are not on the last object, we are looking for the next most efficient object to fill the bag :
        while(x!=n):
            # If the object can/must be in the bag
            if (list[x] != 0):
                # We look if that object is more efficient
                if (values[x]/weight[x] >= max_next):
                    max_next = values[x]/weight[x]
            x += 1
        # We compute c with the best missing value/ratio to fill the capacity
        c = c - max_next * (capacity-somme_w)

        # If c > upper -> we break the branch
        if (c > upper): 
            return []
        # Else we go over the next branches
        else :
            # If we were at the last object then we have a solution
            if k == n:
                return list
            # Else we make two new branches
            else :
                # One branch where we put the k object in the bag
                list[k] = 0
                y = resoudre(list,k+1)
                if (y != []):
                    return y
                # Another where we do not put the k object in the bag
                list[k] = 1
                return resoudre(list,k+1)

## ---------------------
## Call of function
## ---------------------

    # At first we call the function starting from the first object (index 0)
    z = resoudre(comb,0)
    # Then we print the solution
    print(str(z))
    print("valeur = "+str(-upper))
