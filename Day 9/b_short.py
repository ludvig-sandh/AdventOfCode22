with open("in.txt", "r") as f:
    visited, knots = set(), [[0, 0] for _ in range(10)]
    ds = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    for line in f.read().split("\n"):
        d, a = line.split()[0], int(line.split()[1])
        for _ in range(a):
            knots[9] = [a + b for a, b in zip(knots[9], ds[d])]
            for i in range(8, -1, -1):
                if not (abs(knots[i + 1][0] - knots[i][0]) <= 1 and abs(knots[i + 1][1] - knots[i][1]) <= 1):
                    dx, dy = knots[i + 1][0] - knots[i][0], knots[i + 1][1] - knots[i][1]
                    knots[i][0] += dx // abs(dx) if dx != 0 else 0
                    knots[i][1] += dy // abs(dy) if dy != 0 else 0
            visited.add(tuple(knots[0]))
    print(len(visited))