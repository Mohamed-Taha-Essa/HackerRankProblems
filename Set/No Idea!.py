n ,m =map(int ,input().split())
arr =list(map(int ,input().split()))
count =0
A =set(map(int ,input().split()))
B=set(map(int ,input().split()))
for i in arr :
    if i in A:
        count+=1
    elif i in B:
        count-=1
print(count)