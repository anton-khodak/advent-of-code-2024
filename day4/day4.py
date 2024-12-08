with open("day4_input.txt") as f:
    lines = f.readlines()

count = 0
for i, line in enumerate(lines):
    for j, ch in enumerate(line.strip("\n")):
        m = len(line.strip("\n"))
        if ch != "X":
            continue
        # dir right
        if j + 3 <= m and line[j + 1 : j + 4] == "MAS":
            count += 1
        # dir left
        if j - 3 >= 0 and line[j - 3 : j] == "SAM":
            count += 1
        # dir down
        print(f"{i} {j}")
        print(f"len {len(lines)} {m}")
        if (
            i + 3 < len(lines)
            and lines[i + 1][j] == "M"
            and lines[i + 2][j] == "A"
            and lines[i + 3][j] == "S"
        ):
            count += 1
        # dir up
        if (
            i - 3 >= 0
            and lines[i - 1][j] == "M"
            and lines[i - 2][j] == "A"
            and lines[i - 3][j] == "S"
        ):
            count += 1
        # dir up-right
        if (
            i - 3 >= 0
            and j + 3 < m
            and lines[i - 1][j + 1] == "M"
            and lines[i - 2][j + 2] == "A"
            and lines[i - 3][j + 3] == "S"
        ):
            count += 1
        # dir up-left
        if (
            i - 3 >= 0
            and j - 3 >= 0
            and lines[i - 1][j - 1] == "M"
            and lines[i - 2][j - 2] == "A"
            and lines[i - 3][j - 3] == "S"
        ):
            count += 1
        # down-right
        if (
            i + 3 < len(lines)
            and j + 3 < m
            and lines[i + 1][j + 1] == "M"
            and lines[i + 2][j + 2] == "A"
            and lines[i + 3][j + 3] == "S"
        ):
            count += 1
        # down-left
        if (
            i + 3 < len(lines)
            and j - 3 >= 0
            and lines[i + 1][j - 1] == "M"
            and lines[i + 2][j - 2] == "A"
            and lines[i + 3][j - 3] == "S"
        ):
            count += 1


print(count)
