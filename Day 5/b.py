def get_instructions(text):
    instructions = []
    text = text[text.index("m"):]
    for row in text.split("\n"):
        row = row.split(" ")
        instruction = [int(row[1]), int(row[3]) - 1, int(row[5]) - 1]
        instructions.append(instruction)
    return instructions

def get_boxes(text):
    boxes = []
    for row in text.split("\n"):
        if row == "" or row[0] == 'm':
            break
        brackets = [i for i, x in enumerate(row) if x == '[']
        for bracket in brackets:
            c = row[bracket + 1]
            index = (bracket + 1) // 4
            while index >= len(boxes):
                boxes.append([])
            boxes[index].append(c)
    return [list(reversed(box)) for box in boxes]

def perform_instructions(boxes, instructions):
    for amount, fr, to in instructions:
        move = boxes[fr][-amount:]
        boxes[fr] = boxes[fr][:-amount]
        boxes[to] += move
    result = "".join([box[-1] for box in boxes])
    return result

if __name__ == "__main__":
    with open("in.txt", "r") as f:
        text = f.read()
        boxes = get_boxes(text)
        instructions = get_instructions(text)
        result = perform_instructions(boxes, instructions)
        print(result)