import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O((n + m) log(n + m))                  !**
# ---------------------------------------------------------------------
def solution_one(nums1: List[int], m: int, nums2: List[int], n: int) \
        -> List[int]:
    """Merge nums1 and nums2 into a single array sorted in ASC order.

    Examples:
        >>> solution_one([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
        >>> solution_one([1], 1, [], 0)
        [1]
        >>> solution_one([0], 0, [1], 1)
        [1]
        >>> solution_one([2, 0], 1, [1], 1)
        [1, 2]
    """
    for i in range(n):
        nums1[m] = nums2[i]
        m += 1
    nums1.sort()
    return nums1


# ---------------------------------------------------------------------
# Approach 2: Two Pointers. Time: O(n + m)                          !**
# ---------------------------------------------------------------------
def solution_two(nums1: List[int], m: int, nums2: List[int], n: int) \
        -> List[int]:
    """Merge nums1 and nums2 into a single array sorted in ASC order.

    Examples:
        >>> solution_two([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
        >>> solution_two([1], 1, [], 0)
        [1]
        >>> solution_two([0], 0, [1], 1)
        [1]
        >>> solution_two([2, 0], 1, [1], 1)
        [1, 2]
    """
    m -= 1
    n -= 1
    i = len(nums1) - 1
    while n >= 0:
        if m >= 0 and nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1
        i -= 1
    return nums1


if __name__ == '__main__':
    doctest.testmod()
