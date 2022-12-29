#26.12.2022
#Ghazal
#if

x=-10
if x<1:
    print('lower than 1')
elif x==1:
    print('equal 1')
elif x==-10:
    print('-10')    #the previous condition was validated
else:               #otherwise, no condition        #we can use infinite elif s
    print('higher than 1')


print('---------------------------------------------------------')


u=100
if u<0:
    print('manfi')
else:               #elif with 0 can help
    print('mosbat')



print('---------------------------------------------------------')


y=0
if y>0:
    print('U got this')
    if y>90:
        print('top student')
    else:
        print('it isnt U')
print('not included')
    

print('---------------------------------------------------------')

p=99
if p>0 & p%3==0:
    print('divisible to 3')
else:
    print('not divisible to 3')

print('---------------------------------------------------------')

r=9000000000000001
if (r>0 and r%10==0) or (r%100==0):
    print('divisable to 10 or 100')
else:
    print('non-divisable to 10 or 100')
    
print('---------------------------------------------------------')
for i in 'salam':
    print(i)

for i in 'Ghazal':
    print('She is amazing!')
