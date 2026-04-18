if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if i == query_name :
            s=0
            for n in student_marks[i]:
                s+=n
            a=s/len(student_marks[i])
    print(f"{a:.2f}")