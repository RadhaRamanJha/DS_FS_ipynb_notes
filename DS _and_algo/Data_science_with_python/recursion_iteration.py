# Recursion Examples
## 1. Factorial calculation
def factorial_recursion(n: int) -> int:
    """Returns the factorial of n via recursion"""
    if n == 0:
        return 1
    else:
        return n*factorial_recursion(n-1)
print(factorial_recursion(5))

## 2. Calculate nth fibbonacci number
def fibbonaci_recusrsion(n: int) -> int:
    """Returns the nth fibbonaci number via recurssion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci_recusrsion(n-1) + fibbonaci_recusrsion(n-2)

print(fibbonaci_recusrsion(10))

## 3. List out all the files in a directory
from typing import Union
from pathlib import Path
import os

PathType = Union[str,Path]
def list_files_recurrsive(path:PathType) -> str:
    """Recurrsively lists all files in a specified path"""
    for file in os.listdir(path):
        item_path = os.path.join(path,file)
        if os.path.isfile(item_path):
            print(item_path)
        elif os.path.isdir(item_path):
            list_files_recurrsive(item_path)
list_files_recurrsive(r"C:\radha\R-basics")

# iteration Examples
## 1. Factorial calculation
def factorial_iteration(n: int) -> int:
    """Returns the factorial of n via iteration"""
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial_iteration(5))

## 2. Calculate nth fibbonacci number
def fibbonaci_iteration(n: int) -> int:
    """Returns the nth fibbonaci number via iteration"""
    l = [0,1]
    for i in range(2,n+1):
        l.append(l[-1]+l[-2])
    return l[-1]
print(fibbonaci_iteration(10))

## 3. Calculation of average
from typing import List
def calculate_average(numbers: List) -> float:
    """Calculates the average of all numbers present in List or Tuple"""
    count = 0
    total = 0
    for number in numbers:
        count += 1
        total += number
    return total/count
print(calculate_average([3,4,5,6,7,8]))
print(calculate_average((4,5,6,7)))

## Hybrid - Recurssion and Iteration