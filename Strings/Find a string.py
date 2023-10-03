def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        print(string[i:])
        if string[i:].startswith(sub_string):
            count += 1
    return count
if __name__ == '__main__':
    string = input("ente the string ").strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)