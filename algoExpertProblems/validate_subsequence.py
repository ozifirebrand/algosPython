def is_valid_subsequence(array, sequence):
    # array_index = 0
    sequence_index = 0
    # while sequence_index < len(sequence) and array_index < len(array):
    #     if array[array_index] == sequence[sequence_index]:
    #         sequence_index += 1
    #     array_index += 1
    for item in array:
        for item2 in array:
            if item2 == item:
                sequence_index += 1
            else : continue
    return sequence_index == len(sequence)


print(is_valid_subsequence(array=[6, 3, 2, 5, 1, 9, 4], sequence=[6, 2, 9]))
print(is_valid_subsequence(array=[6, 3, 2, 5, 1, 9, 4], sequence=[1, 2, 9]))