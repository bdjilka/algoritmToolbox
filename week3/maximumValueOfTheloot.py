# python3
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
    pivot = nums[(low + high) // 2]['value']
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i]['value'] > pivot:
            i += 1
        j -= 1
        while nums[j]['value'] < pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def sort_relative_value(weights, values):
    """
    Additional function to sort relative value value[i]/weight[i] in descending order.
    (Quick sort)
    :param weights: array of weights of items
    :param values: array of values of items
    :return: array of indexes
    """

    def _quick_sort(items, low, high):
        """
        Subsidiary function to provide recursion
        """
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    rel_values = [{'index': i, 'value': values[i] / weights[i]} for i in range(len(values))]
    _quick_sort(rel_values, 0, len(rel_values) - 1)

    return rel_values


def get_optimal_value(capacity, weights, values, n):
    """
    Implementation of algorithm for the fractional knapsack problem.

    Algorithm firstly sort items by descending relative value value[i]/weight[i]. Then we take as much of first sorted
    item as possible (whole or a part of it), then we make the exact same procedure with second item of tre sorted list.
    We repeat it until we won't reach capacity.

    The function returns summary value of items

    :param capacity: integer, capacity of knapsack
    :param weights: array of weights of items
    :param values: array of values of items
    :param n: number of items
    :return: resulting summary value
    """
    if n == 1:
        return values[0] * min(weights[0], capacity) / weights[0]

    related_values = sort_relative_value(weights, values)
    sum_value = 0
    i = 0

    while capacity > 0 and i < n:
        index = related_values[i]['index']
        rel_value = related_values[i]['value']
        count = min(capacity, weights[index])
        capacity -= count
        sum_value += rel_value * count
        i += 1

    return sum_value


if __name__ == "__main__":
    """
    Input format example:
    3 50
    60 20
    100 50
    120 30
    
    first line: number of items (3) and capacity of knapsack (50)
    every other line: value of item (60) and weight of item (20)
    
    Limitation:
    number of items: 1 <= n <= 10**3
    capacity: 0 <= W <= 2*10**6
    value of item: 0 <= vi <= 2*10**6
    weight of item: 0 <= vi <= 2*10**6
    """
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values, n)
    print("{:.10f}".format(opt_value))
