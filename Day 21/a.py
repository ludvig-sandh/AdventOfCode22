from dataclasses import dataclass
from typing import List, Dict

def plus(this, other):
    return this + other

def minus(this, other):
    return this - other

def mult(this, other):
    return this * other

def div(this, other):
    return this // other

def identity(this, other):
    return this

@dataclass
class Monkey:
    result: int
    operation: str
    operator1: str
    operator2: str

@dataclass
class Monkeys:
    monkeys: Dict[str, Monkey]

    def compute_monkey(self, monkey_name):
        if monkey_name not in self.monkeys:
            return int(monkey_name)
        monkey = self.monkeys[monkey_name]
        if monkey.result != None:
            return monkey.result

        functions = {
            "+": plus,
            "-": minus,
            "*": mult,
            "/": div,
            " ": identity
        }
        
        monkey.result = functions[monkey.operation](
            self.compute_monkey(monkey.operator1),
            self.compute_monkey(monkey.operator2)
            )
        return monkey.result

    def add_monkey(self, name, monkey):
        assert(name not in self.monkeys)
        self.monkeys[name] = monkey

monkeys = Monkeys(dict())

with open("in.txt", "r") as f:
    for line in f.read().split("\n"):
        name = line[:4]
        rest = line[6:]
        try:
            num = int(rest)
            # It's just a number
            operator1 = operator2 = int(rest)
            operation = " "
        except ValueError:
            operator1 = line[6:10]
            operation = line[11]
            operator2 = line[13:17]
        monkeys.add_monkey(name, Monkey(None, operation, operator1, operator2))

print(monkeys.compute_monkey("root"))