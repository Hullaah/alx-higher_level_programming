#!/usr/bin/python3
"""pascal triangle module
this module was done as part of the projects done
during the alx SE training. It contains the function pascal_triangle
that implements pascal's triangle
"""


def pascal_triangle(n: int) -> int:
    ans = []
    if n <= 0:
        return []
    for i in range(n):
        """if i == 0:
            ans.append([1])
        else:"""
        ans.append([int(combination(i, x)) for x in range(i + 1)])
    return ans

        
    
def factorial(n: int) -> int:
    """Calculates the factorial of a number
    Args:
        n: number whose factorial is to be calculated
    Return:
        n!
    """
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans

def permutation(n: int, x: int) -> int:
    """Calculates the permuation of x in n
    Args:
        n: Number
        x: Number
    Return:
        n! / (n - x)!
    """
    return factorial(n) / factorial(n - x)

def combination(n: int, x: int) -> int:
    """Calculates the permuation of x in n
    Args:
        n: Number
        x: Number
    Return:
        n! / (n - x)!x!
    """
    return permutation(n, x) / factorial(x)
