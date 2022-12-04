def priority(item_type):
    if ord('a') <= ord(item_type) <= ord('z'):
        return ord(item_type) - ord('a') + 1     
    if ord('A') <= ord(item_type) <= ord('Z'):
        return ord(item_type) - ord('A') + 27
    raise Exception(f"Invalid item type \"{item_type}\"")

def get_rucksacks():
    with open("in.txt", "r") as f:
        rucksacks = f.read().split("\n")
        rucksacks_compartments = [[sack[:len(sack) // 2], sack[len(sack) // 2:]] for sack in rucksacks]
        return rucksacks_compartments
    
def find_common_item_type(rucksack_compartment):
    for item_type in rucksack_compartment[0]:
        if item_type in rucksack_compartment[1]:
            return item_type

def main():
    answer = 0
    rucksacks_compartments = get_rucksacks()
    for rucksack_compartment in rucksacks_compartments:
        common_item_type = find_common_item_type(rucksack_compartment)
        answer += priority(common_item_type)
    print(answer)
    
if __name__ == "__main__":
    main()