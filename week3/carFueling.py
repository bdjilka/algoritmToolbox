# python3
import sys


def compute_min_refills(distance, tank, n, stops):
    """
    Implementation of car fueling problem. When you need to travel 'distance' miles, your machine can go 'tank' miles
    and the stop locations are mentioned an 'stops' array. The goal is to make minimum amount of stops.

    To solve these problem used next greedy algorithm. We find the furthest stop, that is less then 'tank', this is
    the first stop. After that we can assume that it is the start of travel, where we need to go 'distance - first
    stop' miles and array of stops now starts not from index 0, but from index of first stop. So we repeat it untill
    won't reach destination point or if it is impossible

    :param distance: integer, [1, 10**5]
    :param tank: integer, [1, 400]
    :param n: integer, number of stops, [1, 300]
    :param stops: array of integers in range of [1, 300], 0 < stops[0] < stops[1] <...< stops[len(stops) -1] < distance
    :return: number of refills or -1 if it is impossible
    """
    count = 0
    current = 0

    stops.insert(0, 0)
    stops.append(distance)

    while current <= n:
        last = current
        while current <= n and stops[current + 1] - stops[last] <= tank:
            current += 1
        if current == last:
            return -1
        if current <= n:
            count += 1
    return count


if __name__ == '__main__':
    """
    Input sample:
    950                 # distance
    400                 # tank
    4                   # number of spots
    200 375 550 750     # spots array
    """
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))
