# python3


def max_pairwise_product(numbers):
    """
    Naive realization on maximum pairwise product algorithm.
    Complexity is O(n^2)
    :param numbers: array of not negative integers
    :return: maximum multiple of two numbers from array
    """
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product


def optimax_pairwise_product(numbers):
    """
    Optimized realization on maximum pairwise product algorithm.
    Complexity is O(n)
    :param numbers: array of not negative integers
    :return: maximum multiple of two numbers from array
    """
    n = len(numbers)
    max1 = numbers[0] if numbers[0] > numbers[1] else numbers[1]
    max2 = numbers[1] if numbers[0] > numbers[1] else numbers[0]

    for i in range(2, n):
        if numbers[i] > max2:
            if numbers[i] > max1:
                max2 = max1
                max1 = numbers[i]
            else:
                max2 = numbers[i]

    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    print(optimax_pairwise_product(input_numbers))
