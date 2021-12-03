def two_sum(array, target_sum):
    two_sum_array = []
    for value in array:
        number = target_sum - value
        for a_digit in array:
            if number == a_digit & a_digit != value:
                two_sum_array.append(a_digit)
                two_sum_array.append(value)
                return two_sum_array
    return two_sum_array


array1 = [4, 2, 7, 5, 3, 1]
targetSum = 10
print(two_sum(array1, targetSum))


def two_sum_2(array2, value):
    array2.sort()
