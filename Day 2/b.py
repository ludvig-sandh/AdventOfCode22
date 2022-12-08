def score(abc, xyz):
    res = 0
    if xyz == "X":
        res = 1
    elif xyz == "Y":
        res = 2
    elif xyz == "Z":
        res = 3
    if abc == "A" and xyz == "X" or abc == "B" and xyz == "Y" or abc == "C" and xyz == "Z":
        res += 3
    if abc == "A" and xyz == "Y" or abc == "B" and xyz == "Z" or abc == "C" and xyz == "X":
        res += 6
    return res

ans = 0
with open("in.txt", "r") as f:
    f = f.read().split("\n")
    for ff in f:
        ans += score(ff[0], ff[2])
print(ans)


