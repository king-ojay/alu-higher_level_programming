from grade_book import GradeBook
from models import Student, Course
from database_setup import session 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///gradebook.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def run_grade_book_app():
    grade_book = GradeBook(session)

    while True:
        print("Choose an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            names = input("Enter student name: ")
            email = input("Enter student email: ")
            student = Student(names=names, email=email)
            grade_book.add_student(student)
            print("Student added successfully.")

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name=name, trimester=trimester, credits=credits)
            grade_book.add_course(course)
            print("Course added successfully.")

        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")

            student = session.query(Student).filter_by(email=student_email).first()
            course = session.query(Course).filter_by(name=course_name).first()

            if student and course:
                grade_book.register_student_for_course(student, course)
                print("Student registered for course successfully.")
            else:
                print("Student or Course not found.")

        elif choice == '4':
            sorted_students = grade_book.calculate_ranking()
            print("Student Rankings:")
            for student in sorted_students:
                print(f"{student.names} - GPA: {student.GPA}")

        elif choice == '5':
            grade = input("Enter grade to search for: ")
            matching_students = grade_book.search_by_grade(grade)
            print("Students with grade", grade)
            for student in matching_students:
                print(f"{student.names} - Email: {student.email}")

        elif choice == '6':
            student_email = input("Enter student email: ")
            student = session.query(Student).filter_by(email=student_email).first()
            if student:
                print(grade_book.generate_transcript(student))
            else:
                print("Student not found.")

        elif choice == '7':
            break

        else:
            print("Very wrong choice, Please try again.")

if __name__ == "__main__":
    run_grade_book_app()
