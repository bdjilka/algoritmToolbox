# python3


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    d = gcd(a, b)
    return int(a / d * b)


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(lcm(input_numbers[0], input_numbers[1]))
