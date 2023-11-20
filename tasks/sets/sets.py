# create a set of several elements of the int type
my_set = set([1, 2, 3, 4, 5])

# add another element to it
my_set.add(6)
print(my_set)

#  create another set with several elements, some of 
# which should be the same as in the first set
second_set = set((1, 3, 5, 7, 9, 11, 13, 15))
print(second_set)

# find common elements in two sets and place them in a new set
new_set = my_set & second_set
print(new_set)

# convert the resulting set to a list and print the list to 
# the terminal
list_of_sets = list(new_set)
print(list_of_sets)

print('differents from my_set and second_set: ', my_set - second_set)
print('differents from second_set and my_set: ', second_set - my_set)
