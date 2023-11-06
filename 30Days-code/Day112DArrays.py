
arr=[]
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
    
row = len(arr)
col = len(arr[0])
mx = -100
for i in range(row-2):
    for j in range(col-2):
        t = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j +2]
        mx = max(t, mx)

print(mx)
