# 02220122 - Part 1(Task 1 and Task 2)

#Task 1
class ArrayStack:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._stack = [None] * capacity  # Initialize an array with given capacity
        # Variable to track the top of the stack
        self._top = -1  # Indicates stack is empty
        print(f"Created new ArrayStack with capacity: {capacity}")

    def is_empty(self):
        # Check if the stack is empty
        return self._top == -1

# Create an instance of ArrayStack with default capacity 10
stack = ArrayStack()

# Check if the stack is empty and print the result
print("Stack is empty:", stack.is_empty())


#Task 2
class ArrayStack:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._stack = [None] * capacity  # Initialize an array with given capacity
        # Variable to track the top of the stack
        self._top = -1  # Indicates stack is empty
        self._capacity = capacity  # Store capacity for boundary check
        print(f"Created new ArrayStack with capacity: {capacity}")

    def is_empty(self):
        # Check if the stack is empty
        return self._top == -1
    
    def push(self, element):
        # 1. Push operation - Add an element to the top of the stack
        if self._top + 1 == self._capacity:
            print("Stack overflow! Cannot push element.")
            return
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")
    
    def pop(self):
        # 2. Pop operation - Remove and return the element at the top
        if self.is_empty():
            print("Stack underflow! Cannot pop element.")
            return None
        popped_element = self._stack[self._top]
        self._top -= 1
        print(f"Popped element: {popped_element}")
        return popped_element
    
    def peek(self):
        # 3. Peek operation - Return the element at the top without removing it
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]
    
    def size(self):
        # 4. Size operation - Return the current number of elements
        print(f"Stack size: {self._top + 1}")
        return self._top + 1
    
    def display(self):
        # 5. Display operation - Show all elements in the stack
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Display stack:", [self._stack[i] for i in range(self._top + 1)])

# Create an instance of ArrayStack with default capacity 10
stack = ArrayStack()

# Perform stack operations as per the example output
stack.push(10)  # Push 10
stack.display()  # Display stack
stack.push(20)  # Push 20
stack.display()  # Display stack
stack.push(30)  # Push 30
stack.display()  # Display stack
stack.peek()  # Get the top element
stack.pop()  # Pop the top element
stack.size()  # Get the size of the stack
stack.display()  # Display stack
