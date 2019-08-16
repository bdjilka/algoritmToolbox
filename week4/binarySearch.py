# python3
import sys


def binary_search(num, list):
    """
    Realization of binary search. The point of algorithm is that list is ordered, so you can check the medium element of
    list and cut one half of it depending on whether num is less or more that medium element.
    The complexity is O(log(n)).
    :param num: integer from 1 to 10**4
    :param list: list of integers in range(1, 10**9)
    :return: index of element or -1 it is not in list
    """
    left, right = 0, len(list) - 1
    while left <= right:
        middle = (right + left) // 2
        if num == list[middle]:
            return middle
        if num > list[middle]:
            left = middle + 1
        if num < list[middle]:
            right = middle - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    """
    Input contains from 2 lines:
    First line contains a number (integer from 1 to 10000) of elements in list and list itself.
    Second line an amount of numbers that needed to be found and numbers itself.
    
    For example:
    5 1 5 8 12 13
    5 8 1 23 1 11 
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(x, a), end=' ')
