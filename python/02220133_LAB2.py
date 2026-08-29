#Task 1: Implement the Node and List Class Structure 

# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Data field to store the element
        self.next = None  # Reference to the next node

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Reference to the first node
        self.tail = None  # Reference to the last node (optional but helpful)
        self.size = 0     # Counter to track the number of elements

    def __str__(self):
        # Helper method to represent the linked list as a string
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

    def append(self, data):
        # Add an element to the end of the list
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node  # Update the tail reference
        self.size += 1

    def prepend(self, data):
        # Add an element to the beginning of the list
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def get_size(self):
        # Return the current size of the linked list
        return self.size

# Example Usage
linked_list = LinkedList()
print("Created new LinkedList")
print(f"Current size: {linked_list.get_size()}")
print(f"Head: {linked_list.head}")

#Task 2: Implement Basic Operations 
# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the element
        self.next = None  # Reference to the next node

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        # Add an element to the end of the list
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node  # Update the tail reference
        self.size += 1
        print(f"Appended {data} to the list")

    def prepend(self, data):
        # Add an element to the beginning of the list
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        print(f"Prepended {data} to the list")

    def get(self, index):
        # Retrieve an element at a specific index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, data):
        # Replace an element at a specific index
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data
        print(f"Set element at index {index} to {data}")

    def get_size(self):
        # Return the current number of elements
        return self.size

    def print_list(self):
        # Print the elements of the linked list
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked list:", elements)

# Example Usage
linked_list = LinkedList()
linked_list.append(5)
linked_list.get(0)
linked_list.set(0, 10)
linked_list.get(0)
print(f"Current size: {linked_list.get_size()}")
linked_list.prepend(10)
linked_list.print_list()
