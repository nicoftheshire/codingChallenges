# An implementation of merge sort in python.
# 
# Nicholas Holtzhausen, February 2022

def merge_sort(list):
    # If list length is smaller than 2, it is sorted:
    if len(list) == 1:
        return list

    # Find midpoint of list:
    mid = len(list) // 2

    # Recursively sort left and right halves of list:
    left_partition = merge_sort(list[:mid])
    right_partition = merge_sort(list[mid:])

    return merge(left_partition, right_partition)


def merge(left_partition, right_partition):
    i = 0
    j = 0
    left_partition = []
    right_partition = []
    ret_list = []
    while i < len(left_partition) and j < len(right_partition):
        if left_partition[i] < right_partition[j]:
            ret_list.append(left_partition[i])
            i += 1
        else:
            ret_list.append(right_partition[j])
            j += 1

    ret_list.extend(left_partition[i:])
    ret_list.extend(right_partition[j:])
    return ret_list

def main():
    unsorted_list = 'eoihfkjndfbvlkjhdasiuohf'
    print(unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)

main()
