from typing import List


def runningSum(nums: List[int]) -> List[int]:
    new = []

    currentVal = 0
    n = len(nums)
    for i in range(n):
        currentVal += nums[i]
        new.append(currentVal)

    return new


print(runningSum([1, 2, 3, 4]))
