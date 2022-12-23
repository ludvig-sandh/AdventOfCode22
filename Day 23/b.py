elves = set()
with open("in.txt", "r") as f:
    for r, line in enumerate(f.read().split("\n")):
        for c in range(len(line)):
            if line[c] == '#':
                elves.add((r, c))

order = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check_direction(direction, r, c):
    dr, dc = direction
    if dr == 0:
        for nr in range(r - 1, r + 2):
            if (nr, c + dc) in elves:
                return False
    elif dc == 0:
        for nc in range(c - 1, c + 2):
            if (r + dr, nc) in elves:
                return False
    return True

def count_ground():
    ir, ic = 1000000, 1000000
    ar, ac = -1000000, -1000000
    for (r, c) in elves:
        ir = min(ir, r)
        ic = min(ic, c)
        ar = max(ar, r)
        ac = max(ac, c)
    ans = 0
    for r in range(ir, ar + 1):
        for c in range(ic, ac + 1):
            if (r, c) not in elves:
                ans += 1
    return ans

NUM_ROUNDS = 10
current_round = 0
while True:
    wanted_moves = dict()
    for (r, c) in elves:
        no_elves = True
        for direction in order:
            if not check_direction(direction, r, c):
                no_elves = False
                break
        if no_elves:
            continue
        for direction in order:
            if check_direction(direction, r, c):
                key = (r + direction[0], c + direction[1])
                if key not in wanted_moves:
                    wanted_moves[key] = []
                wanted_moves[key].append((r, c))
                break
    
    if len(wanted_moves.keys()) == 0:
        print(current_round + 1)
        exit(0)

    for wanted_move, wanted_elves in wanted_moves.items():
        if len(wanted_elves) == 1:
            elves.remove(wanted_elves[0])
            elves.add(wanted_move)
    order = order[1:] + [order[0]]
    current_round += 1

# Total time: 22min