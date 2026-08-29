# Tshering lhamo - part1 ( Queue Implementation using Array )

# Task 1 (Implement the ArrayQueue Class Structure )
class ArrayQueue:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._array = [None] * capacity
        # Variables to track the front and rear indices
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = capacity
        print(f"Created new Queue with capacity: {capacity}")
    
    def is_empty(self):
        return self._size == 0

# Example Output
queue = ArrayQueue()  # Default capacity is 10
print(f"Queue is empty: {queue.is_empty()}")

#Task 2 (Implement Array-based Queue Operations)
class ArrayQueue:
    def __init__(self, capacity=10):
        self._array = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = capacity
        print(f"Created new Queue with capacity: {capacity}")

    def is_empty(self):
        return self._size == 0

    def enqueue(self, element):
        if self._size == self._capacity:
            raise Exception("Queue is full")
        self._array[self._rear] = element
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        element = self._array[self._front]
        self._array[self._front] = None  # Optional: Clear the slot
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        print(f"Dequeued element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._array[self._front]

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            queue = []
            index = self._front
            for _ in range(self._size):
                queue.append(self._array[index])
                index = (index + 1) % self._capacity
            print(f"Display queue: {queue}")

# Example Usage
queue = ArrayQueue()

queue.enqueue(10)
queue.display()

queue.enqueue(20)
queue.display()

queue.enqueue(30)
queue.display()

print(f"Front element: {queue.peek()}")
queue.dequeue()
queue.display()

print(f"Queue size: {queue.size()}")
