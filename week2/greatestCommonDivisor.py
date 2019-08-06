# python3


def gcd(a, b):
    """
    Recursive algorithm of finding the greatest common divisor.
    :param a: integer number
    :param b: integer number
    :return: integer number
    """
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(gcd(input_numbers[0], input_numbers[1]))
