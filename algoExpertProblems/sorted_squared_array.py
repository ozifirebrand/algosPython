# space and time complexity This is an O(nlog n) time algorithm and an O(n) space
# Not efficient enough
def sort_and_square_array(array):
    new_array = []
    for value in array:
        new_array.append(value * value)
    new_array.sort()
    return new_array


first_array = [4, 3, 6, 8, 2]

print(sort_and_square_array(first_array))


# function of the reversed function in python
def sorting_and_squaring_arrays(array):
    print(list(reversed(range(len(array)))))


sorting_and_squaring_arrays(first_array)