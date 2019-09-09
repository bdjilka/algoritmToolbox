# Uses python3
import sys


def lcs3(arr1, arr2, arr3, n, m, k):
    """
    Compute the length of a longest common subsequence of three sequences.

    The idea in creating table of comparison. We go row by row and for each cell choose maximum variant, based on
    previous solutions.

    :param arr1: array of integers
    :param arr2: array of integers
    :param arr3: array of integers
    :param n: length of first array
    :param m: length of second array
    :param k: length of second array

    :return: integer
    """

    # matrix of longest common subsequences
    matrix = [[[0 for i in range(n + 1)] for j in range(m + 1)] for l in range(k + 1)]

    for l in range(1, k + 1):
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if arr1[i - 1] == arr2[j - 1] and arr2[j - 1] == arr3[l - 1]:
                    matrix[l][j][i] = matrix[l-1][j - 1][i - 1] + 1
                else:
                    matrix[l][j][i] = max(matrix[l - 1][j][i],
                                          matrix[l][j - 1][i],
                                          matrix[l][j][i - 1])

    return matrix[k][m][n]


if __name__ == '__main__':
    """
    Input example:
    4
    2 7 8 3
    4
    5 2 8 7
    3
    1 2 3

    The 1-st, 3-rd and 5-th lines contain an integer n (from 1 to 100), the 2-nd, 4-th and 6-th contain a sequence of 
    integers (each from -10**9 to 10**9).
    """
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    # a = [8, 3, 2, 1, 7]
    # an = 5
    # b = [8, 2, 1, 3, 8, 10, 7]
    # bn = 7
    # c = [6, 8, 3, 1, 4, 7]
    # cn=6

    print(lcs3(a, b, c, an, bn, cn))
