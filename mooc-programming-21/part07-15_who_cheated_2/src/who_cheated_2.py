# You have the CSV files from the previous exercise at your disposal again. Please write a function named final_points(), which returns the final exam points received by the students, in a dictionary format, following these criteria:

# If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
# If the submission was made over 3 hours after the start time, the submission is ignored.
# The tasks are numbered 1 to 8, and each submission is graded with 0 to 6 points.

# In the dicionary returned the key should be the name of the student, and the value the total points received by the student.

# Hint: nested dictionaries might be a good approach when processing the tasks and submission times of each student.

# Write your solution here
import csv
import json
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

def final_points():
    final_points = {}
    data = get_students_exam_data()
    for student, info in data.items():
        total_points = 0
        start_time = info['start_time']
        tasks = info['stats']['tasks']
        for task in range(1, 9):
            indices = [i for i, v in enumerate(tasks) if v == task]
            max_point = 0
            for index in indices:
                point = info['stats']['points'][index]
                sub_time = info['stats']['submission_times'][index]
                if sub_time <= (start_time + timedelta(hours=3)):
                    if point > max_point:
                        max_point = point
            total_points += max_point
        final_points[student] = total_points
    return final_points

# Data structure
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