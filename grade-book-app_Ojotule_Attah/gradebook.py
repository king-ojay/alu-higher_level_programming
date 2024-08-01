# gradebook.py

from models import Student, Course

class GradeBook:
    def __init__(self, session):
        self.session = session

    def add_student(self, student):
        self.session.add(student)
        self.session.commit()

    def add_course(self, course):
        self.session.add(course)
        self.session.commit()

    def register_student_for_course(self, student, course):
        student.register_for_course(course)
        self.session.commit()

    def calculate_GPA(self, student):
        return student.calculate_GPA()

    def calculate_ranking(self):
        students = self.session.query(Student).all()
        sorted_students = sorted(students, key=lambda student: student.GPA if student.GPA else 0, reverse=True)
        return sorted_students

    def search_by_grade(self, grade):
        matching_students = []
        students = self.session.query(Student).all()
        for student in students:
            for course in student.courses_registered:
                if course.grade == grade:
                    matching_students.append(student)
                    break
        return matching_students

    def generate_transcript(self, student):
        transcript = f"Transcript for {student.names}:\n"
        transcript += f"Email: {student.email}\n"
        transcript += "Courses Registered:\n"
        for course in student.courses_registered:
            transcript += f"- {course.name}, Trimester: {course.trimester}, Credits: {course.credits}, Grade: {course.grade}\n"
        transcript += f"GPA: {student.GPA}\n"
        return transcript

