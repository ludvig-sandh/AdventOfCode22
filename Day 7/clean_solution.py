from sys import setrecursionlimit
from file_system import *

def get_instructions():
    with open("in.txt", "r") as f:
        content = f.read()
        lines = content.split("\n")
    return lines

def main():
    setrecursionlimit(1000000000)
    instructions = get_instructions()

    file_system = FileSystem()
    file_system.build_graph(instructions)
    file_system.evaluate_subtree_sizes_dfs(file_system.ROOT_DIR)
    print("A:", file_system.sum_sizes_dfs(file_system.ROOT_DIR, 100000))
    print("B:", file_system.find_smallest_enough(70000000, 30000000))

main()