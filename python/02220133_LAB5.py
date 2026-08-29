# 02220133_part2
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    
    comparisons += 1
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

# Example usage:
sorted_list = [12, 23, 34, 45, 56, 67, 89]
target = 67

print("Sorted List:", sorted_list)
print(f"Searching for {target} using Binary Search")

# Iterative version
print("Iterative version : ")
index, comparisons = binary_search_iterative(sorted_list, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comparisons}")

# Recursive version
print("Recursive version : ")
index, comparisons = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {comparisons}")
