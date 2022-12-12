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
                goal = r * len(content[0]) + c
            elif content[r][c] == 'E':
                content[r][c] = 'z'
                start = r * len(content[0]) + c

    for r in range(len(content)):
        for c in range(len(content[0])):
            dxs = [1, 0, -1, 0]
            dys = [0, 1, 0, -1]
            for i in range(4):
                nr, nc = r + dys[i], c + dxs[i]
                if nr < 0 or nc < 0 or nr >= len(content) or nc >= len(content[0]):
                    continue
                if ord(content[r][c]) - ord(content[nr][nc]) <= 1:
                    G[r * len(content[0]) + c].append(nr * len(content[0]) + nc)
    path = [["." for _ in range(len(content[0]))] for _ in range(len(content))]
    dists = [-1 for _ in range(len(content) * len(content[0]))]
    q = Queue()
    q.put((start, 0, -1))
    while q.qsize() > 0:
        front, dist, last = q.get()
        if dists[front] != -1:
            continue
        dists[front] = dist
        for nei in G[front]:
            q.put((nei, dist + 1, front))
    ans = 10000000
    for r in range(len(content)):
        for c in range(len(content[0])):
            if content[r][c] == 'a':
                if dists[r * len(content[0]) + c] > -1:
                    ans = min(ans, dists[r * len(content[0]) + c])
    print(ans)

# Total time: 29min