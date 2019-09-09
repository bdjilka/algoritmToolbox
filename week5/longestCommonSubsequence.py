# Uses python3
import sys


def longestCommonSubsequence(first, second, n, m):
    """
    Compute the length of a longest common subsequence of two sequences.

    The idea in creating table of comparison. We go row by row and for each cell choose maximum variant, based on
    previous solutions.

    :param first: array of integers
    :param second: array of integers
    :param n: length of first array
    :param m: length of second array
    :return: integer
    """
    # matrix of longest common subsequences
    matrix = [[0 for i in range(n + 1)] for j in range(m+1)]

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if first[i - 1] == second[j - 1]:
                matrix[j][i] = matrix[j - 1][i - 1] + 1
            else:
                matrix[j][i] = max(matrix[j - 1][i], matrix[j][i - 1])

    return matrix[m][n]


if __name__ == '__main__':
    """
    Input example:
    4
    2 7 8 3
    4
    5 2 8 7

    The first and third lines contain an integer n (from 1 to 100), the second and last contain a sequence of 
    integers (each from -10**9 to 10**9).
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    first = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    second = data[:m]

    print(longestCommonSubsequence(first, second, n, m))
