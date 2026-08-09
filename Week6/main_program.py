# main_program.py - Lab 6.2: Using custom module and standard library modules
import math
import random

import my_utils

my_utils.greet("Alice")

for n in (7, 10):
    print(f"Is {n} prime? {my_utils.is_prime(n)}")

number = 16
print(f"Square root of {number} is {math.sqrt(number)}")

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
