from sys import setrecursionlimit

MINUTES = 24

orem_cost = [0, 0, 0]
claym_cost = [0, 0, 0]
obsm_cost = [0, 0, 0]
geom_cost = [0, 0, 0]

DP = None

def dp(i, ore, clay, obs, orem, claym, obsm, geom):
    if i == MINUTES:
        return 0

    key = (i, ore, clay, obs, orem, claym, obsm, geom)
    if key in DP:
        return DP[key]
    
    # Buy nothing
    best = geom + dp(i + 1, ore + orem, clay + claym, obs + obsm, orem, claym, obsm, geom)
    
    # Buy ore machine
    if ore >= orem_cost[0] and clay >= orem_cost[1] and obs >= orem_cost[2]:
        if orem + 1 <= max([orem_cost[0], claym_cost[0], obsm_cost[0], geom_cost[0]]):
            best = max(best, geom + dp(i + 1, ore - orem_cost[0] + orem, clay - orem_cost[1] + claym, obs - orem_cost[2] + obsm, orem + 1, claym, obsm, geom))

    # Buy clay machine
    if ore >= claym_cost[0] and clay >= claym_cost[1] and obs >= claym_cost[2]:
        if claym + 1 <= max([orem_cost[1], claym_cost[1], obsm_cost[1], geom_cost[1]]):
            best = max(best, geom + dp(i + 1, ore - claym_cost[0] + orem, clay - claym_cost[1] + claym, obs - claym_cost[2] + obsm, orem, claym + 1, obsm, geom))

    # Buy obsidian machine
    if ore >= obsm_cost[0] and clay >= obsm_cost[1] and obs >= obsm_cost[2]:
        if obsm + 1 <= max([orem_cost[2], claym_cost[2], obsm_cost[2], geom_cost[2]]):
            best = max(best, geom + dp(i + 1, ore - obsm_cost[0] + orem, clay - obsm_cost[1] + claym, obs - obsm_cost[2] + obsm, orem, claym, obsm + 1, geom))
    
    # Buy geode machine
    if ore >= geom_cost[0] and clay >= geom_cost[1] and obs >= geom_cost[2]:
        best = max(best, geom + dp(i + 1, ore - geom_cost[0] + orem, clay - geom_cost[1] + claym, obs - geom_cost[2] + obsm, orem, claym, obsm, geom + 1))

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
    answer = 0
    for i, line in enumerate(lines, 1):
        read_blueprint(line)
        DP = dict()
        best = dp(0, 0, 0, 0, 1, 0, 0, 0)
        print(f"BEST for blueprint {i}: {best}")
        quality = best * i
        answer += quality
    print(answer)