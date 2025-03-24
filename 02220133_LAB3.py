#02220133- part 2 (task3 and task4).

### Task3.
# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Data field to store the element
        self.next = None  # Reference to the next node

# Define the LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None   # Reference to the top node (head of the linked list)
        self.size = 0     # Counter to track the number of elements
        print("Created new LinkedStack")

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Push operation
    def push(self, value):
        new_node = Node(value)  # Create a new node
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node  # Update the top to the new node
        self.size += 1  # Increment the size counter

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped_value = self.top.data  # Get the data from the top node
        self.top = self.top.next  # Move top to the next node
        self.size -= 1  # Decrement the size counter
        return popped_value

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

# Example usage
stack = LinkedStack()
print("Stack is empty:", stack.is_empty())  # Output: True


### Task 4.
# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Data field to store the element
        self.next = None  # Reference to the next node

# Define the LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None   # Reference to the top node
        self.size_count = 0  # Counter to track the number of elements
        print("Created new LinkedStack")

    # Push operation
    def push(self, element):
        new_node = Node(element)  # Create a new node
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node       # Update the top to the new node
        self.size_count += 1      # Increment the size counter
        print(f"Pushed {element} to the stack")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped_value = self.top.data  # Get the data from the top node
        self.top = self.top.next      # Update top to the next node
        self.size_count -= 1          # Decrement the size counter
        print(f"Popped element: {popped_value}")
        return popped_value

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    # Check if the stack is empty
    def is_empty(self):
        return self.size_count == 0

    # Return the current size of the stack
    def size(self):
        print(f"Stack size: {self.size_count}")
        return self.size_count

    # Display all elements in the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            print(f"Display stack: {elements}")

# Create a new stack
stack = LinkedStack()

# Push elements
stack.push(10)
stack.display()  # Output: Display stack: [10]

stack.push(20)
stack.display()  # Output: Display stack: [20, 10]

stack.push(30)
stack.display()  # Output: Display stack: [30, 20, 10]

# Peek at the top
stack.peek()  # Output: Top element: 30

# Pop an element
stack.pop()  # Output: Popped element: 30
stack.display()  # Output: Display stack: [20, 10]

# Check size
stack.size()  # Output: Stack size: 2
