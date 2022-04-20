def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid_point = len(a_list) // 2
        left = a_list[:mid_point]
        right = a_list[mid_point:]

        merge_sort(left)
        merge_sort(right)

        left_pointer = 0
        right_pointer = 0
        alist_pointer = 0

        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                a_list[alist_pointer] = left[left_pointer]
                left_pointer += 1
            else:
                a_list[alist_pointer] = right[right_pointer]
                right_pointer += 1
            alist_pointer += 1
        while left_pointer < len(left):
            a_list[alist_pointer] = left[left_pointer]
            left_pointer += 1
            alist_pointer += 1
        while right_pointer < len(right):
            a_list[alist_pointer] = right[right_pointer]
            right_pointer += 1
            alist_pointer += 1
    print("Merging ", a_list)


alist = [54, 26, 93, 17, 77, 66, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
