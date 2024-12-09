# s = "2333133121414131402"

with open("input.txt") as f:
    s = f.readline().strip("\n")

res = 0
arr = []
counter = 0
for i, d in enumerate(s):
    if i % 2 == 0:
        arr.extend(list(counter for i in range(int(d))))
        counter += 1
    else:
        arr.extend(list("." for i in range(int(d))))

head = 0
tail = len(arr) - 1

while head < tail:
    if arr[head] != ".":
        head += 1
        continue
    if head >= tail:
        break
    while arr[tail] == ".":
        tail -= 1
    arr[head] = arr[tail]
    tail -= 1

res = 0
for i in range(tail+1):
   res += arr[i]*i 
print(res)
