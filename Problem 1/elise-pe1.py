#project euler number 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


1--under 10, mult by 3 or 5? yes
2 -- under 10, div by 3 or 5? no
3 -- under 10, div by 3 or 5? yes
4 -- no
5-- yes
6 - yes
7 - no
8 --no
9 --yes.

3+5+6+9 = 23

#string MultsOfThreeOrFive #array of characters of unknown length? or make it a string you concatenate
#or just add to total every time you find one.
i = 3
sum = 0
for i in range (0,1001)
    if ( div(i, 3) == 3 ) || ( div(i, 5) == 5 ) #is it a sum of 3 or 5?
        then sum = sum + i
print(sum)



##################
i = 0
for i in range (0,1000)
    if i%3 == 0 | i%5 == 0:
        sum = i + i
