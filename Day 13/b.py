import ast
from copy import deepcopy

def get_list(text):
    return ast.literal_eval(text)

def fix(item1, item2):
    if type(item1) == int and type(item2) == int:
        return
    for i in range(len(item1)):
        if i >= len(item2):
            return
        if type(item1[i]) == list:
            if not type(item2[i]) == list:
                item2[i] = [item2[i]]
        elif type(item2[i]) == list:
            item1[i] = [item1[i]]
        fix(item1[i], item2[i])

with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    items = []
    for i in range(0, len(lines), 3):
        items.extend([get_list(lines[i]), get_list(lines[i + 1])])

    items.append([[2]])
    items.append([[6]])

    for i in range(len(items)):
        for j in range(len(items) - 1):
            item1, item2 = deepcopy(items[j]), deepcopy(items[j + 1])
            fix(item1, item2)
            if item1 > item2:
                items[j], items[j + 1] = items[j + 1], items[j]
    print((items.index([[2]]) + 1) * (items.index([[6]]) + 1))

# total: 49min