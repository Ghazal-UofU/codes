#30.12.2022
#Ghazal_uofU
#solving problems with for and if



#d= 'wrig AAAA bB'  #moving throughout the str needs for        #cheking needs if       #counting needs counter



d= input ('please enter a str : ')

counter_up = 0
counter_low = 0

for i in d:
    if i.isupper():     #func for uppercase recognition
        counter_up+=1
    else:
        counter_low+=1   #space is not lower neither upper, this is the bug of our code

print('the num of upperCase is =', counter_up)
print('the num of lowerCase is =', counter_low)
        
        

print('---------------------------------------------------')

#as I mentioned above in comments

c=' '.islower()
w=' '.isupper()

print(c)
print(w)

print('---------------------------------------------------')


d= input ('please enter a str : ')

counter_up = 0
counter_low = 0
none_letter_counter=0

for i in d:
    if i.isupper():     #func for uppercase recognition
        counter_up+=1
    elif i.islower():                                       ###resolving the bug
        counter_low+=1   #space is not lower neither upper, this is the bug of our code
    else:
        none_letter_counter+=1   #like num or space or ...

print('the num of upperCase is =', counter_up)
print('the num of lowerCase is =', counter_low)
print('the num of non-letters is = ' , none_letter_counter)


print('---------------------------------------------------')
