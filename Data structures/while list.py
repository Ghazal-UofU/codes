#9.1.2023
#Ghazal

#while


print(''.join(list('salaaaam')))            #concat them, not aplicable on integers

print(''.join(['d', 'g', 'jjj']))


print(''. join(['1', '2222', '100000']))    #these integers are str, so it is aplicable


print(' '. join(['1', '2222', '100000']))   #within a space between elements, the space is put at first like this: ' '


print(' ,'. join(['1', '2222', '100000'])) 


print(' **Yes!**'. join(['1', '2222', '100000']))


print('--------------------------------------------------')


 # Apple example

a= ['green', 'green', 'rusty',  'red', 'green']
clean = []

for i in a:
    
    if i=='rusty':
        continue
    if i=='green':
        clean.append(i)
    if i=='red':
        break

        
print(clean)

print('--------------------------------------------------')

#Apple problem with while

#while True needs break

a= ['green', 'green', 'rusty',  'red', 'green']

z= a.copy()         #for backup
print(z)

rusty_counter= 0
green_counter= 0

while True:
    apple= z. pop(0)
    if apple == 'red':
        break
    elif apple == 'rusty':
        rusty_counter +=1
    else:
        green_counter +=1

print('rusty: ', rusty_counter)
print('green: ', green_counter)
        
print('--------------------------------------------------')

#pop()

s= ['8438', '5435', '42035', '334', '43']

for i in range (len(s)):
    
    print(s.pop(0))
