# python3


def findCycle(number, modulo):
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
    for i in range(2, number + 1):
        d += '{},'.format(str((f2 + f1) % modulo))
        cycle += 1
        f2, f1 = f1, (f2 + f1) % modulo
        if len(d) % 2 == 0:
            length = int(len(d) / 2)
            if d[0:length] == d[length:len(d)]:
                return {'ok': True, 'cycle': int(cycle/2), 'arr': d.split(',')[0:int(cycle/2)]}
    return {'ok': False, 'cycle': int(d.split(',')[-2])}


def opti_fibonacci(number, modulo):
    """
    Modified fibonacci algorithm to work with big numbers. It finds not whole numbers but its reminder from
    division of fibonacci[number] by modulo number, where fibonacci[i] is i-th number in fibonacci sequence.

    As fibonacci sequence of reminders is periodic, we can find this period and cut number of iterations.
    :param number: index of fibonacci sequence number required to find
    :param modulo: positive integer number more than 2
    :return: required fibonacci number
    """
    if number < 2:
        return number % modulo

    result = findCycle(number, modulo)
    if result['ok'] is False:
        return result['cycle']

    n = number % result['cycle']
    return result['arr'][n]


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(opti_fibonacci(input_numbers[0], input_numbers[1]))
