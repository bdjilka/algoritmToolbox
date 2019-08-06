# python3


def findCycle(number):
    """
    Find cycle of reminders in fibonacci sequence.
    :param number: index in sequence
    :param modulo: integer number
    :return: if loop is found earlier than required number, returned length of cycle and array of reminders, else
    returned required number itself
    """
    cycle = 2
    d = '0,1,'
    f2 = 0
    f1 = 1
    for i in range(2, number + 2):
        d += '{},'.format(str((f2 + f1) % 10))
        cycle += 1
        f2, f1 = f1, (f2 + f1) % 10
        if len(d) % 2 == 0:
            length = int(len(d) / 2)
            if d[0:length] == d[length:len(d)]:
                return {'ok': True, 'cycle': int(cycle/2), 'arr': d.split(',')[0:int(cycle/2)]}
    return {'ok': False, 'cycle': [int(d.split(',')[-3]), int(d.split(',')[-2])]}


def lastDigitOfFibonacciSquareSum(number):
    """
    Finds the last digit of sum of this first 'number' fibonacci numbers squared.
    Algorithm is finds the 'number + 1' and 'number' numbers in sequence and multiples them.

    'number', fibonacci[number] and square of it can be very big (up to 10**14), so iteration approach is too slow.
    Because of it firstly algorithm tries to find cycle of reminders.
    :param number: integer number
    :return: integer from 0 to 9
    """
    if number < 2:
        return number

    result = findCycle(number)
    if result['ok'] is False:
        return (result['cycle'][0] * result['cycle'][1]) % 10

    n1 = (number + 1) % result['cycle']
    n = (number) % result['cycle']
    return (int(result['arr'][n]) * int(result['arr'][n1])) % 10


if __name__ == '__main__':
    input_number = int(input())
    print(lastDigitOfFibonacciSquareSum(input_number))
