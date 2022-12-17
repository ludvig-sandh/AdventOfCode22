# 18:45 - 18:50

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
board = [[0 for _ in range(7)] for _ in range(NUM_DROPS * 4)]

def get_positions(place_x, place_y, rock_index):
    global rocks
    rock_positions = []
    for y in len(rocks[rock_index]):
        for x in len(rocks[rock_index][y]):


with open("in.txt", "r") as f:
    winds = f.read()
    print(winds)
    print(rocks[3])