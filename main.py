import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 2
print("Classes per week:", classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week/classes_per_week
print("Cost per class:", cost_per_class)
print(cost_per_class, type(cost_per_class))


#Part B
my_list = (5, 6.75, '2', 'hello', 'goodbye')
random_my_list = random.choice(my_list)
print("Random value in the list:", random_my_list)

