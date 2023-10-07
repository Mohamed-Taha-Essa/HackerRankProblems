from collections import namedtuple 


n =int(input())
column =input().split()
Student=namedtuple('Student' ,f'{column[0]} {column[1]} {column[2]} {column[3]}')

for i in range(n):
    pass

st1 =Student(25442 ,52 ,'taha' ,5)
print(st1)