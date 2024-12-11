from collections import defaultdict

example = "125 17"
# task = "4329 385 0 1444386 600463 19 1 56615"


stages = defaultdict(dict)

stages[0][1] = 1


def num_of_children(num, target) -> int:
    if num in stages:
        if stages[num].get(target):
            return stages[num][target]
    if target == 1:
        if len(str(num)) % 2 == 0:
            stages[num][target] = 2
            return 2
        else:
            stages[num][target] = 1
            return 1

    if len(str(num)) % 2 == 0:
        mid = len(str(num)) // 2
        res = num_of_children(int(str(num)[:mid]), target - 1) + num_of_children(int(str(num)[mid:]), target - 1)
        stages[num][target] = res
        return res
    else:
        res = num_of_children(num * 2024, target - 1)
        stages[num][target] = res
        return res



arr = [int(x) for x in example.split(" ")]
print(sum(list(num_of_children(x, 6) for x in arr)))
