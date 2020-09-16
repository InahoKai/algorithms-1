from typing import List

# Apparently the known dict is called a hashmap
# Faster than 91.23% on leetcode


def numIdenticalPairs(nums: List[int]) -> int:
    known = {}
    pairs = 0
    for num in nums:
        if num in known:
            pairs += known[num]
            known[num] += 1
        else:
            known[num] = 1
    return pairs


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))