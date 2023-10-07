def split_and_join(line):
    # write your code here
    l =line.split(" ")
    jo = "-".join(l)
    return jo

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)