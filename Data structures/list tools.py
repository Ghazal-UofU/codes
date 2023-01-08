#8.1.2023
#Ghazal

#some other tools for lists (such as: index, count, sort, reverse, copy)


o= [5, 33, 33, 0, 76]
print (o. index(33))        #indexes are zero-based (they start from 0), it returns the index of 33 (the first 33)

print (o. index(76))



print(o.count(33))      #it counts the number of iteration that 33 appeared in the list


o.sort()                #it sort the list
print(o)


y= [ 88, 1401, 97, 1400]

y. sort()       #key enables u to define a func that lets u give it a metric to evaluate it
print(y)


y.sort(reverse=True)    #a reverse sort
print(y)


y. copy()       #it presents a copy of that list
print(y)
