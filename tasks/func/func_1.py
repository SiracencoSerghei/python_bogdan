# # create a merge_lists_to_dict function
# # the func must have two parameters
# # the func should combine two lists using the
# # built-in zip func
# # convert a zip object to a dict and return it from the func
# # call the func by passing it two lists as arguments
# # output the result of the func call to the terminal


# def merge_lists_to_dict(keys_list: list, values_list: list) -> dict:
#         merged_dict = dict(zip(keys_list, values_list))
#         return merged_dict

# keys = [1, 2, 3, 4, 5]
# values = ('Sergio', 'Arturo', 'Pietro', 'Vlad', 'Leonora')
# result = merge_lists_to_dict(keys, values)
# print(result)

# =======================

# # rewrite the call to the merge_lists_to_dict func from 
# # the previous task so that it uses keyword args

# def merge_lists_to_dict(*args: list) -> dict:
#     merged_dict = dict(zip(args[0], args[1]))
#     return merged_dict


# keys = [1, 2, 3, 4, 5]
# values = ('Sergio', 'Arturo', 'Pietro', 'Vlad', 'Leonora')
# result = merge_lists_to_dict(keys, values)
# print(result)

# ==============================

# Add another function call. first arg in this call should be 
# positional arg and the second should be keyword arg

def merge_lists_to_dict(key, value = []) -> dict:
    merged_dict = dict(zip(key, value))
    return merged_dict


keys = [1, 2, 3, 4, 5]
values = ( 'Pietro', 'Leonora', 'Sergio', 'Arturo', 'Vlad')
result = merge_lists_to_dict(keys, value = values)
print(result)
