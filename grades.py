# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76
from collections import defaultdict

def get_avg(student):
    grades = []
    grades = newdict[name]
    n = len(grades)
    return (name, sum(grades)/len(grades))

def save_grade(name, grade):
    if name in newdict:
        grades = newdict[name]
        grades.append(grade)
        newdict[name] = grades
    else:
        grades=[]
        grades.append(grade)
        newdict[name] = grades

def print_grades():
    for key, value in newdict.items:
        print(key, value)
    
newdict = {} 
with open('grades.txt') as f:
    for line in f:
        student, grade = line.strip().split()
        save_grade(student,int(grade))
  
newdict[name].append(grade)

def get_grades(fn):
    grades = defaultdict(list)
    with open(fn) as f:
        for line in f:
            name, grade = line.strip().s;it(' ')
            grade = float(grade)
            grades[name].append(grade)
            return grades
# want a function that can create a dictio
# nary given a filename

def get_averages(grades):
    avgs = []
    for name, scores in grades.items():
        avg = sum(scores)/len(scores)
        avgs.append((name, avg))
    return avgs

def rank_scores(avgs):
    sorted(avgs, key=lambda x: print(x, type(x)))
    sorted(avgs, key=lambda t: t[1][::-1]) 


