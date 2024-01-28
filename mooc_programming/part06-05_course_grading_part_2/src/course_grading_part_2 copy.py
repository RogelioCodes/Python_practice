# wwite your solution here
# write your solution here
#file format 1
#id;first;last
#12345678;peter;pythons
#12345687;jean;javanese
#12345699;alice;adder

#file 2 format
#id;e1;e2;e3;e4;e5;e6;e7
#12345678;4;1;1;4;5;2;4
#12345687;3;5;3;1;5;4;6
#12345699;10;2;2;7;10;2;2

import math

def read_file(file_name):
    dict = {}
    with open(file_name) as new_file:
        for line in new_file:
            line = line.replace("\n","")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            dict[parts[0]] = parts[1:]
        return dict


def list_str_to_int(list):
    for index, value in enumerate(list):
        list[index] = int(value)

def points_to_grade(points):
    grade = -1
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5


if False:
    # this is never executed
    student_info_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
    exam_data_file = input("Exam points:  ")
else:
    # hard-coded input
    student_info_file = "students1.csv"
    exercises_file = "exercises1.csv"
    exam_data_file = "exam_points1.csv"


#students = []
students = read_file(student_info_file)
exercise_grades = read_file(exercises_file)
exam_scores = {}
#exam_scores = read_file(exam_data_file)
final_score = {}

#print(exam_scores)
#calculates grade


with open(exam_data_file) as new_file:
    for line in new_file:
        line = line.replace("\n","")
        parts = line.split(";")
        if parts[0] == "id":
           
            continue
        exam_points = parts[1:]
        print(f"exam_points: {exam_points}")
        sum = 0
        id = parts[0]
        for score in exam_points:
           # print(f"exam_points: {exam_points}")
            sum += int(score)
           
            exam_scores[parts[0]] = sum
        exam_scores[parts[0]] = exam_scores[parts[0]]
        print(f"parts0: {parts[0]}")
        print(f"exercise_grades[id]: {exercise_grades[parts[0]] }")
        percent_of_exercise_points = math.floor( (exercise_grades[parts[0]] / 40 ) * 100 )
        exercise_points = math.floor(percent_of_exercise_points/10)
        #print(f"exercise_%: {percent_of_exercise_points}")
       # print(f"exercise_points: {exercise_points}")
        total = exam_scores[parts[0]] + exercise_points
        final_score[parts[0]] = total
       # print(f"id: {id} exam points: { exam_scores[parts[0]]}, exercise_points: { exercise_grades[parts[0]]}")
        #print(f"total: {total}") 
#print(exam_scores)
#print(final_score)


#for id, name in students.items():
#    if id in exercise_grades:
#        grade = exercise_grades[id]
#        print(f"{name} {grade}" )



for id, name in students.items():
    if id in final_score:
        grade = points_to_grade(final_score[id])
        print(f"{name} {grade}" )

for id, exercises_list in exercise_grades.items():
    list_str_to_int(exercises_list)

for id, name in students.items():
 
    exercises_total = sum(exercise_grades[id])
   
    if id in exercise_grades:
       
        print(f"{name[0]} {name[1]} {exercises_total}" )
#output:
#Student information: students1.csv
#Exercises completed: exercises1.csv
#pekka peloton 21
#jaana javanainen 27
#liisa virtanen 35