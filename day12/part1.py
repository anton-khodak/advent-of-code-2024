from typing import Tuple
from copy import deepcopy

farm = []
with open("input.txt") as f:
    for line in f:
        farm.append(list(line.strip("\n")))

visited = deepcopy(farm)

def start_search(i, j, plot, tiles_n) -> Tuple[int, int]:
    if i < 0 or i >= len(farm) or j < 0 or j >= len(farm):
        return 0, 0
    if farm[i][j] != plot:
        return 0, 0
    if visited[i][j] == ".":
        return 0, -1
    visited[i][j] = "."
    walls_total = 0
    walls_tile = 4
    plots_total = 1
    for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        walls, plots = start_search(i+dir_x, j + dir_y, plot, 1) 
        walls_total += walls
        if plots != 0:
            walls_tile -= 1
        if plots != -1:
            plots_total += plots
    walls_total += walls_tile
    return walls_total, plots_total
        

res = 0
for i, row in enumerate(farm):
    for j, plot in enumerate(row):
        if visited[i][j] != ".":
            walls, tiles = start_search(i, j, plot, 1)
            print(f"plot: {plot}, walls {walls}, tiles {tiles}")
            res += walls * tiles

print(res)
