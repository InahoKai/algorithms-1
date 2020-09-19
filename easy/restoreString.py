from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    A = [''] * len(s)
    for i, c in zip(indices, s):
        A[i] = c
    return "".join(A)


print(restoreString("codeleet", [4, 5, 6, 7, 0, 1, 2, 3]))
