# Consider a domain of size n = 5000.
# A: (5 points) Generate random numbers in the domain [n] until two have the same value. How many
# random trials did this take? We will use k to represent this value.






import random                   # importing random module

randomList=[]                   # random numbers list

randomList.append(random.randint(1, 5000))
counter = 1


while True:                     # traversing the while loop

    r=random.randint(1,5000)     # generating a random number in the range 1 to 5000

    

    if r not in randomList:     # checking whether the generated random number is not in the randomList

        randomList.append(r)    # appending the random number to the list, if the condition is true

        counter += 1


    else:
        break
    
print('k = ', counter)
print(randomList)
