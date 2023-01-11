#11.1.2023

#Ghazal

#overview on dictionary


d= {1:'book', 2: 'pen', 3: 'Ipad', 4: '$'}

print('1' not in d) #key not in dic
print(1 not in d)

print('-------------------------------------------------')


#items() return the pairs , key and value pair = item
b =d.items()
list(b) #in a format of list

print(b)


print('-------------------------------------------------')

#it returns the coresponding value to the key requested

print(d. pop(1))


print (d)   #1 has been removed

reversed (d)        #???
print(d. keys)
print (d)

print('-------------------------------------------------')


print(d.setdefault(2))

d.setdefault(2, 'pencil')       #if the key exists in the dic, the injected value won't be applied

print(d)

d.setdefault(10, 'pencil')  #adding because it does not exist now

print(d)


print('-------------------------------------------------')

