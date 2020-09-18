# Runtime: 24 ms, faster than 94.17% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.6 MB, less than 92.63% of Python3 online submissions for Jewels and Stones.
def numJewelsInStones(J: str, S: str) -> int:
    J_set = set(J)
    return sum(item in J_set for item in S)


print(numJewelsInStones("aA", "aAAbbbb"))
