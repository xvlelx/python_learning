student = {
    '이름' : '홍현기',
    '나이' : 28,
    '점수' : 55
}

def print_student(student_dict):
    print(f"{student_dict['이름']}{student_dict['나이']}{student_dict['점수']}")

    return

def is_passed(student_dict):
    if student_dict['점수'] >= 60:
        return True
    else:
        return False

def print_result(student_dict):
    result = print_student(student_dict)
    result = is_passed(student_dict)
    if result == True:
        print('pass')
    else:
        print('Fail')

print_result(student)
