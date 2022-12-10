with open("in.txt", "r") as f:
    xs = [1]
    for line in f.read().split("\n"):
        if line[0] == 'n':
            xs.append(xs[-1])
            continue
        
        dx = int(line.split(" ")[1])
        xs.append(xs[-1])
        xs.append(xs[-1] + dx)

    ans = 0
    for i in range(20, len(xs), 40):
        ans += xs[i - 1] * i
    print(ans)
