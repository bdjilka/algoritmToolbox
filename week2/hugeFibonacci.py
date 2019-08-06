# python3


def findCycle(number, modulo):
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
