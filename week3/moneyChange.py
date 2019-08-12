# python3


def get_change(m):
    """
    Realization of money change elementary greedy algorithm.
    Returns the minimum number of coins needed to change the input value into coins with denominations 1, 5, and 10
    :param m: given money, integer from 1 to 1000
    :return: integer
    """
    # the point of algorithm is to give at most coins with denominations 10
    n10 = m // 10
    m -= 10 * n10
    # then give maximally possible number of coin with denominations of 5
    n5 = m // 5
    m -= 5 * n5
    # then reminder will be consist of coins with denominations 1
    return n10 + n5 + m


if __name__ == '__main__':
    moneyToChange = int(input())
    print(get_change(moneyToChange))
