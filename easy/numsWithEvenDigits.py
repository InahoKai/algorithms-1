from typing import List
# Runtime: 48 ms, faster than 94.59% of Python3 online submissions for Find Numbers with Even Number of Digits.


def findNumbers(nums: List[int]) -> int:
    count = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            count += 1
    return count


print(findNumbers([12, 345, 2, 6, 7896]))