with open("in.txt", "r") as f:
    xs = [1]
    for line in f.read().split("\n"):
        if line[0] == 'n':
            xs.append(xs[-1])
            continue
        
        dx = int(line.split(" ")[1])
        xs.append(xs[-1])
        xs.append(xs[-1] + dx)

    screen = [[] for _ in range(6)]
    for y in range(6):
        for x in range(40):
            i = y * 40 + x
            if abs(xs[i] - x) <= 1:
                screen[y].append("#")
            else:
                screen[y].append(".")
        screen[y] = "".join(screen[y])
        
    print(*screen, sep="\n")

# total time: 13min
