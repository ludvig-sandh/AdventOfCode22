def get_intervals():
    intervals = []
    with open("in.txt", "r") as f:
        rows = f.read().split("\n")
        intervals_splitted = [row.split(",") for row in rows]
        for interval1, interval2 in intervals_splitted:
            interval1_splitted = interval1.split("-")
            interval2_splitted = interval2.split("-")
            interval = []
            interval.append([int(interval1_splitted[0]), int(interval1_splitted[1])])
            interval.append([int(interval2_splitted[0]), int(interval2_splitted[1])])
            intervals.append(interval)
    return intervals

def intervals_overlap(interval1, interval2):
    if interval2[0] <= interval1[0] <= interval2[1]:
        return True
    if interval2[0] <= interval1[1] <= interval2[1]:
        return True
    if interval1[0] <= interval2[0] <= interval1[1]:
        return True
    if interval1[0] <= interval2[1] <= interval1[1]:
        return True
    return False
        
def main():
    ans = 0
    intervals = get_intervals()
    for interval1, interval2 in intervals:
        if intervals_overlap(interval1, interval2):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()

# Total time: 14min