from collections import defaultdict
from itertools import combinations
from typing import Tuple, Optional

coords = defaultdict(list)
flen = 0
with open("input.txt") as f:
    for i, line in enumerate(f):
        flen = len(line)
        for j, ch in enumerate(line):
            if ch != "." and ch != "\n":
                coords[ch].append((i, j))

print(coords)
print(f"len: {flen}")

def antinodes(a, b) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
    diff_x = b[0] - a[0]
    diff_y = b[1] - a[1]
    print(f"a: {a}, b: {b}")
    left = (a[0] - diff_x, a[1] - diff_y)
    print(f"left: {left}")
    if (left[0] < 0 or left[0] >= flen) or (left[1] < 0 or left[1] >= flen):
        left = None
    right = (b[0] + diff_x, b[1] + diff_y)
    print(f"right: {right}")
    if (right[0] < 0 or right[0] >= flen) or (right[1] < 0 or right[1] >= flen):
        right = None
    return left, right

answers = set()
for freqs in coords.values():
    combs = combinations(freqs, 2)
    for comb in combs:
        if comb is not []:
            left, right = antinodes(comb[0], comb[1])
            if left is not None:
                answers.add(left)
            if right is not None:
                answers.add(right)

print(answers)
print(len(answers))


