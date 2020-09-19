from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    known = {}
    for i, num in enumerate(nums):
        if num in known:
            return [known[num], i]
        else:
            known[target - num] = i
