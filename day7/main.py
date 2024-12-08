import operator
from itertools import product

equations = []
with open("input.txt") as f:
    for line in f:
        target, rest = line.split(":")
        equation = [int(target)]
        equation.extend(list(int(x) for x in rest.strip(" ").split(" ")))
        equations.append(equation)

answer = 0
for eq in equations:
    target = eq[0]
    products = list(product([operator.mul, operator.add], repeat=len(eq) - 1))
    for prod in products:
        res = 1
        for i, num in enumerate(eq[1:]):
            res = prod[i](res, num)
            if res > target:
                break
        if res == target:
            answer += target
            break

print(answer)

