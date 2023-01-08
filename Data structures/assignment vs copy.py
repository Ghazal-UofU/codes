#8.1.2023
#Ghazal

#difference between assignment and Copy


e= [3, 9, 90, 1, 77, 99]
p= e                        #assignment
print(p)
print(p==e)
print(p is e)

p. append(666)
print(p)
print(e)        # p and e both changed


t= e. copy()
print(t)


e. append(6)
print(e)
print(t)

#copy is udeful when u want to have the original one, and work on another list for some calculation




