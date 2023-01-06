#6.1.2023
#for and indexing on lists

b=[1,100, 79, 50, ['Ghazal', 4]]


print (b[0])
print(b[-1])
#print(b[10])    #out of range

print(b[1:3:1])     #up to but not including


#printing 'Ghazal'

a= b[-1]
print(a)
print(a[0])

#or this way:

print(b[-1][0])

print('------------------------------------------')

print(b[-1][0][0])


print('------------------------------------------')

for i in b:
    print(i)
    
print('------------------------------------------')

#indexes for when u need to know the indexes
for i in range (len(b)):
    print(i)


for i in range (len(b)):
    print(b[0 : 5])
