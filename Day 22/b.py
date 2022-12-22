from dataclasses import dataclass

class Grid:
    def __init__(self, board):
        self.board = []
        self.height = len(board)
        self.width = max([len(row) for row in board])
        for row in board:
            self.board.append("")
            for item in row:
                self.board[-1] += item
            for _ in range(max(0, self.width - len(row))):
                self.board[-1] += " "
        self.y = 0
        self.x = self.board[0].index('.')
        self.dx = 1
        self.dy = 0
        self.turns = ""

    def display(self):
        face = {(1, 0): '>', (0, 1): 'v', (-1, 0): '<', (0, -1): '^'}
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) == (self.y, self.x):
                    print(face[(self.dx, self.dy)], end="")
                else:
                    print(self.board[r][c], end="")
            print()


    def turn(self, direction):
        self.turns += direction
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] * 2
        if direction == 'R':
            self.dx, self.dy = directions[directions.index((self.dx, self.dy)) + 1]
        elif direction == 'L':
            self.dx, self.dy = directions[directions.index((self.dx, self.dy)) + 3]

    def go_forward(self):
        self.turns = ""
        nx, ny = self.x, self.y
        while True:
            nx, ny = nx + self.dx, ny + self.dy

            # x: 0, 50, 100, 150
            # y: 0, 50, 100, 150, 200

            if nx == 150 and ny <= 49: # Going off to right
                ny = 100 + (49 - ny)
                nx = 99
                self.turn("R")
                self.turn("R")
            elif nx == 100 and 50 <= ny <= 99:
                nx = 100 + (ny - 50)
                ny = 49
                self.turn("L")
            elif nx == 100 and 100 <= ny <= 149:
                ny = 149 - ny
                nx = 149
                self.turn("R")
                self.turn("R")
            elif nx == 50 and 150 <= ny <= 199:
                nx = 50 + (ny - 150)
                ny = 149
                self.turn("L")

            elif nx == 49 and ny <= 49: # Going off to left
                ny = 100 + (49 - ny)
                nx = 0
                self.turn("R")
                self.turn("R")
            elif nx == 49 and 50 <= ny <= 99:
                nx = ny - 50
                ny = 100
                self.turn("L")
            elif nx == -1 and 100 <= ny <= 149:
                ny = 149 - ny
                nx = 50
                self.turn("R")
                self.turn("R")
            elif nx == -1 and 150 <= ny <= 199:
                nx = 50 + (ny - 150)
                ny = 0
                self.turn("L")

            elif ny == 99 and nx <= 49: # Going off up
                ny = 50 + nx
                nx = 50
                self.turn("R")
            elif ny == -1 and 50 <= nx <= 99:
                ny = 100 + nx
                nx = 0
                self.turn("R")
            elif ny == -1 and 100 <= nx <= 149:
                nx = nx - 100
                ny = 199
            
            elif ny == 200 and nx <= 49: # Going off down
                nx += 100
                ny = 0
            elif ny == 150 and 50 <= nx <= 99:
                ny = 150 + (nx - 50)
                nx = 49
                self.turn("R")
            elif ny == 50 and 100 <= nx <= 149:
                ny = 50 + (nx - 100)
                nx = 99
                self.turn("R")

            if self.board[ny][nx] == '#':
                for direction in reversed(self.turns):
                    self.turn('L' if direction == 'R' else 'R')
                break
            elif self.board[ny][nx] == '.':
                self.x, self.y = nx, ny
                break
        
    def __perform_instruction(self, instruction):
        if instruction in "RL":
            self.turn(instruction)
            return
        for _ in range(int(instruction)):
            lx, ly = self.x, self.y
            self.go_forward()
            if (self.x, self.y) == (lx, ly):
                break

    def perform_instructions(self, instructions):
        for parts in instructions.split("R"):
            for j, forward_instruction in enumerate(parts.split("L")):
                self.__perform_instruction(forward_instruction)
                if j == len(parts.split("L")) - 1:
                    continue
                self.turn("L")
            self.turn("R")
        self.turn("L")

with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    stop = lines.index('')
    board = lines[:stop]
    instructions = lines[-1]

    grid = Grid(board)
    grid.display()

    grid.perform_instructions(instructions)

    face_score = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
    ans = 1000 * (grid.y + 1) + 4 * (grid.x + 1) + face_score[(grid.dx, grid.dy)]
    print(ans)

# total time: 1h 50m