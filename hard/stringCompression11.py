import collections

# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".
#
# Notice that in this problem, we are not adding '1' after single characters.
#
# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
#
# Find the minimum length of the run-length encoded version of s after deleting at most k characters.


def getLengthOfOptimalCompression(s: str, k: int) -> int:
    amounts = collections.Counter(s)
    new = []
    used = 0
    for key, val in amounts.items():
        if val != 1:
            new.append(key)
            new.append(str(val))
    return len(''.join(new))


print(getLengthOfOptimalCompression("aaabcccd", 2))