from pprint import pprint


trails = []
with open("input.txt") as f:
    for line in f:
        trails.append([int(x) for x in line if x != "\n"])

n_trails = [[0 for x in range(len(trails))] for y in range(len(trails))]

def start_search(i, j, prev) -> int:
    if i < 0 or i >= len(trails) or j < 0 or j >= len(trails):
        return 0
    cur = trails[i][j]
    if cur != prev + 1:
        return 0
    if n_trails[i][j] != 0:
        return 0
    if cur == 9:
        n_trails[i][j] = 1
        return 1
    right = start_search(i, j+1, cur)
    n_trails[i][j] += right
    left = start_search(i, j-1, cur) 
    n_trails[i][j] += left
    bottom = start_search(i+1, j, cur) 
    n_trails[i][j] += bottom
    up = start_search(i-1, j, cur) 
    n_trails[i][j] += up
    return n_trails[i][j]

res = 0
for i, row in enumerate(trails):
    for j, start in enumerate(row):
        if start == 0:
            res += start_search(i, j, -1)
            # pprint(n_trails)
            n_trails = [[0 for x in range(len(trails))] for y in range(len(trails))]

count = 0
for i, row in enumerate(trails):
    for j, start in enumerate(row):
        if start == 0:
            count += n_trails[i][j]
            # print(n_trails[i][j])

# pprint(n_trails)
print(res)

