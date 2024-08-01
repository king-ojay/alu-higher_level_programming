

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course
from gradebook import GradeBook

engine = create_engine('sqlite:///gradebook.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def run_grade_book_app():

    print("Welcome to Ojay's Grade Book Application!")

    grade_book = GradeBook(session)

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            names = input("Enter student name: ")
            email = input("Enter student email: ")
            student = Student(names=names, email=email)
            grade_book.add_student(student)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name=name, trimester=trimester, credits=credits)
            grade_book.add_course(course)
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            student = session.query(Student).filter_by(email=student_email).first()
            course = session.query(Course).filter_by(name=course_name).first()
            if student and course:
                grade_book.register_student_for_course(student, course)
            else:
                print("Student or Course not found.")
        elif choice == '4':
            ranking = grade_book.calculate_ranking()
            print("Student Ranking:")
            for rank, student in enumerate(ranking, start=1):
                print(f"{rank}. {student.names} - GPA: {student.GPA}")
        elif choice == '5':
            grade = input("Enter grade to search for: ")
            students = grade_book.search_by_grade(grade)
            print(f"Students with grade {grade}:")
            for student in students:
                print(f"- {student.names}")
        elif choice == '6':
            student_email = input("Enter student email: ")
            student = session.query(Student).filter_by(email=student_email).first()
            if student:
                transcript = grade_book.generate_transcript(student)
                print(transcript)
            else:
                print("Student not found.")
        elif choice == '7':
            print("Byeee.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_grade_book_app()
