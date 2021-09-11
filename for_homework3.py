class_scores = [
    {'school_class': '4a', 'scores': [2,4,4,5,3]},
    {'school_class': '4b', 'scores': [5,3,4,5,2]},
    {'school_class': '4c', 'scores': [3,4,4,5,4]},
    {'school_class': '4d', 'scores': [3,2,4,2,4]},
]


class_count = 0
scores_sum = 0
for score in class_scores:
    scores_sum = sum(score['scores'])/len(score['scores'])
    class_count =+ 1
    print(scores_sum)
print(scores_sum/class_count)



