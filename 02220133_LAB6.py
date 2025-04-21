
# 02220133_part2 (Merge Sort Implementation )

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0, 0  # Base case: no comparisons or accesses

    mid = len(arr) // 2
    left_half, left_comparisons, left_accesses = merge_sort(arr[:mid])
    right_half, right_comparisons, right_accesses = merge_sort(arr[mid:])
    
    sorted_arr, merge_comparisons, merge_accesses = merge(left_half, right_half)

    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    total_accesses = left_accesses + right_accesses + merge_accesses

    return sorted_arr, total_comparisons, total_accesses

def merge(left, right):
    sorted_arr = []
    i = j = 0
    comparisons = 0
    accesses = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        accesses += 2  # Accessing left[i] and right[j]
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            accesses += 1  # Adding left[i] to sorted_arr
            i += 1
        else:
            sorted_arr.append(right[j])
            accesses += 1  # Adding right[j] to sorted_arr
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        accesses += 1  # Adding left[i] to sorted_arr
        i += 1

    while j < len(right):
        sorted_arr.append(right[j])
        accesses += 1  # Adding right[j] to sorted_arr
        j += 1

    return sorted_arr, comparisons, accesses

# Example usage:
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, num_comparisons, num_accesses = merge_sort(original_list)
print(f"Original List: {original_list}")
print(f"Sorted using Merge Sort: {sorted_list}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of array accesses: {num_accesses}")


