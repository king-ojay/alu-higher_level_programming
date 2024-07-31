#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = None

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def calculate_GPA(self):
        # Calculate GPA based on courses taken
        if not self.courses_registered:
            return 0.0
        
        total_credits = 0
        total_points = 0

        for course in self.courses_registered:
            total_credits += course.credits
            total_points += course.credits * course.grade

        self.GPA = total_points / total_credits
        return self.GPA
