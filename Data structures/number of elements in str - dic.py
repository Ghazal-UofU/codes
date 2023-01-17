# 17. 1. 2023
# counting str elements in a dic (frequency count) 

o = 'dhff?hjefeji???4455$'

result = {}

for i in o:
    result.setdefault (i, 0)        # if i has a value, remain it. Otherwise, it is 0
    result [i] += 1

print (result)

print ('--------------------------------------------')

#non-letter counting

 
result = {'?' : 0, '$' : 0}

for i in o:
    if i == '?' or i=='$':
        result[i] += 1

print (result)

print ('--------------------------------------------')

#non-letter counting

 
result = {'?' : 0, '$' : 0}

for i in o:
    if i == '?':
        result[i] += 1
    elif i == '$':
        result [i] +=1

print (result)

print ('--------------------------------------------')

#non-letter counting

 
result = {'?' : 0, '$' : 0}
target = '?$'


for i in o:
    if i in target:
        result [i] +=1

print (result) 

print ('--------------------------------------------')

# in skillful programming U should prevent repeating pieces of codes! Optimize it!
# " The best code I've ever written, is the one that I never wrote! " :
# it probably means I wrote another optimized code rather than that!
