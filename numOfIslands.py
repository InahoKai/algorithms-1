from typing import List
import itertools as it


def numIslands(grid: List[List[str]]):
    if not grid:
        return 0
    count = 0

    def dfs(row, col, g):
        s = [(row, col)]
        while s:
            r, c = s.pop()
            g[r][c] = 'v'
            if r - 1 >= 0 and g[r - 1][c] not in '0v':
                s.append((r - 1, c))
            if r + 1 < len(g) and g[r + 1][c] not in '0v':
                s.append((r + 1, c))
            if c - 1 >= 0 and g[r][c - 1] not in '0v':
                s.append((r, c - 1))
            if c + 1 < len(g[0]) and g[r][c + 1] not in '0v':
                s.append((r, c + 1))
        return g

    for r, c in it.product(range(len(grid)), range(len(grid[0]))):
        if grid[r][c] == '1':
            grid = dfs(r, c, grid)
            count += 1
    return count


input_grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(input_grid))
