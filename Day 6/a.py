text = input()
last = [*text[:4]]
if len(last) == len(set(last)):
    print(4)
    exit(0)
for i in range(4, len(text)):
    last = last[1:]
    last.append(text[i])
    if len(last) == len(set(last)):
        print(i + 1)
        exit(0)