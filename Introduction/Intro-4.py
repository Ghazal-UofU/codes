#25-12-2022
#Ghazal
#conversion between types (bool, int, float, str)


print(int(12))
print(int(12.1))
print(float(15))
print(float('51'))

#errors
#print(int('salam'))
#print(int(121.9))

#correct
print(int(float(121.9)))


print(str(10))  #why output not in '' ?
print(str(10.89))


print(bool(10))
print(bool(10.1))
print(bool(0.1))
print(bool(0))      #only 0 will be false
print(bool('salam'))
print(bool(" "))
print(bool(""))     #false because it is nothing


a='salam abc'
b= a[0:3]
print(b)
b= a[0:7]
print(b)

t=''
#print(t[0])
t=' '
print(t[0])
