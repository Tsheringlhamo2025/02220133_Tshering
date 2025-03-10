#task 1
class CustomList:
    def __init__(self, capacity=10):
        # Initialize the private array and other attributes
        self._array = [None] * capacity  # Private array to store elements
        self.capacity = capacity         # Tracks the total capacity
        self.size = 0                    # Tracks the current size (number of elements)

        # Print statements to match the example output
        print(f"Created new CustomList with capacity: {self.capacity}")
        print(f"Current size: {self.size}")

# Example usage:
custom_list = CustomList()


#task 2
class CustomList:
    def __init__(self, capacity=10):
        self._array = [None] * capacity  # Private array to store elements
        self.capacity = capacity         # Total capacity
        self.size = 0                    # Current size (number of elements)
        

    def append(self, element):
        if self.size == self.capacity:
            print("Error: List capacity exceeded!")
            return  # Simply stop execution of this method
        self._array[self.size] = element
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds!")
        print(f"Element at index {index}: {self._array[index]}")
        return self._array[index]

    def set(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds!")
        self._array[index] = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        print(f"Current size: {self.size}")
        return self.size

# Example usage
custom_list = CustomList()
custom_list.append(5)      # Output: Appended 5 to the list
custom_list.get(0)         # Output: Element at index 0: 5
custom_list.set(0, 10)     # Output: Set element at index 0 to 10
custom_list.get(0)         # Output: Element at index 0: 10
print(f"Current size: {custom_list.size}")  # Output: Current size: 1
