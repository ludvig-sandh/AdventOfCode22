rocks = [
    [
        [1, 1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]

NUM_DROPS = 2022
WIDTH = 7
board = [[0 for _ in range(7)] for _ in range(NUM_DROPS * 4)]

def get_positions(place_x, place_y, rock_index):
    global rocks
    rock_positions = []
    for y in range(len(rocks[rock_index])):
        rock_y = []
        for x in range(len(rocks[rock_index][y])):
            if rocks[rock_index][y][x] == 1:
                rock_y.append([place_x + x, place_y - y])
        rock_positions.append(rock_y)
    return rock_positions

def update_positions(rock_positions, dx, dy):
    for y in range(len(rock_positions)):
        for x in range(len(rock_positions[y])):
            rock_positions[y][x][0] += dx
            rock_positions[y][x][1] += dy
    return rock_positions

def check_overlap(rock_positions, board):
    for i in range(len(rock_positions)):
        for j in range(len(rock_positions[i])):
            x, y = rock_positions[i][j]
            if x < 0 or x >= WIDTH:
                return True
            if y < 0:
                return True
            if board[y][x] == 1:
                return True
    return False

def get_highest(board):
    for y in range(len(board) - 1, -1, -1):
        if sum(board[y]) != 0:
            return y
    return -1

def get_dx(direction):
    dxs = {
        '>': 1,
        '<': -1
    }
    return dxs[direction]

def save_positions(rock_positions, board):
    for i in range(len(rock_positions)):
        for j in range(len(rock_positions[i])):
            x, y = rock_positions[i][j]
            assert(board[y][x] == 0)
            board[y][x] = 1

with open("in.txt", "r") as f:
    winds = f.read()
    j = 0
    for i in range(NUM_DROPS):
        highest = get_highest(board)
        rock_positions = get_positions(2, highest + 3 + len(rocks[i % len(rocks)]), i % len(rocks))
        while True:
            rock_positions = update_positions(rock_positions, get_dx(winds[j % len(winds)]), 0)
            if check_overlap(rock_positions, board):
                rock_positions = update_positions(rock_positions, -get_dx(winds[j % len(winds)]), 0)
            j += 1

            rock_positions = update_positions(rock_positions, 0, -1)
            if check_overlap(rock_positions, board):
                rock_positions = update_positions(rock_positions, 0, 1)
                break
        save_positions(rock_positions, board)
    print(get_highest(board) + 1)