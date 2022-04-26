#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
if number >= 0:
    n = number % 10
else:
    n = -number % 10
    n = -n
if n > 5:
    print("{} {} is {} and is greater than 5".format(str, number, n))
elif n == 0:
    print("{} {} is {} and is 0".format(str, number, n))
elif n < 6 and n != 0:
    print("{} {} is {} and is less than 6 and not 0".format(str, number, n))
