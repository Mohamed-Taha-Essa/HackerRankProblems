# Enter your code here. Read input from STDIN. Print output to STDOUT
n =int(input())
d={}
for i in range(n):
    name ,number =input().split()
    d[name] =(number)
for i in range(n):
    try:
        name =input()
        if name in d.keys():
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except EOFError:
        break

    
        
        