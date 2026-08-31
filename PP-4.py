def grader():
    print("Thank for using Dauren's grader")
    student_name = input("Enter student name:")

    while True:
        try:
            course1 = input("Enter first course grade:")
            course1_f = int(course1)
            break
        except:
            print("Wrong value. Try again!")

    while True:
        try:
            course2 = input("Enter second course grade:")
            course2_f = int(course2)
            break
        except:
            print("Wrong value. Try again!")

    while True:
        try:
            course3 = input("Enter third course grade:")
            course3_f = int(course3)
            break
        except:
            print("Wrong value. Try again!")

    total = course1_f + course2_f + course3_f
    percentile = total/3
    if percentile >= 90:
        return f"{student_name} got A"

    elif percentile >= 80 and percentile < 90:
        return f"{student_name} got B"

    elif percentile >= 70 and percentile < 80:
        return f"{student_name} got C"

    elif percentile >= 60 and percentile < 70:
        return f"{student_name} got D"
    else:
        return f"{student_name} got F"

print(grader())