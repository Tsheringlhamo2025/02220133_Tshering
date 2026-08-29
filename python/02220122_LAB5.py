#Part1: Sequential Search Implementation _ 02220122

# A function named sequential_search is defined where it takes two arguments arr and target
def sequential_search(arr, target):
    comparisons = 0
# enumerate() is a in-built python function that returns index of each element and the value at that index.
    for index, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return index, comparisons
    return -1, comparisons # -1 means not found

# Example usage
arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

print(f"List: {arr}")
print(f"Searching for {target} using Sequential Search")
index, comparisons = sequential_search(arr, target)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {comparisons}")
