import re

# ex = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("day3_input.txt") as f:
    ex = f.read()

print(ex)


def answer(inp):
    ans = 0
    for pair in re.findall(r"mul\(\d+,\d+\)", inp):
        num1, num2 = pair[4:-1].split(",")
        ans += int(num1) * int(num2)
    return ans


print(answer(ex))
