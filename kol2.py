# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Student:
"""Contains data for a specific student:
	first_name: student's first name
	last_name: student's last name
	courses: list of courses the student attends
		keys: course names
		values: 2d list of
			- attendance (boolean values)
			- grades (float [1:6])"""
	def __init__(self,last_name,first_name):
		self.first_name = first_name
		self.last_name = last_name
		self.courses = {}
	
	def add_student_course(self,course_name):
		self.courses[course_name] = [ [] , [] ]'
	
	def full_name(self):
		return self.last_name+" "+self.first_name

class Classroom:
"""Contains data for a classroom (group of students)
	student_list: list of Student objects
	courses_list: list of names of courses"""
	def __init__(self):
		self.student_list = []
		self.courses_list = []
	
	def add_course(self):
		course_name = input("What is the course name? (please type it surrounded by quotes)\n")
		self.courses_list.append(course_name)
	
	def add_student(self):
		print "Student's last name? (surround in quotes)"
		last_name = input()
		print "Student's first name? (surround in quotes)"
		first_name = input()
		student = Student(last_name,first_name)
		self.student_list.append(student)
	
	def finalize_students(self):
		for student in self.student_list:
			for course in self.courses_list:
				student.add_student_course(course)

	def check_attendance(self):
		print "Select the course number from the list:
		for i in range(len(self.courses_list)):
			print "["+str(i)+"] "+self.courses_list[i]
		chosen_index = input()
		course_name = self.courses_list[chosen_index]
		print "Checking attendance. Type 1 after a name if present, 0 if absent."
		for student in student_list:
			attendance = input(student+" ")
			student.courses['course_name'][0].append(bool(attendance))
	
	def add_student_grade(self):
		print "Select the course number from the list:
		for i in range(len(self.courses_list)):
			print "["+str(i)+"] "+self.courses_list[i]
		course_index = input()
		course_name = self.courses_list[course_index]
		print "Select student:"
		for i in range(len(self.student_list)):
			print "["+str(i)+"] "+self.student_list[i].full_name()
		student_index = input()
		grade = input("What is the obtained grade? ")
		self.student_list[student_index].courses['course_name'][1].append(grade)
