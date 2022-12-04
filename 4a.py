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

def interval_fully_contains(interval1, interval2):
    return interval1[0] <= interval2[0] and interval1[1] >= interval2[1]
        
def main():
    ans = 0
    intervals = get_intervals()
    for interval1, interval2 in intervals:
        if interval_fully_contains(interval1, interval2):
            ans += 1
        elif interval_fully_contains(interval2, interval1):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()