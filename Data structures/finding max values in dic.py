# 23. 1. 2023
# finding max values in dic
# Ghazal


dic = {1: 100, 2: 200, 3: 300}
print (dic)

print ('-----------------------------------------')

for i in dic:
    print (i)           #in dic it returns keys
    
print ('-----------------------------------------')

for i in dic:
    print (dic[i])      # it returns values

print ('-----------------------------------------')

for i in dic:
    print (i, ":", dic [i])     #it returns keys and values

print ('-----------------------------------------')

# it's method

for i, j in dic. items ():
    print(i, j)                 #it returns keys and values, i and j types are tuple 

print ('-----------------------------------------')

dic1 = {'w1' : [34, 543, 87, 989, 324] ,    # max = 989
        'w2' : [4535, 6, 65, 99] }          # max = 4545

print(max(dic1))


ans = {}

for k, v in dic1. items():          # k: key, v: value
    ans.setdefault ( k, 0)          # it sets 0 for as the first key
    ans [k] = max (v)               # the value of k should be the max of the list
print(ans)

print ('-----------------------------------------')

dic1 = {'w1' : [34, 543, 87, 989, 324] ,    # max = 989
        'w2' : [4535, 6, 65, 99] }          # max = 4545

print(max(dic1))


ans = {}

for k, v in dic1. items():          # k: key, v: value
    ans.setdefault ( k, max (v))

print (ans)
   
