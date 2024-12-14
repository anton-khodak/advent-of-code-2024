import numpy as np
import math
import re
from collections import namedtuple

games = []
game  = namedtuple("game", ["a", "b", "prize"])
with open('input.txt') as f:
    a = None
    b = None
    prize = None
    for i, line in enumerate(f):
        if i % 4 == 0:
            a = tuple(int(x) for x in re.findall("\d+", line))
        elif i % 4 == 1:
            b = tuple(int(x) for x in re.findall("\d+", line))
        elif i % 4 == 2:
            prize = tuple(int(x) for x in re.findall("\d+", line))
        else:
            games.append(game(a, b, prize))
# print(games)
res = 0
for g in games:
    arr1 = np.array([ [g.a[0], g.b[0]],
                     [g.a[1], g.b[1]]])
    arr2 = np.array([g.prize[0], g.prize[1]])
    coords = np.linalg.solve(arr1, arr2)
    if len(coords) == 2:
        # print(coords[1])
        # print(math.isclose(round(coords[1]), coords[1], rel_tol=1e-06))
        if coords[0] > 0 and coords[1] > 0 and math.isclose(round(coords[0]), coords[0], rel_tol=1e-06) and math.isclose(round(coords[1]), coords[1], rel_tol=1e-06):
            res += 3 * coords[0] + coords[1]
        # print(res)

print(res)
