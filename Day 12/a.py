from queue import Queue

with open("in.txt", "r") as f:
    content = f.read().split("\n")
    content = [list(i) for i in content]
    G = [[] for _ in range(len(content) * len(content[0]))]

    start = None
    goal = None
    for r in range(len(content)):
        for c in range(len(content[0])):
            if content[r][c] == 'S':
                content[r][c] = 'a'
                start = r * len(content[0]) + c
            elif content[r][c] == 'E':
                content[r][c] = 'z'
                goal = r * len(content[0]) + c

    for r in range(len(content)):
        for c in range(len(content[0])):
            dxs = [1, 0, -1, 0]
            dys = [0, 1, 0, -1]
            for i in range(4):
                nr, nc = r + dys[i], c + dxs[i]
                if nr < 0 or nc < 0 or nr >= len(content) or nc >= len(content[0]):
                    continue
                if ord(content[nr][nc]) - ord(content[r][c]) <= 1:
                    G[r * len(content[0]) + c].append(nr * len(content[0]) + nc)
    path = [["." for _ in range(len(content[0]))] for _ in range(len(content))]
    visited = [False for _ in range(len(content) * len(content[0]))]
    q = Queue()
    q.put((start, 0, -1))
    while q.qsize() > 0:
        front, dist, last = q.get()
        if visited[front]:
            continue
        visited[front] = 1
        if front == goal:
            print(dist)
            break
        for nei in G[front]:
            q.put((nei, dist + 1, front))
