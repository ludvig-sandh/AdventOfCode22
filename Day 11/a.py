from dataclasses import dataclass
from queue import Queue

def plus(this, other):
    return this + other

def mult(this, other):
    return this * other

def square(this, other):
    return this * this

def double(this, other):
    return 2 * this

@dataclass
class Monkey:
    operation: int
    operator: int
    divisible: int
    true: int
    false: int
    iterations = 0

    def create(self):
        self.items = Queue()

    def consume_items(self):
        while not self.items.empty():
            front = self.items.get()
            front = self.operation(front, self.operator)
            front //= 3
            if front % self.divisible == 0:
                monkeys[self.true].items.put(front)
            else:
                monkeys[self.false].items.put(front)
            self.iterations += 1

monkeys = []

with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    for i in range(1, len(lines), 7):
        starting_items = [int(j) for j in lines[i][18:].split(", ")]
        operation = lines[i + 1][23]
        operator = lines[i + 1][25:]
        divisible = int(lines[i + 2][21:])
        true = int(lines[i + 3][29:])
        false = int(lines[i + 4][30:])
        monkey = None
        if operation == "*":
            if operator == "old":
                monkey = Monkey(square, 0, divisible, true, false)
            else:
                monkey = Monkey(mult, int(operator), divisible, true, false)
        elif operation == "+":
            if operator == "old":
                monkey = Monkey(double, 0, divisible, true, false)
            else:
                monkey = Monkey(plus, int(operator), divisible, true, false)
        monkey.create()
        for item in starting_items:
            monkey.items.put(item)
        monkeys.append(monkey)

NUM_ROUNDS = 20
for i in range(NUM_ROUNDS):
    for j, monkey in enumerate(monkeys):
        monkey.consume_items()

monkeys.sort(key=lambda x: x.iterations)
print(monkeys[-2].iterations * monkeys[-1].iterations)