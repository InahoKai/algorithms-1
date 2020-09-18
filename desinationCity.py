from typing import List
# Runtime: 48 ms, faster than 95.59% of Python3 online submissions for Destination City.


def destCity(paths: List[List[str]]) -> str:
    d = {}
    for path in paths:
        src = path[0]
        dst = path[1]
        d[src] = dst
    for k, v in d.items():
        if v not in d:
            return v


print(destCity([["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]))
