from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Association table for many-to-many relationship between students and courses
student_course = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    names = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses_registered = relationship('Course', secondary=student_course, back_populates='students')
    GPA = Column(Float)

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def calculate_GPA(self):
        total_credits = sum(course.credits for course in self.courses_registered)
        total_points = sum(self.get_grade_points(course.grade) * course.credits for course in self.courses_registered)
        self.GPA = total_points / total_credits if total_credits > 0 else 0
        return self.GPA

    def get_grade_points(self, grade):
        grade_mapping = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        return grade_mapping.get(grade, 0.0)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    trimester = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    grade = Column(String)
    students = relationship('Student', secondary=student_course, back_populates='courses_registered')

