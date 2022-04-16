def array_sort(array, target_sum):
    triplets = []
    var = array.sort
    for index in range(0, 9):
        right = len(array) - 1
        left = index + 1
        while left < right:
            current_sum = array[index] + array[left] + array[right]
            if current_sum == target_sum:
                array_of_sums = {array[index], array[left], array[right]}
                triplets.append(array_of_sums)
                right -= 1
                left += 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return triplets