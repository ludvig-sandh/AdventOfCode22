def get_val(grid, x, y):
    if (x, y) in grid:
        return grid[(x, y)]
    return None

def set_val(grid, x, y, val):
    grid[(x, y)] = val

with open("in.txt", "r") as f:
    grid = {}
    for line in f.read().split("\n"):
        l = [[int(i.split(",")[0]), int(i.split(",")[1])] for i in line.split(" -> ")]
        for i in range(len(l) - 1):
            x, y = l[i]
            while x != l[i + 1][0] or y != l[i + 1][1]:
                set_val(grid, x, y, "#")
                if l[i + 1][0] != l[i][0]:
                    dx = l[i + 1][0] - l[i][0]
                    dx //= abs(dx)
                    x += dx
                else:
                    dy = l[i + 1][1] - l[i][1]
                    dy //= abs(dy)
                    y += dy
            set_val(grid, x, y, "#")
    ans = 0
    while True:
        ans += 1
        # let sand fall
        sx, sy = 500, 0
        while True:
            under = get_val(grid, sx, sy + 1)
            if under is None:
                sy += 1
            elif under in "#o":
                below_left = get_val(grid, sx - 1, sy + 1)
                if below_left is not None and below_left in "#o":
                    below_right = get_val(grid, sx + 1, sy + 1)
                    if below_right is not None and below_right in "#o":
                        set_val(grid, sx, sy, "o")
                        break
                    else:
                        sx += 1
                        sy += 1
                else:
                    sx -= 1
                    sy += 1
            if sy > 1000:
                print(ans - 1)
                exit(0)