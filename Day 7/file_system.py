class TreeItem:
    def __init__(self, size = 0):
        self.total_size = size
        self.children = []

    def add_child(self, absolute_path):
        self.children.append(absolute_path)

    def add_size(self, size):
        self.total_size += size

    def num_children(self):
        return len(self.children)

    def is_file(self):
        return self.num_children() == 0

class FileSystem:
    ROOT_DIR = "root"
    def __init__(self):
        self.directory_stack = []
        self.file_tree = dict()
        self.file_tree[self.ROOT_DIR] = TreeItem()

    def __abs_path(self, item_name):
        return self.directory_stack[-1] + "/" + item_name

    def __insert_item_in_tree(self, item_name, size):
        absolute_path = self.__abs_path(item_name)
        self.file_tree[self.directory_stack[-1]].add_child(absolute_path)
        self.file_tree[absolute_path] = TreeItem(size)

    def __read_cd_instruction(self, instruction):
        directory_name = instruction[5:]
        if directory_name == "/":
            self.directory_stack = [self.ROOT_DIR]
        elif directory_name == "..":
            self.directory_stack.pop()
        else:
            self.__insert_item_in_tree(directory_name, 0)
            self.directory_stack.append(self.__abs_path(directory_name))

    def __read_ls_instruction(self, instructions, i):
        num_ls_items = 0
        while instructions[i][0] != '$':
            instruction = instructions[i]
            if instruction[0:3] != "dir":
                filesize, filename = instruction.split(" ")
                self.__insert_item_in_tree(filename, int(filesize))
            num_ls_items += 1
            i += 1
            if i >= len(instructions):
                break
        return num_ls_items

    def build_graph(self, instructions):
        i = 0
        while i < len(instructions):
            instruction = instructions[i]
            if instruction[0] == '$':
                if instruction[2:4] == "cd":
                    self.__read_cd_instruction(instruction)
                elif instruction[2:4] == "ls":
                    num_ls_items = self.__read_ls_instruction(instructions, i + 1)
                    i += num_ls_items
            i += 1

    def evaluate_subtree_sizes_dfs(self, node):
        for child in self.file_tree[node].children:
            self.evaluate_subtree_sizes_dfs(child)
            self.file_tree[node].add_size(self.file_tree[child].total_size)

    def sum_sizes_dfs(self, node, threshold_size):
        result = 0
        if self.file_tree[node].total_size <= threshold_size and not self.file_tree[node].is_file():
            result += self.file_tree[node].total_size
        for child in self.file_tree[node].children:
            result += self.sum_sizes_dfs(child, threshold_size)
        return result

    def find_smallest_enough(self, MAX_SIZE, NEEDED_SIZE):
        current_size = self.file_tree[self.ROOT_DIR].total_size
        sizes = []
        for tree_item in self.file_tree.values():
            sizes.append(tree_item.total_size)
        sizes.sort()
        for size in sizes:
            if MAX_SIZE - (current_size - size) >= NEEDED_SIZE:
                return size
        return -1