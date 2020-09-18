from typing import List
# Runtime: 24 ms, faster than 98.42% of Python3 online submissions for Create Target Array in the Given Order.


def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    new = []
    for i, val in enumerate(index):
        new.insert(val, nums[i])
    return new


print(createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
