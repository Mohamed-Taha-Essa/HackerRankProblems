from collections import Counter

K = int(input()) + 1
rooms = list(map(int, input().split()))


count = Counter(rooms)

for key, value in count.items():
    if value == 1:
        print(key)