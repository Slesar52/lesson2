class_scores = [
    {'school_class': '4a', 'scores': [2,4,4,5,3]},
    {'school_class': '4b', 'scores': [5,3,4,5,2]},
    {'school_class': '4c', 'scores': [3,4,4,5,4]},
    {'school_class': '4d', 'scores': [3,2,4,2,4]},
]

avg_school = []


for score in class_scores:
    avg_class = sum(score['scores'])/len(score['scores'])
    avg_school.append(avg_class)
    print("средняя по классу: ", avg_class)
print("Средняя по школе", sum(avg_school)/len(avg_school))



