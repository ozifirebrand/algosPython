# space and time complexity This is an O(nlog n) time algorithm and an O(n) space
# Not efficient enough
def sort_and_square_array(array):
    new_array = []
    for value in array:
        new_array.append(value * value)
    new_array.sort()
    return new_array


# reversed function in python. It simply reverses lists and the likes
def sorting_and_squaring_arrays(array):
    array.sort()
    sorted_squares_array = [0 for _ in array]
    smallest_value_index = 0
    largest_value_index = len(array) - 1

    for index_in_descending_order in reversed(range(len(array))):

        smallest_value = array[smallest_value_index]
        largest_value = array[largest_value_index]

        if abs(smallest_value) > abs(largest_value):
            sorted_squares_array[index_in_descending_order] = smallest_value * smallest_value
            smallest_value_index += 1

        else:
            sorted_squares_array[index_in_descending_order] = largest_value * largest_value
            largest_value_index -= 1
    return sorted_squares_array


first_array = [4, 3, 6, 8, 2]

print(sort_and_square_array(first_array))

print(sorting_and_squaring_arrays(first_array))
