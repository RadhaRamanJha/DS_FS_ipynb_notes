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
def fibbonaci_iteration(n):
    """Returns the nth fibbonaci number via iteration"""
    l = [0,1]
    for i in range(2,n+1):
        l.append(l[-1]+l[-2])
    return l[-1]
print(fibbonaci_iteration(10))