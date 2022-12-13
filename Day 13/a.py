import ast

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
        items.append([get_list(lines[i]), get_list(lines[i + 1])])
        
    ans = 0
    for i in range(len(items)):
        fix(*items[i])
        if items[i][0] <= items[i][1]:
            ans += i + 1
    print(ans)