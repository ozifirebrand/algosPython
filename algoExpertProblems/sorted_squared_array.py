def sort_and_square_array(array):
    new_array = []
    for value in array:
        new_array.append(value * value)
    new_array.sort()
    return new_array


first_array = [4, 3, 6, 8, 2]

print(sort_and_square_array(first_array))