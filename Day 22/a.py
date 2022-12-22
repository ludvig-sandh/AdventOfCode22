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

    def display(self):
        print(*self.board, sep="\n")

    def turn(self, direction):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] * 2
        if direction == 'R':
            self.dx, self.dy = directions[directions.index((self.dx, self.dy)) + 1]
        elif direction == 'L':
            self.dx, self.dy = directions[directions.index((self.dx, self.dy)) + 3]

    def go_forward(self):
        nx, ny = self.x, self.y
        while True:
            nx, ny = nx + self.dx, ny + self.dy
            if nx >= self.width:
                nx = 0
            elif nx < 0:
                nx = self.width - 1
            elif ny >= self.height:
                ny = 0
            elif ny < 0:
                ny = self.height - 1

            if self.board[ny][nx] == '#':
                break
            elif self.board[ny][nx] == '.':
                self.x, self.y = nx, ny
                break
        
    def __perform_instruction(self, instruction):
        if instruction in "RL":
            self.turn(instruction)
            return
        for _ in range(int(instruction)):
            self.go_forward()

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