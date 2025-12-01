mat = []
with open("input.txt") as f:
    for line in f:
        mat.append([ch for ch in line if ch != "\n"])

m = 0
n = 0
dir_x = -1
dir_y = 0
for i, line in enumerate(mat):
    for j, ch in enumerate(line):
        if ch == "^":
            m = i
            n = j
            break

counter = 1
new_x = m + dir_x
new_y = n + dir_y
mat[m][n] = 'X'
while 0 <= new_x < len(mat) and 0 <= new_y < len(mat):
    ns = mat[new_x][new_y]
    print(f"mat[{new_x};{new_y}] == {ns}")
    if ns == "#":
        new_x -= dir_x
        new_y -= dir_y
        if dir_x != 0:
            new_dir_x = 0
        if dir_y == 0:
            new_dir_y = dir_x * (-1)
        if dir_x == 0:
            new_dir_x = dir_y
        if dir_y != 0:
            new_dir_y = 0
        dir_x = new_dir_x
        dir_y = new_dir_y
    elif ns != "X":
        counter += 1
        mat[new_x][new_y] = 'X'
    new_x += dir_x
    new_y += dir_y
print(counter)
