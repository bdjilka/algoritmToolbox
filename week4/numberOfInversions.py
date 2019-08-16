#python3
import random
import sys


def merge_parts(a, left, middle, right):
    """
    Algorithm of merging two sorted parts into one sorted part. Also while merging algorithm checks if pair for
    inversion and returns number of inversions.
    :param a: initial array
    :param left: left bound of first array that is merged
    :param middle: divider between arrays
    :param right: right bound of second array that is merged
    :return: number of inversions
    """
    count = 0
    current = left
    arr = a[left:right + 1]
    index1 = left
    index2 = middle + 1

    while index1 <= middle and index2 <= right:
        if arr[index1 - left] <= arr[index2 - left]:
            a[current] = arr[index1 - left]
            index1 += 1
        else:
            a[current] = arr[index2 - left]
            count += middle - index1 + 1
            index2 += 1
        current += 1

    if index1 > middle:
        for i in range(current, right + 1):
            a[i] = arr[index2 - left]
            index2 += 1
    else:
        for i in range(current, right + 1):
            a[i] = arr[index1 - left]
            index1 += 1

    return count


def get_number_of_inversions(a, left, right):
    """
    This function finds number of all possible inversions (an inversion of a sequence a[0], a[1], ..., a[n−1] is a pair
    of indices 0<=i<j< n such that a[i] > a[j]). The number of inversions of a sequence in some sense measures how
    close the sequence is to being sorted.

    :param a: initial array
    :param left: left bound of array that is analysed
    :param right: right bound of array that is analysed
    :return: number of inversions

    This problem is solved with the help of merge sort algorithm. For this, standard Merge(A, B) function returns the
    resulting sorted array and the number of pairs (a, b) such that a is a part of A and b of B and a > b. MergeSort(A)
    function returns a sorted array A and the number of inversion in A.
    """
    number_of_inversions = 0
    if right == left:
        return number_of_inversions
    ave = (left + right) // 2

    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave + 1, right)

    number_of_inversions += merge_parts(a, left, ave, right)

    return number_of_inversions


def naive_realization(array):
    count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if a[i] > a[j]:
                count += 1
    return count


if __name__ == '__main__':
    """
    Input consists of integer, representing length of sequence ( from 1 to 10**9) and integer sequence itself (each 
    element lays in interval from 1 to 10**9) 
    """
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a) - 1))

    # while True:
    #     n = random.randint(1, 20)
    #     a = [random.randint(0, 100) for i in range(n)]
    #     naive = naive_realization(a)
    #     print('A: ', str(a))
    #     alg = get_number_of_inversions(a, 0, len(a) - 1)
    #     print(naive, ' ', alg)
    #     if alg != naive:
    #         break
