# python3


def findCycle(number, modulo):
    """
    Find cycle of reminders in fibonacci sequence.
    :param number: index in sequence
    :param modulo: integer number
    :return: if loop is found earlier than required number, returned length of cycle and array of reminders, else
    returned required number itself
    """
    # the length of period multiplied twice
    cycle = 2

    # string, representing sequence of reminders of fibonacci numbers
    d = '0,1,'

    # f2 and f1 is previous and prev-previous fibonacci numbers, for example, if we are managing with i = 3,
    # f2 is the first number and f1 is the second one.
    f2 = 0
    f1 = 1

    # this loop finds period, if the period is found it returns ok status equal to True, length of cycle and periodic
    # array of reminders
    # but the loop is limited and period can not be found by the end of loop, in this case we return ok status set to
    # False and cycle parameter equal to needed reminder
    for i in range(2, number + 1):

        # adding new reminder
        d += '{},'.format(str((f2 + f1) % modulo))

        # increasing length of cycle
        cycle += 1

        # refreshes numbers
        f2, f1 = f1, (f2 + f1) % modulo

        # we will check for loop only if length of string is even
        if len(d) % 2 == 0:
            length = int(len(d) / 2)

            # checking if two parts of string is equal
            if d[0:length] == d[length:len(d)]:

                # if equal, then period is found, we can return the answer
                return {
                    'ok': True,
                    'cycle': int(cycle/2),
                    'arr': d.split(',')[0:int(cycle/2)]
                }
    return {
        'ok': False,
        'cycle': int(d.split(',')[-2])
    }


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

    # the period was not found, so result object contains answer
    if result['ok'] is False:
        return result['cycle']

    # the period was found, so we need to understand to which element in array of reminder fibonacci[number] is equal,
    # for this we calculates the reminder from division (number % result['cycle']) and uses as the needed index for
    # array of reminders
    n = number % result['cycle']
    return result['arr'][n]


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(opti_fibonacci(input_numbers[0], input_numbers[1]))
