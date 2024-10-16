# How good are you really? 8kyu

# There was a test in your class and you passed it. Congratulations!

# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return true if you're better, else false!

# Note:
# Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

def better_than_average(class_points: list, your_points: int) -> bool:
    #adding your score to the class points list
    all_points = class_points + [your_points]
    # sum off all the scores
    sum_class = sum(all_points)
    # finding the average score in the list
    average_score = sum_class / len(all_points)
    # logic to see if you are higher or lower than average and returning the bool
    if your_points < average_score:
        return False
    else:
        return True
    
print(better_than_average([10, 15, 30, 40], 35))