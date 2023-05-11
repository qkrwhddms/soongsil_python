# 학년 계산 함수
def calculate_grade(credit):
    if credit < 35:
        return 1
    elif credit < 70:
        return 2
    elif credit < 105:
        return 3
    else:
        return 4

# 학생 수 계산 함수
def count_students_by_grade(students, num_students):
    count_by_grade = [0, 0, 0, 0]
    for i in range(num_students):
        credit = students[i]
        grade = calculate_grade(credit)
        count_by_grade[grade-1] += 1
    return count_by_grade

# 학생별 학년 출력 함수
def print_student_grades(students, num_students):
    for i in range(num_students):
        credit = students[i]
        grade = calculate_grade(credit)
        print(f"{i+1}번 취득학점 - {credit} 학년 - {grade}")

# 학년별 학생 수 출력 함수
def print_count_by_grade(count_by_grade):
    for i in range(4):
        print(f"{i+1}학년 {count_by_grade[i]}명")

# 메인 함수
def main():
    students = []
    num_students = 5
    for i in range(num_students):
        while True:
            credit = input(f"{i+1}번의 취득학점은? >")
            try:
                credit = int(credit)
                if credit < 0 or credit > 180:
                    print("취득학점은 (0~180)까지 값만 입력해야 합니다. 다시 입력하세요.")
                    continue
                students.append(credit)
                break
            except ValueError:
                print("취득학점은 (0~180)까지 값만 입력해야 합니다. 다시 입력하세요.")

    while True:
        print(f"\n입력된 취득학점 {tuple(students)}")
        print("1. 개인별 학년")
        print("2. 학년 현황")
        print("3. 종료")
        menu = input("\n** 메뉴에 있는 숫자를 선택해 주세요. **\n")
        if menu == "1":
            print("*** [개인별 학년] ***")
            print_student_grades(students, num_students)
        elif menu == "2":
            print("*** [학년 현황] ***")
            count_by_grade = count_students_by_grade(students, num_students)
            print_count_by_grade(count_by_grade)
        elif menu == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("** 메뉴에 있는 숫자를 선택해 주세요. **")

if __name__ == '__main__':
    main()