#!/usr/bin/env python

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

from __future__ import division
import sys
import json

classroom = {'_courselist':[],'_studentlist':[]}

def add_student(name):
	classroom.setdefault(name,{course:{'attends':[], 'grades':[]} \
		for course in classroom['_courselist']})
	classroom['_studentlist'].append(name)
	classroom['_studentlist'].sort()

def add_course(course):
	for name,student in classroom.items():
		if name=='_courselist':
			student.append(course)
		elif not name.startswith('_'):
			student[course] = {'attends':[], 'grades':[]}

def add_grade(student,course,grade):
	classroom[student][course]['grades'].append(grade)

def check_attendance(course):
	print 'Input "0" for absent, "1" or leave empty for present'
	for name in classroom['_studentlist']:
		check = raw_input(name+'?\t')
		classroom[name][course]['attends'].append(int(check) if check else 1)

def get_student_course_attendance(student,course):
	attend_sum = sum(classroom[student][course]['attends'])
	attend_count = len(classroom[student][course]['attends'])
	return attend_sum/attend_count

def get_student_full_attendance(student):
	all_attend = []
	for course in classroom['_courselist']:
		all_presence.extend(classroom[student][course]['attends'])
	return sum(all_attend)/len(all_attend)

def get_student_course_average(student,course):
	grade_sum = sum(classroom[student][course]['grades'])
	grade_count = len(classroom[student][course]['grades'])
	return grade_sum/grade_count

def get_student_full_average(student):
	averages = []
	for course in classroom['_courselist']:
		averages.append(get_student_course_average(student,course))
	return sum(averages)/len(averages)

def get_student():
	print 'Select the student index number:'
	for i in xrange(len(classroom['_studentlist'])):
		print str(i+1)+'\t'+classroom['_studentlist'][i]
	student = classroom['_studentlist'][int(raw_input())-1]
	return student

def get_course():
	print 'Select the index number of a course from the list below'
	for i in xrange(len(classroom['_courselist'])):
		print str(i+1)+'\t'+classroom['_courselist'][i]
	course = classroom['_courselist'][int(raw_input())-1]
	return course

