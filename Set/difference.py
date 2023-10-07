n = int(input())
france_subscribe =set(map(int ,input().split()))
n2 = int(input())
english_subscribe =set(map(int ,input().split()))

print(len(france_subscribe.difference(english_subscribe)))