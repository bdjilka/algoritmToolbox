# python3


def opti_lastDigitFibonacci(number):
    """
    Realization of fibonacci algorithm, that returns only last digit.
    This saves memory and excludes situation of overflow
    :param number: index of fibonacci sequence
    :return: digit from 0 to 9
    """
    if number < 2:
        return number

    # creating array of zeros, length is equal to index of required fibonacci number, setting up first and second
    # elements equal to 1
    arr = [0 for i in range(number)]
    arr[0] = 1
    arr[1] = 1

    # computing other elements of array, but saving only last digit, this guarantees that 0 < arr[i-1] + arr[i-2] < 18
    # and 0 < arr[i] < 9
    # arr[i] is equal to i-th fibonacci number
    for i in range(2, number):
        arr[i] = (arr[i-1] + arr[i-2]) % 10
    return arr[-1] % 10


if __name__ == '__main__':
    input_number = int(input())
    print(opti_lastDigitFibonacci(input_number))
