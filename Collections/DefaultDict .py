from collections import defaultdict
n, m=map(int,input().split())
A=[]
B=[]
for _ in range(n):
    A.append(input())
for _ in range(m):
    B.append(input())
d=defaultdict(list)
print(A)
for i in range(len(A)):
    d[A[i]].append(i+1)
    print('d[a[i]] = ',d[A[i]])

print("d = " ,d)
for i in range(len(B)):
    print("d[B[i]] = ",d[B[i]])
    if len(d[B[i]])>0:
        print(*d[B[i]])
    else:
        print(-1)


