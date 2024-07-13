import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  !!!
# ---------------------------------------------------------------------
def solution(gas: List[int], cost: List[int]) -> int:
    """There are n gas stations along a circular route, where the amount
    of gas at the i-th station is gas[i]. It costs cost[i] of gas to
    travel from the i-th station to the next (i + 1)-th station. Return
    the starting gas station's index if you can travel around the
    circuit once in the clockwise direction, otherwise return -1.

    Examples:
        >>> solution([2, 3, 4], [3, 4, 3])
        -1
        >>> solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        3
        >>> solution([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])
        4
        >>> solution([3, 1, 1], [1, 2, 2])
        0
        >>> solution([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9])
        -1
    """
    res = curr_gain = total_gain = 0
    for i in range(len(gas)):
        curr_gain += gas[i] - cost[i]
        total_gain += gas[i] - cost[i]
        if curr_gain < 0:
            res = i + 1
            curr_gain = 0
    return res if total_gain >= 0 else -1


if __name__ == '__main__':
    doctest.testmod()