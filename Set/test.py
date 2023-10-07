n = int(input())
A = set(input().split())
N = int(input())

for i in range(N):
    opr = input().split()
    B = set(input().split())
    
    if opr[0] == "intersection_update":
        A.intersection_update(B)

    elif opr[0] == "update":
        A.update(B)

    elif opr[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)

    elif opr[0] == "difference_update":
        A.difference_update(B)

    else:
        pass

sum = 0
for i in A:
    sum += int(i)

print(sum)