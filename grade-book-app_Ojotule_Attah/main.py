from database_setup import session
from grade_book import GradeBook
from models import Student, Course

def run_grade_book_app():
    # Create a GradeBook instance with a database session
    grade_book = GradeBook(session)

    # Add students and courses, register students for courses, etc.
    student1 = Student(names="John Doe", email="john@example.com")
    course1 = Course(name="Math", trimester="Spring 2024", credits=3, grade="A")
    
    grade_book.add_student(student1)
    grade_book.add_course(course1)
    grade_book.register_student_for_course(student1, course1)

    # Calculate GPA and generate transcript
    grade_book.calculate_GPA(student1)
    print(grade_book.generate_transcript(student1))

if __name__ == "__main__":
    run_grade_book_app()

