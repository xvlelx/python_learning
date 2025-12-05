students = {
    "현기": {"국어": 85, "영어": 90, "수학": 88},
    "철수": {"국어": 70, "영어": 75, "수학": 80},
    "영희": {"국어": 95, "영어": 92, "수학": 98}
}

def get_student_average(students_dict, name):
    score = students_dict[name].values()
    return sum(score) / len(score)

def print_all_averages(students_dict):
    avg = get_student_average
    for i in students_dict:
        print(f'{i} {avg}')


print(get_student_average(students, '현기'))
print_all_averages(students)