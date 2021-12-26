# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    p1_avg = (person1['result1'] + person1['result2'] + person1['result3'])/3
    p2_avg = (person2['result1'] + person2['result2'] + person2['result3'])/3
    p3_avg = (person3['result1'] + person3['result2'] + person3['result3'])/3

    smallest = p1_avg
    for avg in [p2_avg, p3_avg]:
        if avg < smallest:
            smallest = avg
    
    if smallest == p1_avg:
        return person1
    elif smallest == p2_avg:
        return person2
    elif smallest == p3_avg:
        return person3
    else:
        return {}