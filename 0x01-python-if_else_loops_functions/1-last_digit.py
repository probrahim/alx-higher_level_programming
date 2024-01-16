#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pol= abs(number) % 10
if number < 0:
    pol = -pol
    print(f"Last digit of {number:d} is {pol:d} and is ", end="")
if pol > 5:
    print("greater than 5")
elif pol == 0:
    print("0")
else:
    print("less than 6 and not 0")
