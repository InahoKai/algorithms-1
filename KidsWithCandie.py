from typing import List

# Faster than 93% leetcode


def kidsWithCandies(candies, extra) -> List[bool]:
    new = []
    biggest = sorted(candies)[len(candies) - 1]
    possible = biggest - extra
    print(possible)
    for i in candies:
        if i > possible:
            new.append(True)
        else:
            new.append(False)
    return new
