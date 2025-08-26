# Question 1 - Creating an empty list called my_list.
my_list = [] #OR my_list = list()

print(my_list)

# Question 2 - Append the following elements to my_list: 10, 20, 30, 40.
my_list = []
my_list.extend([10, 20, 30, 40]) #OR my_list.append(10) my_list.append(20) my_list.append(30) my_list.append(40)

print(my_list)

# Question 3 - Insert the value 15 at the second position in the list.
my_list = [10, 20, 30, 40]
my_list.insert(1, 15)

print(my_list)

# Question 4 - Extend my_list with another list: [50, 60, 70].
my_list = [10, 15, 20, 30, 40]
my_list.extend([50, 60, 70])

print(my_list)

# Question 5 - Remove the last element from my_list.
my_list = [10, 15, 20, 30, 40, 50, 60, 70]
my_list.pop()

print(my_list)

# Question 6 - Sort my_list in ascending order.
my_list = [10, 15, 20, 30, 40, 50, 60]
my_list.sort(reverse=False)

print(my_list)

# Question 7 - Find and print the index of the value 30 in my_list.
my_list = [10, 15, 20, 30, 40, 50, 60]
index_30 = my_list.index(30)

print(f"The index of 30 is: {index_30}")
