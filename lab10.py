from array import *
from typing import Tuple


def binary_search(numbers: array, value: int) -> Tuple[bool, int]:
    n = int((len(numbers)-1)/2)
    wartosc_srodkowa = numbers[n]

    if value > wartosc_srodkowa:
        for i in range(n, len(numbers)):
            if value == numbers[i]:
                return (True, i)
    elif (wartosc_srodkowa == value):
        return (True, n)
    else:
        for i in range(n, -1, -1):
            if value == numbers[i]:
                return (True, i)

    return (False, -1)






lista = array('i', [1,3,4,5,6,7,8])
print(binary_search(lista, 7))