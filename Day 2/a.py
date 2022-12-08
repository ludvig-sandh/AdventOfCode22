def lose(x):
    if x == "A":
        return 3
    if x == "B":
        return 1
    if x == "C":
        return 2

def win(x):
    if x == "A":
        return 2
    if x == "B":
        return 3
    if x == "C":
        return 1

def draw(x):
    if x == "A":
        return 1
    if x == "B":
        return 2
    if x == "C":
        return 3

    

def score(abc, xyz):
    res = 0
    if xyz == "X":
        res += lose(abc)
    if xyz == "Y":
        res += 3
        res += draw(abc)
    if xyz == "Z":
        res += 6
        res += win(abc)
    return res

ans = 0
with open("in.txt", "r") as f:
    f = f.read().split("\n")
    for ff in f:
        ans += score(ff[0], ff[2])
print(ans)


