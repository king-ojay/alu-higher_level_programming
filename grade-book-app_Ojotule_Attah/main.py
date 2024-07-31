from database_setup import session
from grade_book import GradeBook
from models import Student, Course

def run_grade_book_app():
    grade_book = GradeBook(session)

    # Example data
    student1 = Student(names="John Doe", email="john@example.com")
    course1 = Course(name="Math", trimester="Spring 2024", credits=3, grade="A")
    
    # Add student and course
    grade_book.add_student(student1)
    grade_book.add_course(course1)
    # Register student for course
    grade_book.register_student_for_course(student1, course1)
    # Calculate GPA
    grade_book.calculate_GPA(student1)
    # Print transcript
    print(grade_book.generate_transcript(student1))

if __name__ == "__main__":
    run_grade_book_app()

