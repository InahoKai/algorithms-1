# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
from typing import List
# Runtime: 520 ms, faster than 81.59% of Python3 online submissions for Island Perimeter.
# Memory Usage: 13.8 MB, less than 93.19% of Python3 online submissions for Island Perimeter.


def islandPerimeter(grid: List[List[int]]) -> int:
    count = 0
    for index, val in enumerate(grid):
        for xindex, xval in enumerate(val):
            sides = 4
            if xval == 1:
                if xindex > 0:
                    if val[xindex - 1] == 1:
                        sides -= 1
                if xindex < len(val) - 1:
                    if val[xindex + 1] == 1:
                        sides -= 1
                if index > 0:
                    if grid[index - 1][xindex] == 1:
                        sides -= 1
                if index < len(grid) - 1:
                    if grid[index + 1][xindex] == 1:
                        sides -= 1
                count += sides
    return count


print(islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
