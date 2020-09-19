# Runtime: 28 ms, faster than 80.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

def numberOfSteps(num: int) -> int:
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            count += 1
        if num % 2 != 0:
            num = num - 1
            count += 1
    return count


print(numberOfSteps(8))
