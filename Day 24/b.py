from math import gcd
from heapq import *

def lcm(a,b):
    return (a * b) // gcd(a,b)

class Blizzard:
    def __init__(self, grid):
        self.height = len(grid)
        self.width = len(grid[0])
        self.states = []
        self.__precompute_states(grid)

    def __precompute_states(self, grid):
        self.num_states = lcm(self.height - 2, self.width - 2)
        arrows = {}
        dirs = {
            '>': [0, 1],
            'v': [1, 0],
            '<': [0, -1],
            '^': [-1, 0]
        }

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] in dirs.keys():
                    if (r, c) not in arrows:
                        arrows[(r, c)] = []
                    arrows[(r, c)].append(dirs[grid[r][c]])

        for i in range(self.num_states):
            state = [[0 for _ in range(self.width)] for _ in range(self.height)]
            for r in range(self.height):
                for c in range(self.width):
                    if r == 0 or c == 0 or r == self.height - 1 or c == self.width - 1:
                        if r == 0 and c == 1:
                            state[r][c] = 0
                        elif r == self.height - 1 and c == self.width - 2:
                            state[r][c] = 0
                        else:
                            state[r][c] = 1
                        continue
                    
                    if (r, c) in arrows:
                        state[r][c] = 1
            self.states.append(state)

            # Move blizzards
            new_arrows = {}
            for (r, c), ds in arrows.items():
                for dr, dc in ds:
                    nr = r + dr
                    nc = c + dc
                    if nr == 0:
                        nr = self.height - 2
                    elif nr == self.height - 1:
                        nr = 1
                    if nc == 0:
                        nc = self.width - 2
                    elif nc == self.width - 1:
                        nc = 1
                    if (nr, nc) not in new_arrows:
                        new_arrows[(nr, nc)] = []
                    new_arrows[(nr, nc)].append([dr, dc])
            arrows = new_arrows
            
    def search(self):
        pq = [[0, 0, 1, 0]]
        visited = set()
        while len(pq) != 0:
            d, r, c, g = heappop(pq)

            key = (d % self.num_states, r, c, g)
            if key in visited:
                continue
            visited.add(key)

            if r == self.height - 1 and c == self.width - 2:
                if g == 0:
                    g = 1
                if g == 2:
                    return d
            if r == 0 and c == 1:
                if g == 1:
                    g = 2

            dcs = [0, 1, 0, -1, 0]
            drs = [1, 0, -1, 0, 0]
            for i in range(5):
                nr = r + drs[i]
                nc = c + dcs[i]
                if nr == 0 or nc == 0 or nr == self.height - 1 or nc == self.width - 1:
                    if (nr != self.height - 1 or nc != self.width - 2) and (nr != 0 or nc != 1):
                        continue
                if nr < 0 or nr >= self.height:
                    continue
                if self.states[(d + 1) % self.num_states][nr][nc] == 1:
                    continue
                heappush(pq, [d + 1, nr, nc, g])
                
with open("in.txt", "r") as f:
    grid = f.read().split("\n")
blizzard = Blizzard(grid)
print(blizzard.search())

# Total time: 43min