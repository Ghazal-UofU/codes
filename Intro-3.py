#24.4.2022
print(bin(1))
print(bin(2))
x=0*2**0 + 1*2**1 #0b10   #after 0b, the frist value from right is 0. so the value * (2 power the index 0 (starting from 0))+... 
print(x)
print(bin(3))   #0b11
y= 1*2**0 +1*2**1 
print(y)
print(bin(5))   #0b101
z=1*2**0+ 0*2**1+1*2**2
print(z)
print (True and True)
print(True or False)
print(True and False)
print(False or False)
a=10
if a>0 and a%2==0:
    print('even')
print(not True)
print (not False)


#XoR   when only one of them could be true
print(True !=True)  #false
print(True !=False)
print(False !=False) #false
print(False !=True)



print(True or True)  
print(True or  False)
print(False or False) #false 
print(False or True)


r= 4 | 10
print(r)
print(bin(14))
print(bin(True))
print(bin(False))


b= int('0b0', 2)    #binary dar mabnaye 2, che int khahad bud?
print(b)
v= int('0b101', 2)
print(v)
print(int('9999')) #converting str to int


s=4
print(bin(s))
c=1100
print(bin(c))
u= s & c
print(bin(u))
print(u)
print('---------------------------------------------------------')
print('4=', bin(4))
print('10=', bin(10))
e= 4 ^ 10  #^ means XoR
print('or result=', e)
print('14=', bin(14))   #put 0 on back of the smaller binary


print('---------------------------------------------------------')

a='salam'
print(a[0]) #starting from 0
print(a[4])
#print(a[5]) #out of the str

#counting indexes from the right with -

print(a[-1])
print(a[-4])
print(len(a))   #str lenght
print(len(a)-1)
print(a[len(a)-1])


b='Uii Ghazal'
t= b[0] +b[1] + b[2]
print(t)
o=b[0:3]        #[start:stop (up to but nor including):step]  it is slicing, default step is 1
print(o)

o=b[0:-1:2]
print(o)

o=b[0::]       #when stop is empty it means the whole str
print(o)

o=b[::2]        #start is 0 by default
print(o)

#reversing the str
o= b[len(b): : -1]   #don't put 0 for the stop, leave it empty if u want it to go through the whole str
print(o)



o= b[: : -1]
print(o)



