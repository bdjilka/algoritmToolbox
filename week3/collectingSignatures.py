# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def partition(nums, low, high):
    """
    Method to find new element that will divide list in two parts.
    Pivot determines as middle element. Through finding next pivot elements also swaps places if needed.
    :param nums: array of elements
    :param low: init index
    :param high: last index
    :return: index of next pivot element
    """
    pivot = nums[(low + high) // 2].start
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i].start < pivot:
            i += 1
        j -= 1
        while nums[j].start > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def sort_segments(segments):
    """
    Additional function to sort segments in ascending order by their start point.
    (Quick sort)
    """

    def _quick_sort(items, low, high):
        """
        Subsidiary function to provide recursion
        """
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(segments, 0, len(segments) - 1)
    return segments


def optimal_points(segments):
    """
    Implementation of signature collecting: it is needed to collect signatures from all tenants of a certain building.
    For each tenant, is known a period of time when he or she is at home. You would like to collect all signatures by
    visiting the building as few times as possible.
    The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is
    to mark as few points on a line as possible so that each segment contains at least one marked point.
    :param segments: set of segments of length from 1 to 100, each number lays in [0, 10**9]
    :return: array of points

    To solve this problem, we need firstly sort ascending segments by their start point. Then we remember start and end
    of first segment in array and find all next segment that has intersection with it. All these segments we can be able
    to visit at once. Then we mark as visited this segments and repeat this it until segments won't end.
    """
    segments = sort_segments(segments)
    points = []
    start = segments[0].start
    end = segments[0].end
    for s in segments:
        temp_start = max(start, s.start)
        temp_end = min(end, s.end)
        if temp_start <= temp_end:
            start = temp_start
            end = temp_end
        else:
            points.append(end)
            start = s.start
            end = s.end
    points.append(end)
    return points


if __name__ == '__main__':
    """
    Input sample:
    3           # number of segments (in this sample 3)
    1 3         # coordinates of endpoint of the first segments
    2 5         # coordinates of endpoint of the second segments
    3 6         # coordinates of endpoint of the last segments
    """
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments_array = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments_array)
    print(len(points))
    for p in points:
        print(p, end=' ')
