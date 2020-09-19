# Runtime: 28 ms, faster than 90.26% of Python3 online submissions for Power of Four.
def isPowerOfFour(num: int) -> bool:
    if num == 0:
        return False
    while num != 1:
        if num % 4 != 0:
            return False
        num = num // 4

    return True


print(isPowerOfFour(16))