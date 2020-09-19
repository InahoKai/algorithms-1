from typing import List
# Runtime: 80 ms, faster than 88.59% of Python3 online submissions for Sort Array By Parity.


def sortArrayByParity(A: List[int]) -> List[int]:
    new = []
    hold = []
    for num in A:
        if num % 2 == 0:
            new.append(num)
        else:
            hold.append(num)
    for i in hold:
        new.append(i)
    return new


print(sortArrayByParity([3, 1, 2, 4]))