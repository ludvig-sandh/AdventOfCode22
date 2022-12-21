from sys import setrecursionlimit
from math import ceil

MINUTES = 32

orem_cost = [0, 0, 0]
claym_cost = [0, 0, 0]
obsm_cost = [0, 0, 0]
geom_cost = [0, 0, 0]
robot_costs = [orem_cost, claym_cost, obsm_cost, geom_cost]

DP = None

def dp(i, ore, clay, obs, orem, claym, obsm, geom):
    if i >= MINUTES:
        return 0

    key = (i, ore, clay, obs, orem, claym, obsm, geom)
    if key in DP:
        return DP[key]

    best = 0
    robots = [orem, claym, obsm]

    for j in range(4):
        minutes_forward = max(1, 1 + max([ceil((robot_costs[j][0] - ore) / orem), (ceil((robot_costs[j][1] - clay) / claym) if claym != 0 else MINUTES) if robot_costs[j][1] != 0 else 0, (ceil((robot_costs[j][2] - obs) / obsm) if obsm != 0 else MINUTES) if robot_costs[j][2] != 0 else 0]))
        if j < 3 and robots[j] + 1 > max([orem_cost[j], claym_cost[j], obsm_cost[j], geom_cost[j]]): continue
        best = max(best, geom + dp(i + minutes_forward, ore - robot_costs[j][0] + orem * minutes_forward, clay - robot_costs[j][1] + claym * minutes_forward, obs - robot_costs[j][2] + obsm * minutes_forward, orem + (1 if j == 0 else 0), claym + (1 if j == 1 else 0), obsm + (1 if j == 2 else 0), geom + (1 if j == 3 else 0)))

    DP[key] = best
    return best

def read_robot(line, arr):
    char_to_index = {
        'or': 0,
        'cl': 1,
        'ob': 2
    }
    ore1_index = 0
    ore1_stop = ore1_index + line[ore1_index:].find(" ")
    arr[char_to_index[line[ore1_stop + 1:ore1_stop + 3]]] = int(line[ore1_index:ore1_stop])
    
    and_index = line[ore1_stop:].find("and")
    if and_index < 8 and and_index != -1:
        ore2_index = ore1_stop + line[ore1_stop:].find("and") + 4
        ore2_stop =  ore2_index + line[ore2_index:].find(" ")
        arr[char_to_index[line[ore2_stop + 1:ore2_stop + 3]]] = int(line[ore2_index:ore2_stop])

        if line[ore2_stop:].find("and") < 8 and line[ore2_stop:].find("and") != -1:
            ore3_index = line[ore2_stop:].find("and") + 4
            ore3_stop =  ore3_index + line[ore3_index:].find(" ")
            arr[char_to_index[line[ore3_stop + 1:ore3_stop + 3]]] = int(line[ore3_index:ore3_stop])

def read_blueprint(line):
    ORE_TEXT = "Each ore robot costs"
    CLAY_TEXT = "Each clay robot costs"
    OBSIDIAN_TEXT = "Each obsidian robot costs"
    GEODE_TEXT = "Each geode robot costs"

    ore_sentence = line[line.find(ORE_TEXT) + len(ORE_TEXT) + 1:]
    clay_sentence = line[line.find(CLAY_TEXT) + len(CLAY_TEXT) + 1:]
    obs_sentence = line[line.find(OBSIDIAN_TEXT) + len(OBSIDIAN_TEXT) + 1:]
    geo_sentence = line[line.find(GEODE_TEXT) + len(GEODE_TEXT) + 1:]
    read_robot(ore_sentence, orem_cost)
    read_robot(clay_sentence, claym_cost)
    read_robot(obs_sentence, obsm_cost)
    read_robot(geo_sentence, geom_cost)

setrecursionlimit(1000000000)
with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    answer = 1
    for i, line in enumerate(lines[:3], 1):
        read_blueprint(line)
        DP = dict()
        best = dp(0, 0, 0, 0, 1, 0, 0, 0)
        print(f"BEST for blueprint {i}: {best}")
        answer *= best
    print(answer)