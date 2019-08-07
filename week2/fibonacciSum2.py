# python3


def findCycle(n, m):
    """
    Find cycle of reminders in fibonacci sequence.
    :param n: index in sequence
    :param m: index in sequence
    :return: if loop is found earlier than 'n' number, returned length of cycle and array of reminders, else
    returned required 'm' and 'n' numbers itself
    """
    cycle = 2
    d = '0,1,'
    f2 = 0
    f1 = 1

    for i in range(2, n + 3):
        d += '{},'.format(str((f2 + f1) % 10))
        cycle += 1
        f2, f1 = f1, (f2 + f1) % 10

        if len(d) % 2 == 0:
            length = int(len(d) / 2)

            if d[0:length] == d[length:len(d)]:
                return {'ok': True,
                        'cycle': int(cycle/2),
                        'arr': d.split(',')[0:int(cycle/2)]
                        }
    return {
        'ok': False,
        'cycle': [int(d.split(',')[m+1]), int(d.split(',')[-2])]
    }


def lastDigitOfFibonacciSum(m, n):
    """
    Finds the last digit of sum of fibonacci numbers beginning from 'm' to 'n'.
    Algorithm is finds the 'n + 2' number in sequence and subtracts 'm + 1' number in sequence from it.

    'n' and 'm' can be very big (up to 10**14), so iteration approach is too slow. Because of it was firstly algorithm
    tries to find cycle of reminders.
    :param m: integer number
    :param n: integer number more or equal to m
    :return: integer from 0 to 9

    ----The idea and realization repeats file hugeFibonacci.py----
    """
    if n < 2:
        return n - m

    result = findCycle(n, m)
    if result['ok'] is False:
        return (result['cycle'][1] - result['cycle'][0]) % 10

    number1 = (n + 2) % result['cycle']
    number2 = (m + 1) % result['cycle']
    return (int(result['arr'][number1]) - int(result['arr'][number2])) % 10


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(lastDigitOfFibonacciSum(input_numbers[0], input_numbers[1]))
