from collections import defaultdict

with open("day5_input.txt") as f:
    data = f.read().splitlines()
# print(data)

rules = defaultdict(set)
updates = []
for line in data:
    if line == "":
        continue  
    elif "|" in line:
        first, second = line.split("|")
        rules[int(first)].add(int(second))
    else:
        updates.append(list(int(x) for x in line.split(',')))
# print(rules)
# print(updates)


def is_valid_update(update: list[int]) -> bool:
    for i, num in enumerate(update):
        j = 0
        while j < i:
            if update[j] in rules[num]:
                return False
            j += 1
    return True

res = 0
for update in updates:
    if is_valid_update(update):
        res += update[len(update) // 2]
print(res)


"""

"""

