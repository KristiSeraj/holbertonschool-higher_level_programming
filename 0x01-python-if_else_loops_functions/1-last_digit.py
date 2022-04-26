#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last  digit of"
if number >= 0:
    n = number % 10
else:
    n = (number - number - number) % 10
if n > 5:
    print(str + " {} is {} and is greater than 5".format(number, n))
elif n == 0:
    print(str + " {} is {} and is 0".format(number, n))
elif n < 6 and n != 0:
    print(str + " {} is {} and is less than 6 and not 0".format(number, n))
