def is_adjacent(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def keep_up(head, tail):
    if is_adjacent(head, tail): return tail
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    tail[0] += dx // abs(dx) if dx != 0 else 0
    tail[1] += dy // abs(dy) if dy != 0 else 0
    return tail

with open("in.txt", "r") as f:
    visited = set()
    head, tail = [0, 0], [0, 0]
    ds = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}

    for line in f.read().split("\n"):
        d, a = line.split()[0], int(line.split()[1])
        for _ in range(a):
            head = [a + b for a, b in zip(head, ds[d])]
            tail = keep_up(head, tail)
            
            # Mark this place
            visited.add(tuple(tail))
    print(len(visited))