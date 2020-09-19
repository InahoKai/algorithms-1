from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i, j in zip(nums[:n], nums[n:]):
        res += [i, j]
    return res
