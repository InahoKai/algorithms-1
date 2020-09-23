#
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to
# 65535).
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
# newColor, "flood fill" the image.
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
# of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the
# same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
# At the end, return the modified image.
#

from typing import List
# Runtime: 72 ms, faster than 95.26% of Python3 online submissions for Flood Fill.
# Memory Usage: 13.9 MB, less than 63.61% of Python3 online submissions for Flood Fill.


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    start = image[sr][sc]
    if start == newColor:
        return image

    def dfs(row, col, g):
        s = [(row, col)]
        while s:
            r, c = s.pop()
            g[r][c] = newColor
            if r - 1 >= 0 and g[r - 1][c] == start:
                s.append((r - 1, c))
            if r + 1 < len(g) and g[r + 1][c] == start:
                s.append((r + 1, c))
            if c - 1 >= 0 and g[r][c - 1] == start:
                s.append((r, c - 1))
            if c + 1 < len(g[0]) and g[r][  c + 1] == start:
                s.append((r, c + 1))
        return g

    return dfs(sr, sc, image)


print(floodFill([[2,2,2],[2,2,0],[2,0,1]], 1, 1, 2))
