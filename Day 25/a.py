from sys import setrecursionlimit
from math import log

digits = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

def to_dec(num):
    return sum([5 ** i * digits[c] for i, c in enumerate(num[::-1])])

def geometric_sum(a, k, n):
    return int(a * (1 - k ** n) / (1 - k))

def from_dec(i, left):
    if left < -geometric_sum(2, 5, i + 1):
        return None
    if left > geometric_sum(2, 5, i + 1):
        return None
    if i == -1 and left == 0:
        return ""
    if i < 0:
        return None

    for c, v in digits.items():
        res = from_dec(i - 1, left - v * 5 ** i)
        if res != None:
            return res + c

setrecursionlimit(1500000000)
with open("in.txt", "r") as f:
    ans = 0
    for line in f.read().split("\n"):
        ans += to_dec(line)
    limit = int(log(ans * 2, 5) + 1)
    out = from_dec(limit - 1, ans)
    print(out[::-1])

# Total time: 27min