'''f we want to add a single element to an existing set,
we can use the .add() operation.
It adds the element to the set and returns 'None'.'''
#first answer
n =int(input())
s=[]
for i in range( n):
    s.append(input())
a = set(s)
print(len(a))

#second answer
'''s = set()

for _ in range(int(input())):
    s.add(input())
    
print(len(s))'''