if __name__=='__main__':
	menu_main = """------Main menu------

[1] Add a student
[2] Add a course
[3] Check attendance during a lesson
[4] Add a grade for a student
[5] Get grade data
[6] Get attendance data
[7] Save the class data to a JSON file
[8] Load the class data from a JSON file
[0] Quit"""
	menu_5 = """---Grade data menu---
[1] Get a student's average grade for a course
[2] Get a student's total average grade
[3] Get the average grade in a course of the whole class
[4] Get the total average grade of the whole class
[0] Return to the main menu"""
	menu_6 = """---Attendance data menu---
[1] Get a student's attendance for a course
[2] Get a student's total attendance
[3] Get the attendance of the whole class for a course
[4] Get the total attendance of the whole class
[0] Return to the main menu"""

	options_main = ['1','2','3','4','5','6','7','8','0']
	options_sub = ['1','2','3','4','0']
	
	unsaved_data = False
	
	print 'Classroom managing program\n'
	
	while True:
		print menu_main
		chosen_option = raw_input('Select an option from the list above\n')
		while not chosen_option:
			chosen_option = raw_input()
		if not any([chosen_option==x for x in options_main]):
			print 'Invalid choice. Select one of the numbers from the menu.'
			continue
		elif chosen_option=='1':
			print '===================='
			print 'Adding a student'
			last_name = raw_input('Input last name:\t')
			first_name = raw_input('Input first name:\t')
			add_student(last_name+' '+first_name)
			unsaved_data = True
		elif chosen_option=='2':
			print '===================='
			print 'Adding a course'
			course_name = raw_input('Input course name:\t')
			add_course(course_name)
			unsaved_data = True
		elif chosen_option=='3':
			print '===================='
			print 'Checking attendance'
			course = get_course()
			check_attendance(course)
			unsaved_data = True
		elif chosen_option=='4':
			print '===================='
			print 'Adding a grade'
			student = get_student()
			course = get_course()
			grade = input('What grade to add?\n')
			add_grade(student,course,grade)
			unsaved_data = True
		elif chosen_option=='5':
			print menu_5
			chosen_option = raw_input('Select an option from the list\n')
			while not chosen_option:
				chosen_option = raw_input()
			if not any([chosen_option==x for x in options_sub]):
				print 'Invalid choice.'
				continue
			elif chosen_option=='1':
				print '===================='
				print 'Student\'s average grade for a course'
				student = get_student()
				course = get_course()
				grade = get_student_course_average(student,course)
				print 'Average grade for '+student+' in '+course+':'
				print '{0:1.2f}'.format(grade)
			elif chosen_option=='2':
				print '===================='
				print 'Student\'s total average grade'
				student = get_student()
				grade = get_student_full_average(student)
				print 'Average grade for '+student+' across all courses:'
				print '{0:1.2f}'.format(grade)
			elif chosen_option=='3':
				print '===================='
				print 'Average grade in a course of the whole class'
				course = get_course()
				averages = []
				for name in classroom['_studentlist']:
					grade = get_student_course_average(name,course)
					averages.append(grade)
				print 'Average grade in '+course+' of the whole class:'
				print '{0:1.2f}'.format(sum(averages)/len(averages))
			elif chosen_option=='4':
				print '===================='
				print 'Total average grade of the whole class'
				averages = []
				for name in classroom['_studentlist']:
					grade = get_student_full_average(name)
					averages.append(grade)
				print 'The whole class\' average grade:'
				print '{0:1.2f}'.format(sum(averages)/len(averages))
			elif chosen_option=='0':
				continue
		elif chosen_option=='6':
			print menu_6
			chosen_option = raw_input('Select an option from the list\n')
			while not chosen_option:
				chosen_option = raw_input()
			if not any([chosen_option==x for x in options_sub]):
				print 'Invalid choice.'
				continue
			elif chosen_option=='1':
				print '===================='
				print 'Student\'s attendance in a course'
				student = get_student()
				course = get_course()
				present = get_student_course_attendance(student,course)
				print 'Attendance for '+student+' in '+course+':'
				print '{0:3.1f}%'.format(100*present)
			elif chosen_option=='2':
				print '===================='
				print 'Student\'s total attendance'
				student = get_student()
				present = get_student_full_attendance(student)
				print 'Attendance for '+student+' across all courses:'
				print '{0:3.1f}%'.format(100*present)
			elif chosen_option=='3':
				print '===================='
				print 'Average attendance in a course of the whole class'
				course = get_course()
				averages = []
				for name in classroom['_studentlist']:
					present = get_student_course_attendance(name,course)
					averages.append(present)
				print 'Average attendance in '+course \
					+' of the whole class:'
				print '{0:3.1f}%'.format(100*sum(averages)/len(averages))
			elif chosen_option=='4':
				print '===================='
				print 'Average total attendance of the whole class'
				averages = []
				for name in classroom['_studentlist']:
					present = get_student_full_attendance(name)
					averages.append(present)
				print 'The whole class\' average total attendance:'
				print '{0:3.1f}%'.format(sum(averages)/len(averages))
			elif chosen_option=='0':
				continue
		elif chosen_option=='7':
			print '===================='
			print 'Saving to a JSON file'
			filename = raw_input('Input the file name (no extension)\n')
			try:
				with open(filename+'.json','w') as output:
					output.write(json.dumps(classroom,sort_keys=True, \
						indent=4, separators=(',', ': ')))
			except IOError as e:
				print 'File output failed:'
				print e
			else:
				print 'Saved correctly to '+filename+'.json'
				unsaved_data = False
		elif chosen_option=='8':
			print '===================='
			print 'Loading from a JSON file'
			filename = raw_input('Input the file name (no extension)\n')
			try:
				with open(filename+'.json','r') as input:
					classroom = json.loads(input.read())
			except IOError as e:
				print 'File input failed:'
				print e
			else:
				print 'Loaded correctly from '+filename+'.json'
		elif chosen_option=='0':
			if unsaved_data:
				print 'There is unsaved data.'
				print 'Are you sure you want to quit? (Y/n)'
				confirm = raw_input()
				if confirm.upper()=='Y':
					sys.exit(0)
				else:
					continue
			else:
				sys.exit(0)

#Jakub Ahaddad
#github username ahdyqb
