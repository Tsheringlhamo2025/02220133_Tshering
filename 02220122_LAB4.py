#       02220122  Part 2 Task 3 and Task 4

# Task 3: Implement Node and LinkedQueue Class Structure

# Node class to store data and reference to next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedQueue class to implement a queue using linked list
class LinkedQueue:
    def __init__(self):
        self.front = None  # Reference to the first node
        self.rear = None   # Reference to the last node
        self.size = 0       # Counter for number of elements
        print("Created new LinkedQueue")
        print(f"Queue is empty: {self.is_empty()}")

    # Check if the queue is empty
    def is_empty(self):
        return self.size == 0

# Example usage
if __name__ == "__main__":
    queue = LinkedQueue()

#Task 4: Implement Linked List-based Queue Operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None
        self._size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        dequeued_element = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        print(f"Dequeued element: {dequeued_element}")
        print("Current queue:", self._format_queue())
        return dequeued_element

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        print(f"Queue size: {self._size}")
        return self._size

    def display(self):
        print("Display queue:", self._format_queue())

    def _format_queue(self):
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + ",".join(elements) + "]" if elements else "null"

# Example usage
queue = LinkedListQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()
queue.size()