#10.1.2023
#Ghazal

#dictionary : a data structure for tagged data, in dic the data is not in order, it uses keys! it is comrised of pairs (key, value). The key can not be repetetive.


#for a data like this: ['Ghazal', 'Abdollahi', '1991', 'PhD', 'UofU']


z= dict ()
print(type (z))

print('-----------------------------------------------')

# {'key': value}


u = {'name': 'Ghazal', 'last name': 'Abdollahi', 'birth date': 1991, 'level': 'PhD', 'university': 'UofU'}
print (u)

#print(u[0])  the dic needs key! not index!

print('-----------------------------------------------')

print (u['name'])

print (u['last name'])

#if you repeat a key, it keeps the last one

e= {1: 'Ghazal', 2:'dream', 2:'Yes'}
print (e)

print (e[1])

print (e[2])

#print (e[0])

print('-----------------------------------------------')


#printing the keys
print (e.keys())

print (u.keys())

#printing values

print (u.values())

print (e.values())

print('-----------------------------------------------')

p= {1: 'Ghazal', 2:'dream', 2:['Yes', 100, 1000]}
print (p[2])
print(p[2][-1])     #returning the inner ones

print('-----------------------------------------------')

#modification on dic


p[2]= 'Got it!'
print (p)


#add elements

p[2023]= 'Shine Bright!'
print (p)


print('-----------------------------------------------')

#converting to list

list (p)
print(p)

#length
print (len (e))
print (len (p))

print('-----------------------------------------------')

#delete

print(p)
del p[1]
print (p)

print('-----------------------------------------------')

#key in dic
print ('salam' in e)
print (1 in e)
print('-----------------------------------------------')
