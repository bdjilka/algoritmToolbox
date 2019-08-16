# python3
import random
import sys


def get_majority_element(a, left, right):
    """
    Realization of majority element problem.
    Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the
    votes. Given a sequence of elements a1, a2, ..., an, you would like to check whether it contains an element that
    appears more than n/2 times.

    :param a: array of votes
    :param left: left bound index
    :param right: right bound index
    :return: majority element or -1 if there is not such

    Algorithm based on divide and conquer approach. We divide sequence on half, search majority elements in each half
    and then merges results.
    If array consists of one element, element is returned. If there is more elements, then we analyse majority elements
    of both parts:
    -- left and right parts do not have majority elements -> there is no majority elements
    -- only left or right part has majority element -> we count if this element is majority for whole array
    -- both parts has its own majority -> count which element has more entries (more than half also) and returns it
    """
    if left == right:
        return a[left]

    left_majority = get_majority_element(a, left, (left + right) // 2)
    right_majority = get_majority_element(a, (left + right) // 2 + 1, right)

    if left_majority == -1 and right_majority == -1:
        return -1

    if left_majority >= 0 and right_majority == -1 or right_majority >= 0 and left_majority == -1:
        count = 0
        if left_majority == -1:
            majority = right_majority
        else:
            majority = left_majority
        for i in range(left, right + 1):
            if a[i] == majority:
                count += 1
        if count > (right - left + 1) // 2:
            return majority
        else:
            return -1

    count_left = 0
    count_right = 0
    for i in range(left, right + 1):
        if a[i] == left_majority:
            count_left += 1
        if a[i] == right_majority:
            count_right += 1
    if count_left > count_right:
        if count_left > (right - left + 1) // 2:
            return left_majority
        else:
            return -1
    if count_right > (right - left + 1) // 2:
        return right_majority
    else:
        return -1


def majority_naive(a):
    """
    Naive implementation. Complexity is O(n^2) instead of O(nlog(n)).
    :param a:
    :return:
    """
    for i in range(len(a)):
        cur = a[i]
        count = 0
        for j in range(len(a)):
            if a[j] == cur:
                count += 1
        if count > len(a) // 2:
            return cur
    return -1


if __name__ == '__main__':
    """
    Input example:
    5
    2 3 9 2 2
    
    The first line contains an integer n (from 1 to 10**5), the next one contains a sequence of n non-negative integers
    (each from 1 to 10**9).
    """
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)

    # print(get_majority_element([5, 0, 0, 3, 2, 0, 0], 0, 6))

    # while True:
    #     n = random.randint(1, 100)
    #     a = [random.randint(0, 2) for i in range(n)]
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     a[random.randint(0, n-1)] = 2
    #     res1 = majority_naive(a)
    #     res2 = get_majority_element(a, 0, n - 1)
    #     print(a)
    #     print(res1)
    #     print(res2)
    #     if res1 != res2:
    #         break
