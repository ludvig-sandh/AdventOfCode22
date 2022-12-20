nums = []

def move_left(index):
    global nums
    if index == 1:
        nums = [nums[0]] + nums[2:] + [nums[1]]
        return len(nums) - 1
    if index == 0:
        nums = nums[1:-1] + [nums[0]] + [nums[-1]]
        return len(nums) - 2
    nums[index], nums[index - 1] = nums[index - 1], nums[index]
    return index - 1

def move_right(index):
    global nums
    if index == len(nums) - 2:
        nums = [nums[-2]] + nums[:-2] + [nums[-1]]
        return 0
    if index == len(nums) - 1:
        nums = [nums[0]] + [nums[-1]] + nums[1:-1]
        return 1
    nums[index], nums[index + 1] = nums[index + 1], nums[index]
    return index + 1

def move(index):
    global nums
    if nums[index][1] < 0:
        for _ in range(-nums[index][1]):
            index = move_left(index % len(nums))
    else:
        for _ in range(nums[index][1]):
            index = move_right(index % len(nums))

def get(index):
    return nums[index % len(nums)][1]

def find(num):
    for i in range(len(nums)):
        if nums[i][1] == num:
            return i

with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    
    queries = []
    for i, line in enumerate(lines):
        num = int(line)
        queries.append([i, num])
        nums.append([i, num])

    for query in queries:
        og_index, d = query
        index = nums.index(query)
        move(index)

    zero = find(0)
    print(get(zero + 1000) + get(zero + 2000) + get(zero + 3000))