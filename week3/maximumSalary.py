#python3

import sys


def isGTE(n, m):
    """
    Additional function to compare to numbers represented as stings.
    If number has equal number of digits, number compared as usual, in other case, greater is number with less amount N
    of digits and if first N digit number of second number is less of equal than first (ex., 2 > 21, 3 > 21, 43 < 445)
    :param n: first number
    :param m: second number (old max)
    :return: True/False
    """
    if len(n) == len(m):
        return n > m
    if len(n) < len(m):
        if n[-1] == '0' and n == m[0:len(n)]:
            if m[-1] == '0':
                return True
            return False
        if n == m[0:len(n)] and m[len(n)] >= n[0]:
            return False
        if n >= m[0:len(n)]:
            return True
        else:
            return False
    else:
        if m[-1] == '0' and m == n[0:len(m)]:
            if n[-1] == '0':
                return False
            return True
        if n[0:len(m)] == m and n[len(m)] >= m[0]:
            return True
        if n[0:len(m)] > m:
            return True
        else:
            return False


def largest_number(a):
    """
    Implementation of algorithm of building the largest number out of given. Each number lays in interval from 1 to 1000

    To
    :param a:
    :return:
    """
    res = ""
    while len(a) > 0:
        max = '0'
        for x in a:
            if isGTE(x, max):
                max = x
        res += max
        a.remove(max)
    return res


if __name__ == '__main__':
    """
    Input sample: 
    2               # amount of input numbers (from 1 to 100)
    21 2            # array of numbers
    """
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
