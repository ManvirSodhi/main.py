import timeit
import Student

if __name__ == '__main__':
    start_time = timeit.default_timer()
    maths = int(input("Enter marks for Maths: "))
    science = int(input("Enter marks for science: "))
    history = int(input("Enter marks for history: "))
    geo = int(input("Enter marks for geography: "))
    Student.Student().compare_marks(maths, science, history, geo)

    marks = int(input("Enter total marks: "))
    students = int(input("Enter total students: "))
    avg = Student.Student().average_marks(marks, students)
    print("The average marks for the class is : ", avg)

    days_present = int(input("Enter days present: "))
    avg_presence = Student.Student().attendance_average(days_present, students)
    print("Average presence of the class is : ", avg_presence)

    students_present = int(input("Total students present today: "))
    absent_today = Student.Student().student_absent(students, students_present)
    print("Total Students absent today: ", absent_today)
    end_time = timeit.default_timer()
    print("Total time taken is ", end_time - start_time)