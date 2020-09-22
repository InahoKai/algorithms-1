from typing import List


# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.
#
# What is the minimum candies you must give?


def candy(ratings: List[int]) -> int:
    res = [1] * len(ratings)
    lbase = rbase = 1

    for i in range(1, len(ratings)):
        lbase = lbase + 1 if ratings[i] > ratings[i - 1] else 1
        res[i] = lbase

    for i in range(len(ratings) - 2, -1, -1):
        rbase = rbase + 1 if ratings[i] > ratings[i + 1] else 1
        res[i] = max(rbase, res[i])

    return sum(res)


print(candy([1, 0, 2]))
