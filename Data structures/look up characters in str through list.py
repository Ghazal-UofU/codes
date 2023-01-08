#8.1.2023
#Ghazal


#are there characters existing in the str through list [? ! # @]

s= 'jckfjeh#!0BB5984504%&*()tr'

signs= []


m= list (s)     #putting str in a list
print(m)

print('------------------------------------')

for i in s:             #or in m, because in this problem, for in str and for in list of that str are doing the same
    if i=='#' or i=='?' or i=='!' or i=='@':
        signs. append(i)
print(signs)
        
print('------------------------------------')


for i in m:
    if i=='#':
        signs. append(i)
    elif i=='?':              #the difference between if and elif here: here there is no difference, but it's better to use elif because if it was verifies as for example '?', then the work is finished!
        signs. append(i)
   
print(signs)

# plus  one more # to the previous signs
print('------------------------------------')

#if U see U are doing a job very difficuly, within a high probability there is a better way to do that!


#finding alphabets


#sample:
a= list ('hfuey%')
print('%' in a)
print('#' in a)

print('------------------------------------')


a= 'jrhgrghkfjre$$gjtgioreigtg&&&&&'


d= list (a)     #convert the str a into the list d


target= list ('jr$%#')

ans= []


for i in d:
    if i in target:
        ans.append(i)
print (ans)
