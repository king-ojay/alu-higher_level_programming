#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = abs(number) % 10 if number >= 0 else -(-number % 10)

if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {result}")
