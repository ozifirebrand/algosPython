def moveElementToEnd(array, toMove):
    # Write your code here.
    # initialise two pointers, left and right including an index
    # initialise values to array with pointers as indices
    # while left pointer is lesser than or equal to right pointer plus one
    # for right pointer, if value is equal to to-move value, reduce pointer by one
    # for left pointer if value is equal to to move value, and right pointer not equals to move
    # value, swap
    # then increment left pointer by one
    # return array
    left = 0
    right = len(array) - 1

    while len(array) != 0 and left != right:
        if array[right] == toMove:
            right -= 1
        if array[left] == toMove and array[right] != toMove:
            save = array[left]
            array[left] = array[right]
            array[right] = save
            left += 1
        if array[left] != toMove:
            left += 1
    return array


def maximum_element(an_array, index, current_max):

    if len(an_array) == 0:
        return 0
    if index == len(an_array) - 1:
        return current_max
    if an_array[index] > current_max:
        current_max = an_array[index]

    index += 1
    return maximum_element(an_array, index, current_max)


ma_element = float('-inf')
array = [562, 1, 562, 2, 2, 2, 8, 13, 4, 2]
print(moveElementToEnd(array, 562))
print(maximum_element(array, 0, ma_element))
