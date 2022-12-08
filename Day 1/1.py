with open("in.txt", "r") as f:
    f = f.read().split("\n\n")
    a = [b.split("\n") for b in f]
    li = []
    for b in a:
        s = 0
        for c in b:
            s += int(c)
        li.append(s)
    li.sort()
    print(li[-1])
    print(li[-3] + li[-2] + li[-1])