if __name__ == '__main__':
   
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    print(students)
    print("========================")

    #second_lowest_score = students[1][1]
    set_element = set([x[1] for x in students])
    print("set elemnt :" ,set_element)
    lis_element =list()
    print("lis_element :" ,lis_element)
    print("========================")
    second_lowest_score = sorted(lis_element)[1]

    print("second_lowest_score:",second_lowest_score)
    print("========================")
    desired_students = []
    for stu in students:
        print(stu[1])
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))
    