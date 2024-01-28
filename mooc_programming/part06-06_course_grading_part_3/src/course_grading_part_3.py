# tee ratkaisu tänne

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

#exam points + exercise points = grade
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


if True:
    # this is never executed
    student_info_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
    exam_data_file = input("Exam points:  ")
else:
    # hard-coded input
    student_info_file = "students1.csv"
    exercises_file = "exercises1.csv"
    exam_data_file = "exam_points1.csv"



students = read_file(student_info_file)
exercise_grades = read_file(exercises_file)
exam_scores = read_file(exam_data_file)
final_score = {} #exam points + exercise points = grade


#calculates grade
for id, exercises_list in exercise_grades.items():
    list_str_to_int(exercises_list)


for id, exam_points in exam_scores.items():
    sum_of_exam_points = 0
    for score in exam_points:
        #print(f"score: {score}")
        sum_of_exam_points += int(score)
        exam_scores[id] = sum_of_exam_points
    #exam_scores[id] = exam_scores[id]
    exercises_total = sum(exercise_grades[id])
   #print(f"exercise_grades[id]: { exercise_grades[id] }")
    #print(f"exercise_grades[id] type: { type(exercise_grades[id]) }")
 
    percent_of_exercise_points = math.floor( (exercises_total / 40 ) * 100 )
    exercise_points = math.floor(percent_of_exercise_points/10)    
    total = exam_scores[id] + exercise_points
    #The three variables we need for the print statement
    #print(f"exam_scores[id]: {exam_scores[id]}")
    #print(f"exercise_points: {exercise_points}")
    #print(f"total: {total}")
    final_score[id] = total #final score is the exam score + the final amount of points awarded for each exercise completed
    #print(f"final_score: {final_score}")
    #print(f"{id} {scores}")



#This is the output of part 1
#print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
print("name" + " " * 25 + " exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for id, name in students.items():
    exercises_total = sum(exercise_grades[id])

    #3 we need
    percent_of_exercise_points = math.floor( (exercises_total / 40 ) * 100 )
    exercise_points = math.floor(percent_of_exercise_points/10)    
    total = exam_scores[id] + exercise_points
    grade = points_to_grade(final_score[id])
    full_name = name[0] + " " + name[1]
    if id in exercise_grades:
        spacer = 10
        print(f"{full_name:30}{exercises_total:<10}{exercise_points:<10}{exam_scores[id]:<10}{total:<10}{grade:<10}" )
#print("-" * 20)
#prints final score
#final score is exam points + exercise points calculation

#print("-" * 20)



#output:
#Student information: students1.csv
#Exercises completed: exercises1.csv
#Exam points: exam_points1.csv
#pekka peloton 0
#jaana javanainen 1
#liisa virtanen 3