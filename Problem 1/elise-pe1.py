#STATUS: WIP

#DESCRIPTION: If we list all the natural numbers below 10 
#that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#NOTE: In order for it to work, I had to go from one if statement, i%3 == 0 | i%5 == 0, and split into the if/elif. I'm not sure why yet.

import math

sumOfMultiples = 0
for i in range (0,1000):
    if i%3 == 0:
        sumOfMultiples = sumOfMultiples + i
    elif i%5 == 0:
        sumOfMultiples = sumOfMultiples + i
print("The sum of all multiples of 3 or 5 below 1000 is: " + str(sumOfMultiples))



