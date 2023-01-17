# 17. 1. 2023
#counting elements in dic

dic = [1, 2, 5, 'd', 9001, 1, 1, 2]     # {1: 3 times, 2: 2times, ...}


result = {}
print(type(result))

print ('------------------------------------------')

for i in dic:
     result.setdefault (i, 0)  # if the key exists, it does not change it! if it does not exist, it adds it!
     result [i] += 1
     print(result)      # counts in each iteration



print (result)      #why again printing?
