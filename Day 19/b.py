from heapq import *
from dataclasses import dataclass

MINUTES = 32

orem_cost = [0, 0, 0]
claym_cost = [0, 0, 0]
obsm_cost = [0, 0, 0]
geom_cost = [0, 0, 0]

@dataclass
class State:
    i: int
    ore: int
    clay: int
    obs: int
    geo: int
    orem: int
    claym: int
    obsm: int
    geom: int

    def get_key(self):
        return (self.i, self.ore, self.clay, self.obs, self.geo, self.orem, self.claym, self.obsm, self.geom)

    def __lt__(self, other):
        return self.get_key() < other.get_key()

def calculate_priority(state: State) -> int:
    return -state.geom * 1000000 - state.obsm * 10000 - state.claym * 100 - state.orem - state.geo * 100000

def estimate_possible(state: State, max_geo) -> bool:
    return True

def astar():
    visited = set()
    pq = []
    start_state = State(0, 0, 0, 0, 0, 1, 0, 0, 0)
    heappush(pq, [0, start_state])
    max_geo = 0
    earliest = MINUTES
    while len(pq) != 0:
        _, state = heappop(pq)

        key = state.get_key()
        if key in visited: continue
        visited.add(key)

        i, ore, clay, obs, geo, orem, claym, obsm, geom = key
        if geo > max_geo:
            max_geo = geo
            print(f"New max geodes found: {max_geo, i}")
        if geo > 0 and i < earliest:
            earliest = i
            print(f"New earliest found: {earliest}")
        if i == MINUTES:
            continue

        if not estimate_possible(state, max_geo):
            continue

        # Buy nothing
        state_nothing = State(i + 1, ore + orem, clay + claym, obs + obsm, geo + geom, orem, claym, obsm, geom)
        heappush(pq, [calculate_priority(state_nothing), state_nothing])
        
        # Buy ore machine
        if ore >= orem_cost[0] and clay >= orem_cost[1] and obs >= orem_cost[2]:
            state_orem = State(i + 1, ore - orem_cost[0] + orem, clay - orem_cost[1] + claym, obs - orem_cost[2] + obsm, geo + geom, orem + 1, claym, obsm, geom)
            heappush(pq, [calculate_priority(state_orem), state_orem])

        # Buy clay machine
        if ore >= claym_cost[0] and clay >= claym_cost[1] and obs >= claym_cost[2]:
            state_claym = State(i + 1, ore - claym_cost[0] + orem, clay - claym_cost[1] + claym, obs - claym_cost[2] + obsm, geo + geom, orem, claym + 1, obsm, geom)
            heappush(pq, [calculate_priority(state_claym), state_claym])

        # Buy obsidian machine
        if ore >= obsm_cost[0] and clay >= obsm_cost[1] and obs >= obsm_cost[2]:
            state_obsm = State(i + 1, ore - obsm_cost[0] + orem, clay - obsm_cost[1] + claym, obs - obsm_cost[2] + obsm, geo + geom, orem, claym, obsm + 1, geom)
            heappush(pq, [calculate_priority(state_obsm), state_obsm])
        
        # Buy geode machine
        if ore >= geom_cost[0] and clay >= geom_cost[1] and obs >= geom_cost[2]:
            state_geom = State(i + 1, ore - geom_cost[0] + orem, clay - geom_cost[1] + claym, obs - geom_cost[2] + obsm, geo + geom, orem, claym, obsm, geom + 1)
            heappush(pq, [calculate_priority(state_geom), state_geom])

    return max_geo


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

with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    answer = 1
    for i, line in enumerate(lines[1:3], 1):
        read_blueprint(line)
        best = astar()
        print(f"BEST for blueprint {i}: {best}")
        answer *= best
    print(answer)

# 11
# 13
# 21