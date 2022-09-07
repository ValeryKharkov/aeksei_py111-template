"""
Taylor series
"""
import math as m
from typing import Union

COUNT_SEQ = 2
def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = 1
    for idx in gen:
        val += x ** idx / math.factorial(idx)
    return val



def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)

    gen = range(1, COUNT_SEQ)
    val = x
    for idx in gen:
        sign = (-1) ** idx
        val += sign * x ** (2 * idx + 1)
    return val


print(sinx(50))