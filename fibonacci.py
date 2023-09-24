cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        li = []
        return li

    elif n == 1:
        li = []
        li.append(0)
        return li
    if n <= 15 and n >= 0:
        li = []
        li.append(0)
        li.append(1)
        for i in range(2, n):
            num = li[i - 1] + li[i - 2]
            li.append(num)
    return (li)


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))