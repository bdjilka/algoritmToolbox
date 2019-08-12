#python3

import sys


def partition(nums, low, high):
    """
    Method to find new element that will divide list in two parts.
    Pivot determines as middle element. Through finding next pivot elements also swaps places if needed.
    :param nums: array of elements
    :param low: init index
    :param high: last index
    :return: index of next pivot element
    """
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] > pivot:
            i += 1
        j -= 1
        while nums[j] < pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def sort_array(array):
    """
    Additional function to sort array in descending order.
    (Quick sort)
    :param array: array to sort
    :return: sorted array
    """

    def _quick_sort(items, low, high):
        """
        Subsidiary function to provide recursion
        """
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(array, 0, len(array) - 1)

    return array


def max_dot_product(a, b):
    """
    Implementation of maximum advertisement revenue. You have n ads to place on a popular Internet page. For each ad,
    you know how much is the advertiser willing to pay for one click on this ad (array a). You have set up n slots on
    your page and estimated the expected number of clicks per day for each slot (array b). Goal is to distribute the
    ads among the slots to maximize the total revenue.
    :param a: array of integers in [-10**5, 10**5]
    :param b: array of integers in [-10**5, 10**5]
    :return: total profit

    Number of ads can vary form 1 to 1000.

    To achieve maximum profit we need to sort descending both array and then multiply a[i]*b[i] for each ad.
    """
    res = 0

    sorted_a = sort_array(a)
    sorted_b = sort_array(b)

    for i in range(len(a)):
        res += sorted_a[i] * sorted_b[i]
    return res


if __name__ == '__main__':
    """
        Input sample:
        3                      # number of ads
        1 3 -5                 # array of profits per click of each ad
        -2 4 1                 # array of average number of clicks for each slot
        """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
