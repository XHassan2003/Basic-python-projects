import random
people = input("Enter your names serperated by comma: ")
names = people.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
list1 = names[random_choice]
print(list1, "is going to buy the meal today!")