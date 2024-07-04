import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: DP. Time: O(n)                                          !
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> bool:
    """You are initially positioned at the array's first index, and each
    element in the array represents your maximum jump length at that
    position. Return True if you can reach the last index, or False
    otherwise.

    Examples:
        # >>> solution([2, 3, 1, 1, 4])
        # True
        >>> solution([3, 2, 1, 0, 4])
        False
    """
    lastPos = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastPos:
            lastPos = i
    return lastPos == 0


if __name__ == '__main__':
    doctest.testmod()