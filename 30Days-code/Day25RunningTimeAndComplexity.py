import math
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False

    return True

n = int(input())

li =[]
for i in range(n):
    number =int(input())
    if is_prime(number):
        li.append('Prime')
    else:
        li.append("Not prime")
print('\n'.join(li) )

