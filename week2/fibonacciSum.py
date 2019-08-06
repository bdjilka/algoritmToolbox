# python3


def findCycle(number):
    cycle = 2
    d = '0,1,'
    f2 = 0
    f1 = 1
    for i in range(2, number + 3):
        d += '{},'.format(str((f2 + f1) % 10))
        cycle += 1
        f2, f1 = f1, (f2 + f1) % 10
        if len(d) % 2 == 0:
            length = int(len(d) / 2)
            if d[0:length] == d[length:len(d)]:
                return {'ok': True, 'cycle': int(cycle/2), 'arr': d.split(',')[0:int(cycle/2)]}
    return {'ok': False, 'cycle': int(d.split(',')[-2])}


def sum(number):
    if number < 2:
        return number

    result = findCycle(number)
    if result['ok'] is False:
        return (result['cycle'] - 1) % 10

    n = number % result['cycle']
    return (int(result['arr'][n + 2]) - 1) % 10


if __name__ == '__main__':
    input_number = int(input())
    print(sum(input_number))
