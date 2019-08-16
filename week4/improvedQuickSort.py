# Uses python3
import sys
import random


def partition3(a, l, r):
    """
    Three way partition, used in cases when sequence has repeated elements
    :param a: sequence of integers
    :param l: left bound
    :param r: right bound
    :return: starting and ending index of elements equal to pivot
    """
    pivot = a[r]
    i = l - 1
    count = 0
    for j in range(l, r):
        if a[j] <= pivot:
            if a[j] == pivot:
                count += 1
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]

    res = [i + 1, count]

    # Replace all equal to pivot elements so that they all stand behind [i+1]-st pivot element.
    # For example, count=2, pivot=5 and the array from l to r is [2, 3, 5, 3, 5, 2, 5, 7, 7], the replaced array
    # must be: [2, 3, 2, 3, 5, 5, 5, 7, 7]
    if count > 0:
        replace_index = i
        current_index = i
        while count > 0:
            if a[current_index] == pivot:
                a[replace_index], a[current_index] = a[current_index], a[replace_index]
                replace_index -= 1
                count -= 1
            current_index -= 1

    return res


def partition2(a, l, r):
    """
    Standard partition used in quick sort
    :param a: sequence of integers
    :param l: left bound
    :param r: right bound
    :return: pivot index
    """
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def randomized_quick_sort(a, l, r):
    """
    Realization of quick sort algorithm for sequences, that have a few unique elements, so there is a lot of repeated
    elements.
    Pivot elements selected randomly and swaps with the first one.
    This realization allow to skip elements equal to pivot element and thus decrease number of iterations.
    :param a: sequence of integers
    :param l: left bound
    :param r: right bound
    :return: particularly sorted sequence
    """
    if l < r:
        k = random.randint(l, r)
        a[r], a[k] = a[k], a[r]
        m, count = partition3(a, l, r)
        randomized_quick_sort(a, l, m - 1 - count)
        randomized_quick_sort(a, m + 1, r)


def quick_sort(a, l, r):
    """
    Realization of quick sort algorithm. Pivot elements selected randomly and swaps with the first one.
    :param a: sequence of integers
    :param l: left bound
    :param r: right bound
    :return: particularly sorted sequence
    """
    if l < r:
        k = random.randint(l, r)
        a[r], a[k] = a[k], a[r]
        m = partition2(a, l, r)
        quick_sort(a, l, m - 1)
        quick_sort(a, m + 1, r)


if __name__ == '__main__':
    """
    Input sample:
    5               # amount of numbers
    2 3 9 2 2       # list of numbers
    """
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    # while True:
    #     n = random.randint(1, 100000)
    #     a1 = [random.randint(0, 1000000000) for i in range(n)]
    #     a2 = list(a1)
    #     print('N: ', n)
    #     print('ARRAY1 ', a1)
    #     quick_sort(a1, 0, n - 1)
    #     print('RES1: ', a1)
    #     print('ARRAY2 ', a2)
    #     randomized_quick_sort(a2, 0, n - 1)
    #     print('RES2: ', a2)
    #     if a1 != a2:
    #         break
