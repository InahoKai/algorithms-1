from typing import List

# Runtime: 24 ms, faster than 99.86% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.8 MB, less than 67.72% of Python3 online submissions for Kids With the Greatest Number of Candies.


def kidsWithCandies(candies, extra) -> List[bool]:
    new = []
    biggest = max(candies)
    possible = biggest - extra
    print(possible)
    for i in candies:
        if i > possible:
            new.append(True)
        else:
            new.append(False)
    return new
