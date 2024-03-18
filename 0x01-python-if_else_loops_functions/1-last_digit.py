#!/usr/bin/python3
import random
# number = random.randint(-10000, 10000)
number = -98
if number > 0:
    lastdigit = abs(number) % 10
else:
    lastdigit = -(abs(number) % 10)
# print(number)
# print(lastdigit)
statement = f"Last digit of {number} is {lastdigit}"
if lastdigit > 5:
    print(f"{statement} and is greater than 5")
elif lastdigit == 0:
    print(f"{statement} and is 0")
elif lastdigit < 6:
    print(f"{statement} and is less than 6 and not 0")
