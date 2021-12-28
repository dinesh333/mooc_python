# The file start_times.csv contains individual start times for a programming exam, in the format name;hh:mm. An example:

# jarmo;09:00
# timo;18:42
# kalle;13:23
# Additionally, the file submissions.csv contains points and handin times for individual exercises. The format here is name;task;points;hh:mm. An example:

# jarmo;1;8;16:05
# timo;2;10;21:22
# jarmo;2;10;19:15
# jne...
# Your task is to find the students who spent over 3 hours on the exam tasks. That is, any student whose any task was handed in over 3 hours later than their exam start time is labelled a cheater. There may be more than one submission for the same task for each student. You may assume all times are within the same day.

# Please write a function named cheaters(), which returns a list containing the names of the students who cheated


# Write your solution here
import csv
from datetime import datetime, timedelta

def get_students_exam_data() -> dict:
    students = {}
    with open('start_times.csv') as start_file:
        for line in csv.reader(start_file, delimiter=';'):
            student = line[0]
            start_time = datetime.strptime(line[1], '%H:%M')
            students[student] = {
                'start_time' : start_time,
                #'start_time' : line[1],
                'stats' : {
                    'tasks' : [],
                    'points' : [],
                    'submission_times' : []
                }
            }

    with open('submissions.csv') as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            student = line[0]
            task = int(line[1])
            point = int(line[2])
            sub_time = datetime.strptime(line[3], '%H:%M')
            students[student]['stats']['tasks'].append(task)
            students[student]['stats']['points'].append(point)
            students[student]['stats']['submission_times'].append(sub_time)
            #students[student]['stats']['submission_times'].append(line[3])

    return students

def cheaters():
    data = get_students_exam_data()
    cheaters = []
    for student, info in data.items():
        start_time = info['start_time']
        submission_times = info['stats']['submission_times']
        for time in submission_times:
            if time > (start_time + timedelta(hours=3)):
                cheaters.append(student)
                break
    return cheaters

# d = {
#     'jarmo' : {
#         'start_time' : '09:00',
#         'stats' : {
#             'exercises' : ['1', '2'],
#             'points' : ['8', '10'],
#             'submission_times' : ['16:05', '19:15']
#         }
#     }
# }