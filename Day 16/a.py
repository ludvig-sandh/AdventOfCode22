# 11:14-11:21, 11:30-
G = {}
relevant_valves = {}
rates = {}

MINUTES = 30

def get_bitmask_pos(valve):
    return 1 << relevant_valves[valve]

def valve_opened(valve, bitmask):
    return bitmask & (1 << relevant_valves[valve])

DP = None
def dp(valve, minutes_left, bitmask):
    if minutes_left == 0:
        return 0

    if valve in DP[bitmask][minutes_left]:
        return DP[bitmask][minutes_left][valve]
    
    best = -1
    found = False
    for nei in G[valve]:
        found = True
        best = max(best, dp(nei, minutes_left - 1, bitmask))
    if valve in relevant_valves and not valve_opened(valve, bitmask):
        found = True
        best = max(best, rates[valve] * (minutes_left - 1) + dp(valve, minutes_left - 1, bitmask | get_bitmask_pos(valve)))
    DP[bitmask][minutes_left][valve] = best
    return best

with open("in.txt", "r") as f:
    lines = f.read().split("\n")

    for line in lines:
        node = line[6:8]
        rate = int(line[23:line.find(";")])
        others_start_index = line.find("valves") + 7
        if others_start_index - 7 == -1:
            others_start_index = line.find("valve") + 6
        others = line[others_start_index:].split(", ")
        
        rates[node] = rate
        if node not in G:
            G[node] = []
        for other in others:
            if other not in G:
                G[other] = []
            G[node].append(other)
        if rate != 0:
            relevant_valves[node] = len(relevant_valves)

    DP = [[{} for _ in range(MINUTES + 1)] for _ in range((1 << 16) - 1)]
    
    print(dp("AA", MINUTES, 0))