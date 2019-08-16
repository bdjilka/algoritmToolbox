#python3
import sys


def binary_search(num, list):
    """
    Realization of binary search.
    :param num: integer from -10**8 to 10**8
    :param list: list of integers in range(-10**8, 10**8) [points]
    :return: index of element or index where it need to be inserted
    """
    left, right = 0, len(list) - 1
    while left <= right:
        middle = (right + left) // 2
        if num == list[middle]:
            return middle
        if num > list[middle]:
            left = middle + 1
        if num < list[middle]:
            right = middle - 1
    return left


def fast_count_segments(starts, ends, points):
    count = [0 for i in range(len(points))]

    segments_count = len(starts)
    for i in range(segments_count):
        begin = binary_search(starts[i], points)
        end = binary_search(ends[i], points)

        if begin >= 0 or end <= segments_count:
            for j in range(begin, end):
                count[j] += 1
    return count


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    """
    Input example:
    2 3         # number of segments and number of points (each from 1 to 50000)
    0 5         # first segment
    7 10        # second segment
    1 6 11      # points
    """
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]

    starts = [-10]
    ends = [10]
    points = [-100, 100, 0]

    # cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')
