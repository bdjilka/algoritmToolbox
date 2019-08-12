#python3

import sys
import math


def optimal_summands(n):
    """
    Implementation of maximum number of prizes. You have n rewards and need to find out which maximum number of prize
    places can you make. The restriction is that every higher place must has more rewards that the lower one.
    The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
    distinct positive integers as possible. That is, to find the maximum k such that n can be written as
    a1 + a2 + ... + ak where a1,..., ak are positive integers and ai != aj for all 1 <= i < j <= k.

    :param n: integer from 1 to 10**9
    :return: array of integers, representing number of rewards for each place

    If we assume that the lowest place will take one 1 reward and every other place will take one more reward, than it
    is obvious that we have an arithmetic progression 1, 2, 3, 4, 5, ... . So we need to find the closest number less
    of equal to n, that is sum of that progression. The reminder of prizes will go to the first place.
    """
    k = int((-1 + math.sqrt(1 + 8*n)) // 2)
    reminder = (-1 + math.sqrt(1 + 8*n)) % 2

    summands = [i + 1 for i in range(k)]
    if reminder != 0:
        summands[-1] += int(n - (1 + k) / 2 * k)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
