#30.12.2022
#Ghazal
#while, input, debug (killing errors), a mbrief referring to (runtime error (resources), semantic error(logic))




a= input('please enter a num:')
print(type(a))


a= int(a)


counter=1
while a>=10:        #why only 10 brings the right output
    a= a//10
    counter+=1
    
print(counter)

print('----------------------------------------------')

# built-in function (it exist in the essense of Python by it's own) like the input which is a built-in func and it's initial output is str

b= int (input('please enter a num:'))
print(type(b))
