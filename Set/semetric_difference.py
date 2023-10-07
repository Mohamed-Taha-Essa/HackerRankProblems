# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
france_subscribe =set(map(int ,input().split()))
n2 = int(input())
english_subscribe =set(map(int ,input().split()))

# print(len(france_subscribe ^ english_subscribe))
print(len(france_subscribe.symmetric_difference(english_subscribe)))