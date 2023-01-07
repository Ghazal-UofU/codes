#list tools for adding elements
#Ghazal_UofU
#7.1.2023



a= [4, 7, 'u', 00]


a[0]='Y'        #replacing an element
print(a)


a.append(5)     #adding element to the end of list a
print(a)


a.insert (1, 300)   #insert in the index 1 the value of 500
print(a)


a.insert (7, 'Ghazal')      #adding to the end of list
print(a)


a.insert (10, 'Yes')        #when the index is more than indexes+1, it adds it to the end of list
print(a)


a.extend('Uii')              #input should be iterable like list and str
print(a)


a.extend([7, 7, 10])        #adding a list to the list
print(a)


a.append([5,7,9])           #adding a list to the end of the list
print(a)


c=[5,0]
b=[1,1]
conc= c+b
print(conc)     #it is concatination, not sum
conc= b+c
print(conc)


c*=5        #5 times conctinating itself
print(c)
