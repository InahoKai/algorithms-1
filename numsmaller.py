from typing import List


def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    new = []
    current = 0
    for i in nums:
        for x in nums:
            if x < i:
                current += 1
        new.append(current)
        current = 0

    return new


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
