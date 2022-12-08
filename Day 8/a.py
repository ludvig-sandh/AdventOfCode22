def get_matrix():
    with open("in.txt", "r") as f:
        content = f.read()
        matrix = content.split("\n")
        return matrix

def get_visible(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visible = [[] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            visible[r].append(0)

    for r in range(rows):
        lastheight = -1
        for c in range(cols):
            if int(matrix[r][c]) > lastheight:
                lastheight = int(matrix[r][c])
                visible[r][c] = 1

    for r in range(rows):
        lastheight = -1
        for c in range(cols -1, -1, -1):
            if int(matrix[r][c]) > lastheight:
                lastheight = int(matrix[r][c])
                visible[r][c] = 1

    for c in range(cols):
        lastheight = -1
        for r in range(rows):
            if int(matrix[r][c]) > lastheight:
                lastheight = int(matrix[r][c])
                visible[r][c] = 1

    for c in range(cols):
        lastheight = -1
        for r in range(rows - 1, -1, -1):
            if int(matrix[r][c]) > lastheight:
                lastheight = int(matrix[r][c])
                visible[r][c] = 1

    return sum([sum(row) for row in visible])
        

def main():
    matrix = get_matrix()
    ans = get_visible(matrix)
    print(ans)

main()