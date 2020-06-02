'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
from pip._vendor.distlib.compat import raw_input


def factorial(n):
    if n < 2 :
        return 1
    else :
         return    n * factorial(n-1)

# input comma separated elements as string
str = str (raw_input ("Enter comma separated integers: "))
# conver to the list
list = str.split (",")
print ("list: ", list)

# convert each element as integers
li = []
for i in list:
	li.append(factorial(int(i)))

# print list as integers
print ("factorial: ", li)
