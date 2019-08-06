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


def lcm(a, b):
    """
    Algorithm of finding the least common multiple. Firstly if finds the greatest common divisor and
    with its help returns least common multiple.
    :param a: integer number
    :param b: integer number
    :return: required integer number
    """
    d = gcd(a, b)
    return int(a / d * b)


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(lcm(input_numbers[0], input_numbers[1]))
