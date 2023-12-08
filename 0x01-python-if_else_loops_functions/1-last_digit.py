#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    lstdgt = number % 10
    print(f"Last digit of {number} is {lstdgt} and is greater than 5")
elif number == 0:
    lstdgt = number % 10
    print(f"Last digit of {number} is {lstdgt} and is 0")
else:
    number = (+number)
    lstdgt = number % 10
    lstdgt = (-lstdgt)
    print(f"Last digit of {number} is {lstdgt} and is less than 6 and not 0")
