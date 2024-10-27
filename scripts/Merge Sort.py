def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
            else:
                list1[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1


mylist = [75, 29, 83, 42, 16, 90, 56, 34, 20, 71, 88, 92, 7]
merge_sort(mylist)
print(mylist)
