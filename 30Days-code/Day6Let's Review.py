n = int(input())
evenn =[]
oddd=[]
for i in range(n):
    str =input()
    odd=[]
    even =[]
    for i ,j in enumerate(str):
        if i % 2==0:
            even.append(j) 
        else:
            odd.append(j)
    evenn.append(even)
    oddd.append(odd)

for i,j in zip(evenn ,oddd):
    print("".join(i),"".join(j))



for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])


