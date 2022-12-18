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

NUM_DROPS = 2022 * 10
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

def get_highest(board, last_highest):
    for y in range(last_highest + 5, -1, -1):
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
    highest = 0
    ans = []
    ans2 = []
    last_rows = None
    falls = []
    for i in range(NUM_DROPS * 1000):
        highest = get_highest(board, highest)
        if len(board) < highest + 100:
            for _ in range(100):
                board.append([0 for _ in range(WIDTH)])
        rock_positions = get_positions(2, highest + 3 + len(rocks[i % len(rocks)]), i % len(rocks))
        fall = 0
        while True:
            if j % len(winds) == 0:
                ans.append(highest + 1)
                ans2.append(i)
                falls.append(fall)
                if len(ans) == 14:
                    last_rows = board[highest - 20:highest + 1]
                    break
            fall += 1
            rock_positions = update_positions(rock_positions, get_dx(winds[j % len(winds)]), 0)
            if check_overlap(rock_positions, board):
                rock_positions = update_positions(rock_positions, -get_dx(winds[j % len(winds)]), 0)
            j += 1

            rock_positions = update_positions(rock_positions, 0, -1)
            if check_overlap(rock_positions, board):
                rock_positions = update_positions(rock_positions, 0, 1)
                break
        if last_rows != None:
            break
        else:
            save_positions(rock_positions, board)
    
    layers = ans
    dropped = ans2

    out = layers[1]
    num_drops_left = 1000000000000 - ans2[1] - ((1000000000000 - ans2[1]) // (ans2[2] - ans2[1])) * (ans2[2] - ans2[1])
    out += ((1000000000000 - ans2[1]) // (ans2[2] - ans2[1])) * (ans[2] - ans[1])
    board = last_rows
    highest = get_highest(board, len(board) - 6)
    start_highest = highest
    for _ in range(100):
        board.append([0 for _ in range(WIDTH)])

    j = -falls[-1]
    for i in range(num_drops_left):
        highest = get_highest(board, highest)
        if len(board) < highest + 100:
            for _ in range(100):
                board.append([0 for _ in range(WIDTH)])
        rock_positions = get_positions(2, highest + 3 + len(rocks[(i + 3) % len(rocks)]), (i + 3) % len(rocks))
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
    print((get_highest(board, highest) - start_highest) + out)