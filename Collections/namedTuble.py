from collections import namedtuple 
n =int(input())
Student=namedtuple('Student' ,input().split())
summ=0
for i in range(n):
    st =Student((input().split()))
    e =int(st.MARKS)
    summ+=e
    
print(summ/n)
print(sum([int(Student(*(input().split())).MARKS) for _ in range(n)])/n)
