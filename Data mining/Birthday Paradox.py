#Ghazal_UofU
# birthday problem
# How many people in a room have a 50, 50 chance of having the same birthday?

# the days within a year = 365

# ref : https://www.geeksforgeeks.org/birthday-paradox/


# infact the answer is 23 which is very low! we try to prove
# the probability of not having the same birthday!
# P(same) = 1 – P(different)
# P(different) can be written as :
# 1 x (364/365) x (363/365) x (362/365) x …. x (1 – (n-1)/365)


# Solution 1 :

import math
# Returns approximate number of
# people for a given probability
def find( p ):
    return math.ceil(math.sqrt(2 * 365 *            # celi for rounding
        math.log(1/(1-p))));
# Driver Code
print(find(0.70))


print('------------------------------------------------------------------')
