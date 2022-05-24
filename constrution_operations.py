"""
In this script, the author develops the operations to present for the user.

"""

import random

# Difficulty: Easy

def easy_sum_operation():
    # Number of digits will be 1 for the two numbers. Sum Operation
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    result = a + b
    print(f'{a}  +  {b}  =  ?\n')
    return result


def easy_subtraction_operation():
    # Number of digits will be 1 for the two numbers. Subtraction Operation
    a = 1
    b = 2
    while a <= b:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    result = a - b
    print(f'{a}  -  {b}  =  ?\n')
    return result

# Difficulty: Medium

def medium_sum_operation():
    # Number of digits will be 1 for the two numbers. Sum Operation
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    result = a + b
    print(f'{a}  +  {b}  =  ?\n')
    return result


def medium_subtraction_operation():
    # Number of digits will be 1 for the two numbers. Subtraction Operation
    a = 1
    b = 2
    while a <= b:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    result = a - b
    print(f'{a}  -  {b}  =  ?\n')
    return result

def medium_multiplication_operation():
    # Number of digits will be 1 for the two numbers. Multiplication Operation
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    result = a * b
    print(f'{a}  *  {b}  =  ?\n')
    return result

# Difficulty: Hard

def hard_sum_operation():
    # Number of digits will be 1 for the two numbers. Sum Operation
    a = random.randint(100, 999)
    b = random.randint(100, 999)
    result = a + b
    print(f'{a}  +  {b}  =  ?\n')
    return result


def hard_subtraction_operation():
    # Number of digits will be 1 for the two numbers. Subtraction Operation
    a = 1
    b = 2
    while a <= b:
        a = random.randint(100, 999)
        b = random.randint(10, 99)
    result = a - b
    print(f'{a}  -  {b}  =  ?\n')
    return result

def hard_multiplication_operation():
    # Number of digits will be 1 for the two numbers. Multiplication Operation
    a = random.randint(10, 99)
    b = random.randint(1, 10)
    result = a * b
    print(f'{a}  *  {b}  =  ?\n')
    return result

# Difficulty: Very Hard

def veryhard_sum_operation():
    # Number of digits will be 1 for the two numbers. Sum Operation
    a = random.randint(1000, 9999)
    b = random.randint(1000, 9999)
    result = a + b
    print(f'{a}  +  {b}  =  ?\n')
    return result


def veryhard_subtraction_operation():
    # Number of digits will be 1 for the two numbers. Subtraction Operation
    a = 1
    b = 2
    while a <= b:
        a = random.randint(1000, 9999)
        b = random.randint(100, 999)
    result = a - b
    print(f'{a}  -  {b}  =  ?\n')
    return result

def veryhard_multiplication_operation():
    # Number of digits will be 1 for the two numbers. Multiplication Operation
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    result = a * b
    print(f'{a}  *  {b}  =  ?\n')
    return result