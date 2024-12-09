
# with open("input.txt") as f:
#     s = f.readline().strip("\n")

s = "2333133121414131402"
# 2333133121414131402

res = 0
arr = []
counter = 0
for i, d in enumerate(s):
    if i % 2 == 0:
        arr.extend(list(counter for i in range(int(d))))
        counter += 1
    else:
        arr.extend(list("." for i in range(int(d))))


spaces = [int(x) for x in s if x % 2 == 1]
files = [int(x) for x in s if x % 2 == 0]

used = 0
last = len(files) - 1

while last > used:
    for i in range(used, last + 2):
        if spaces[i] >= files[last]:
            # decrease capacity
            spaces[i] -= files[last]
            # fill the array
            for j in range()


            if spaces[i] == 0:
                if i == used:
                    used += 1
            break
    last -= 1



# head = 0
# tail = len(arr) - 1
#
# while head < tail:
#     if arr[head] != ".":
#         head += 1
#         continue
#     if head >= tail:
#         break
#     while arr[tail] == ".":
#         tail -= 1
#     arr[head] = arr[tail]
#     tail -= 1
#
# res = 0
# for i in range(tail+1):
#    res += arr[i]*i 
# print(res)
# print(arr)
#
