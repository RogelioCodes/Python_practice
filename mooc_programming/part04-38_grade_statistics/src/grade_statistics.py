# Write your solution here
import math
def ask_scores():
    points = str()
    scores = []
    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            break
        else:
            scores.append(points)
    return scores

def determine_grade(exam_points, exercise_points):

    total_points = exam_points + exercise_points
   
    if total_points >= 0 and total_points <= 14 or exam_points < 10:
        grade = 0
    elif total_points >= 15 and total_points <= 17:
        grade = 1
    elif total_points >= 18 and total_points <= 20:
        grade = 2
    elif total_points >= 21 and total_points <= 23:
        grade = 3
    elif total_points >= 24 and total_points <= 27:
        grade = 4
    elif total_points >= 28 and total_points <= 30:
        grade = 5
    return grade
def grade_distribution(grades):
    print("Grade distribution:")
    i = 5
    stars = "*"
    while i >= 0:
  
        print(f"{i:>3}: { stars * grades.count(i)}")
        i -= 1

def statistics(scores):

    avg = 0
    passing = 0
    grades = [] 
    for score in scores:
        exam_points = int((score.split())[0])
        exercise_points = int((score.split())[1])
        exercise_points = math.floor(exercise_points / 10)
        avg += exam_points
        avg += exercise_points

        grades.append(determine_grade(exam_points, exercise_points))

    # Determines people passing the course
    avg = avg / len(scores) 
    
    for grade in grades:
        if grade > 0:
            passing += 1
    pass_percentage = passing/len(grades) * 100 

    print("Statistics:")
    print(f"Points average: {round(avg,1)}") 
    print(f"Pass percentage: {round(pass_percentage, 1)}")
    grade_distribution(grades)

scores = ask_scores()
statistics(scores)


