

# example = "125 17"
task = "4329 385 0 1444386 600463 19 1 56615"


blink = 1
arr = [int(x) for x in "0".split(" ")]
while blink < 76:
    new_arr = []
    for num in arr:
        if num == 0:
            new_arr.append(1)
        elif len(str(num)) % 2 == 0:
            mid = len(str(num)) // 2
            new_arr.extend([int(str(num)[:mid]), int(str(num)[mid:])])
        else:
            new_arr.append(num * 2024)
    arr = new_arr
    blink += 1
print(len(arr))
