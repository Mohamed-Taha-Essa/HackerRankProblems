'''
Constraints
Output Format


'''


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n >=2 and n<=10:
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            if len(scores) ==3 :
                if (all(x <= 100 and x>=0 for x in scores)):
                    student_marks[name] = scores
        query_name = input()
        degres = student_marks[query_name] 
        perc =float(sum(degres)/len(degres))
        res =f'{perc:.2f}'
        print(res)
        