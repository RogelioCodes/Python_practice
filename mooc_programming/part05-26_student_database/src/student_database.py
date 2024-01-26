# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = [] #[] represents completed courses
       
def add_course(students: dict, name: str, course: tuple):
    existing_courses = students[name]
 
    if course[1] == 0: #if score is 0 the course is not added
        return
  
    if len(existing_courses) == 0: #Always add the course if the list of courses is empty and the score is not 0
        students[name].append(course)
        return
    
    for i in range(len(existing_courses)):
        if course[0] == existing_courses[i][0]: #checks for duplicate
            if course[1] > existing_courses[i][1]: #if score is greater than previous score
                students[name] = [course]
            else:
                return
        else:   
            #print("ADDING COURSE 3")
            students[name].append(course)
        return

def print_student(students: dict, name: str):   
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    print(name + ": ")
   
    if len(students[name]) == 0:
        print(" no completed courses")
        return
    count = len(students[name])
    total = 0
    print(f" {count} completed courses:")
    for course in students[name]:
        print(f"  {course[0]} {course[1]}")
        total += course[1]
    avg = total / len(students[name])
    print(f" average grade {avg}")     

def summary(students: dict):
    person_with_most_courses_completed = {}
    person_with_best_avg_grade = {}
    most_courses_completed = 0
    highest_average_grade = 0
    total = 0

    for student in students.items():
        courses_completed = len(student[1])
        
        if courses_completed > most_courses_completed:
            most_courses_completed = courses_completed
            person_with_most_courses_completed = student[0]
      
        total = 0
        for course in student[1]: #student[1] is list of courses
            total += course[1]
          
        avg = total / courses_completed

        if avg > highest_average_grade:
            highest_average_grade = avg
            person_with_best_avg_grade = student[0]

    print(f"students {len(students)}")
    print(f"most courses completed {most_courses_completed} {person_with_most_courses_completed}")
    print(f"best average grade {highest_average_grade} {person_with_best_avg_grade}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)