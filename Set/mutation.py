# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
first_set =set(input().split())
n2 = int(input())

for i in range(n2):
    mutation =input().split()

    second_set =set(input().split())
    if(mutation[0] == 'intersection_update'):
        first_set.intersection_update(second_set)
    elif(mutation[0] == 'update'):
        first_set.update(second_set)

    elif(mutation[0] == 'symmetric_difference_update'):
        first_set.symmetric_difference_update(second_set)


    elif(mutation[0] == 'difference_update'):
        first_set.difference_update(second_set)
    else:
        pass
summ = 0 
for i in first_set:
    summ +=int(i) 

print(summ)









