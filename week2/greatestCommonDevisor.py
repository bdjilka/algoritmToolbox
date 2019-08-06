# python3


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def opti_gsd(a, b):
    return a*b


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(gcd(input_numbers[0], input_numbers[1]))
