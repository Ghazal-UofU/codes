#23.12.2022
#str, evaluating str, is, in, not in

if 'aa' != 'bb':
    print('yes')
print ('a' >= 'b')
print ('aa' < 'ab')
print ('z' >= 'w')
print ('a' < 'aa')
print ('a' > 'aa')
print ('10' >= 'a') #why
print ('10' <= 'a')
print ('A' < 'a')
print ('a' < 'A')
a=100
a+=10
print(a)
b=20
b-=1
print(b)
t=1
t*=8
print(t)
y=2
y/=1
print(y)
q='abc'
q*=2
print(q)
q+="_UofU"
print(q)
a=2
print(a is 2.1) #why running truely but with syntax error
print(a is 2)
print( type(a) is int)
print( type(a) is float)
a='Ghazal'
if  'a' in a:   #not iterable in int and float
    print('Sure!')
print ('1' in '100') #this way we can search, because now it's not int, it's str
print('0' not in '100')



