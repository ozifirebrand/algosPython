def is_valid_subsequence(array, sequence):
    array_index = 0
    sequence_index = 0
    while sequence_index < len(sequence) and array_index < len(array):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)


print(is_valid_subsequence(array=[6, 3, 2, 5, 1, 9, 4], sequence=[6, 2, 9]))
print(is_valid_subsequence(array=[6, 3, 2, 5, 1, 9, 4], sequence=[1, 2, 9]))
