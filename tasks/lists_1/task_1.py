# create a list with 5 elem
elem1 = "Hello World"
elem2 = 1978
elem3 = True
elem4 = 2.09
elem5 = {"my_name": "Sergio"}

five_elem_lists = list((elem1, elem2, elem3, elem4, elem5))

print(five_elem_lists)

# delete the 3rd elem
del five_elem_lists[2]
print(five_elem_lists)

# print the length of the list to terminal
print("len of the list: ", len(five_elem_lists))

# reverse the order of items in  the list

five_elem_lists.reverse()
print(five_elem_lists)
five_elem_lists = five_elem_lists[::-1]
print(five_elem_lists)

# create another list with é elem

second_list = [False, (1,2,3)]

# expand the 1st with elem from 2nd list

# five_elem_lists.extend(second_list)
five_elem_lists += second_list
print(five_elem_lists)

# display only 6 elem from this list

print(five_elem_lists[:6])
