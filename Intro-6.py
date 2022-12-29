#28.12.2022
#Ghazal

for _ in 'salam':    #_ is a throwable memory
    print ('Hellooooo')

for _ in '10000':   #can only write for on str & data struct
    print(type(_), ':', _)

print('-------------------------------------------------------')
for i in [1, 2, 3]:     #list
    print(i)

print('-------------------------------------------------------')
for i in range (0, 101, 5): #(start, stop, step)    #stop up to but not incuding
    print(i)

print('-------------------------------------------------------')
   
for i in range (5): #(start, stop, step)    #stop up to but not incuding
    print(i)

print('-------------------------------------------------------')
   
for i in range (0, 5): #(start, stop, step)    #stop up to but not incuding
    print(i)

print('-------------------------------------------------------')
   
for i in range (70, 101, 5): #(start, stop, step)    #stop up to but not incuding
    print(i)

print('-------------------------------------------------------')
   
#nested for  #for in for
for i in range (1, 4):
    for j in range (10, 90, 10):    #8 times
        print(i, ':', j)
#i=1 j=10 1:10
#i=1 j=20 2:20
#i=1 j=30 1:30
#i=1 j=40 1:40
#it continues to conduct all the iterations in inner for, and then goes to external for again

print('-------------------------------------------------------')

for i in range (1, 4):  #stop=3
    for j in range (1,4):
       print ([i,j])

print('-------------------------------------------------------')
#break & continue
#continue means leave it a side
#break means finish the loop

for i in range(1, 10, 2):
    for j in range (1, 2, 1):
        if i==5:
            continue #not running 5
        if i==9:
            break #finishing loop
        print([i,j*2])
    
