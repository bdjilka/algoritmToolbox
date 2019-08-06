# python3


def fibonacci(number):
    """
    Recursive naive realization of fibonacci number calculation
    :param number: index of fibonacci number
    :return: required number
    """
    if number < 2:
        return number
    return fibonacci(number-1) + fibonacci(number-2)


def opti_fibonacci(number):
    """
    Optimized algorithm. Has linear dependency from time. But numbers can be were big and take more place then
    integer type allows
    :param number: index of fibonacci number
    :return: required number
    """
    if number < 2:
        return number
    arr = [0 for i in range(number)]
    arr[0] = 1
    arr[1] = 1
    for i in range(2, number):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[-1]


if __name__ == '__main__':
    input_number = int(input())
    # print(fibonacci(input_number))
    print(opti_fibonacci(input_number))
