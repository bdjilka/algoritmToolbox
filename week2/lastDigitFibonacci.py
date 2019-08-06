# python3


def opti_lastDigitFibonacci(number):
    if number < 2:
        return number
    arr = [0 for i in range(number)]
    arr[0] = 1
    arr[1] = 1
    for i in range(2, number):
        arr[i] = (arr[i-1] + arr[i-2]) % 10
    return arr[-1] % 10


if __name__ == '__main__':
    input_number = int(input())
    print(opti_lastDigitFibonacci(input_number))
