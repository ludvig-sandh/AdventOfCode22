from sys import setrecursionlimit

def get_instructions():
    with open("in.txt", "r") as f:
        content = f.read()
        lines = content.split("\n")
    return lines

def build_graph(instructions):
    graph = dict()
    stack = ["/"]
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction[0] == '$':
            if instruction[2:4] == "cd":
                to = instruction[5:]
                if to == "/":
                    stack = ["/"]
                elif to == "..":
                    stack.pop()
                else:
                    stack.append(stack[-1] + "/" + to)
            elif instruction[2:4] == "ls":
                i += 1
                while instructions[i][0] != '$':
                    next_instruction = instructions[i]
                    if next_instruction[0:3] == "dir":
                        directory_name = next_instruction[4:]
                        if stack[-1] not in graph:
                            graph[stack[-1]] = [0, []]
                        graph[stack[-1]][1].append(stack[-1] + "/" + directory_name)
                    else:
                        filesize, filename = next_instruction.split(" ")
                        if stack[-1] not in graph:
                            graph[stack[-1]] = [0, []]
                        graph[stack[-1]][1].append(stack[-1] + "/" + filename)
                        if filename not in graph:
                            graph[stack[-1] + "/" + filename] = [int(filesize), []]
                    i += 1
                    if i >= len(instructions):
                        break
                i -= 1
        i += 1
    return graph

def evaluate_subtree_sizes_dfs(graph, node):
    for neighbor in graph[node][1]:
        evaluate_subtree_sizes_dfs(graph, neighbor)
        graph[node][0] += graph[neighbor][0]

def sum_sizes_dfs(graph, node, threshold):
    result = 0
    if graph[node][0] <= threshold and len(graph[node][1]) != 0:
        result += graph[node][0]
    for neighbor in graph[node][1]:
        result += sum_sizes_dfs(graph, neighbor, threshold)
    return result

def main():
    setrecursionlimit(1000000000)
    instructions = get_instructions()
    graph = build_graph(instructions)
    evaluate_subtree_sizes_dfs(graph, "/")
    answer = sum_sizes_dfs(graph, "/", 100000)
    print(answer)

main()