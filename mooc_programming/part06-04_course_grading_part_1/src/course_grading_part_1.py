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


if False:
    # this is never executed
    student_info_file = input("Student information: ")
    exercises_file = input("Exercises completed: ")
else:
    # hard-coded input
    student_info_file = "students1.csv"
    exercises_file = "exercises1.csv"
   


#students = []
students = read_file(student_info_file)
exercise_grades = read_file(exercises_file)



#Dictionary exercises has list of strings as value. Convert list of strings to list of ints
for id, exercises_list in exercise_grades.items():
    list_str_to_int(exercises_list)

for id, name in students.items():
 
    exercises_total = sum(exercise_grades[id])
   
    if id in exercise_grades:
       
        print(f"{name[0]} {name[1]} {exercises_total}" )
#

#output:
#Student information: students1.csv
#Exercises completed: exercises1.csv
#pekka peloton 21
#jaana javanainen 27
#liisa virtanen 35