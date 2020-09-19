from typing import List
# Runtime: 32 ms, faster than 92.22% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
# Memory Usage: 13.8 MB, less than 75.02% of Python3 online submissions for Number of Students Doing Homework at a Given Time.


def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    count = 0
    for i, val in enumerate(startTime):
        if endTime[i] > queryTime > val:
            count += 1
    return count


print(busyStudent([1, 2, 3], [3, 2, 7], 4))
