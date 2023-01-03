#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{number:d} is_positive')
elif number < 0:
    print(f'{number:d} is_negative')
else:
    print(f'{number:d} is_zero')
