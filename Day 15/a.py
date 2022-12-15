with open("in.txt", "r") as f:
    sensors = []
    beacons = []
    for line in f.read().split("\n"):
        sx = int(line[line.find("x=") + 2:line.find(",")])
        sy = int(line[line.find("y=") + 2:line.find(":")])
        line = line[line.find(":"):]
        bx = int(line[line.find("x=") + 2:line.find(",")])
        by = int(line[line.find("y=") + 2:])
        sensors.append((sx, sy))
        beacons.append((bx, by))
    
    intervals = {}
    for i in range(len(sensors)):
        dist = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
        for d in range(1, dist + 1):
            y1 = sensors[i][1] + d
            y2 = sensors[i][1] - d
            x1 = sensors[i][0] - dist + d
            x2 = sensors[i][0] + dist - d
            if y1 not in intervals:
                intervals[y1] = []
            if y2 not in intervals:
                intervals[y2] = []
            intervals[y1].append((x1, True))
            intervals[y1].append((x2, False))
            intervals[y2].append((x1, True))
            intervals[y2].append((x2, False))
        if sensors[i][1] not in intervals:
            intervals[sensors[i][1]] = []
        intervals[sensors[i][1]].append((sensors[i][0] - dist, True))
        intervals[sensors[i][1]].append((sensors[i][0] + dist, False))
    
    sums = {}
    for y in intervals:
        sums[y] = 0
        stack = []
        interval = sorted(intervals[y], key=lambda x: (x[0], not x[1]))
        for x, start in interval:
            if start:
                stack.append(x)
                continue
            top = stack.pop()
            if stack == []:
                sums[y] += x - top + 1
                for bx, by in beacons:
                    if by == y:
                        if top <= bx <= x:
                            sums[y] -= 1
                for sx, sy in sensors:
                    if sy == y:
                        if top <= sx <= x:
                            sums[y] -= 1
    print(sums[10])
        