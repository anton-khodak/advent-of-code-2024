l1 = []
l2 = []
with open("input.txt") as f:
    for line in f:
        el1, el2 = line.strip("\n").split("  ")
        l1.append(int(el1))
        l2.append(int(el2))
print(l1)
print(l2)

l1.sort()
l2.sort()

res = sum(abs(a - b) for a, b in zip(l1, l2))
print(res)
