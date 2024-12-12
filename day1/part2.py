from collections import Counter

l1 = []
l2 = []
with open("input.txt") as f:
    for line in f:
        el1, el2 = line.strip("\n").split("  ")
        l1.append(int(el1))
        l2.append(int(el2))

c = Counter(l2)
print(sum(x * c[x] for x in l1))
