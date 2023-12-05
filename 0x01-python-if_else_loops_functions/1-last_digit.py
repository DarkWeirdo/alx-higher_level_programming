#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if number > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif number < 5:
    print(f"Last digit of {number} is {lastdigit} and\
          is less than 5 and not 0")
else:
    print(f"Last digit of {number} is {lastdigit} and is 0")
