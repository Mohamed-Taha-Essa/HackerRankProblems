import textwrap
def merge_the_tools(string, k):
    # your code goes here
    a=textwrap.wrap(string,k)
    for i in a :
        i = sorted(set(i), key=i.index)
        print(''.join(i))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)