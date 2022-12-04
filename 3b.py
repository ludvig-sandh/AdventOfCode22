def priority(item_type):
    if ord('a') <= ord(item_type) <= ord('z'):
        return ord(item_type) - ord('a') + 1     
    if ord('A') <= ord(item_type) <= ord('Z'):
        return ord(item_type) - ord('A') + 27
    raise Exception(f"Invalid item type \"{item_type}\"")

def get_elf_groups():
    elf_groups = []
    with open("in.txt", "r") as f:
        rucksacks = f.read().split("\n")
        for i in range(len(rucksacks) // 3):
            elf_groups.append(rucksacks[3 * i:3 * (i + 1)])
    return elf_groups
    
def find_group_badge(elf_group):
    for item_type in elf_group[0]:
        if item_type in elf_group[1] and item_type in elf_group[2]:
            return item_type

def main():
    answer = 0
    elf_groups = get_elf_groups()
    for elf_group in elf_groups:
        group_badge = find_group_badge(elf_group)
        answer += priority(group_badge)
    print(answer)
    
if __name__ == "__main__":
    main()