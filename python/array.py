# Instanitae the array
array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the element in array
for array_item in array_list:
    print(array_item)

# Search element in array using linear search
search_element = 3
for index, array_item in enumerate(array_list):
    if array_item == search_element:
        print('Index of elemtent={}'.format(index))

# Insert element in the array
array_list.append(11)

# Update the element at third index
update_index = 3
array_list[update_index] = 13

# Sorting