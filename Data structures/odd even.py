#8.1.2023
#Ghazal


# putting odd and even into separate lists

c= [4, 2, 6, 7, 88, 33, 555, 3, 9999]


e=[]
o=[]

for i in c:
    if i%2==0:          #[4, 2, 6, 88]
        e.append(i)

    else:
        o.append(i)     #[7, 33, 555, 3, 9999]


print('even list=', e)    
print('odd list=', o)
