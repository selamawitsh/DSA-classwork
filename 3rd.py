class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        return not (self.stack1 or self.stack2)

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: 3

print("Dequeue:", queue.dequeue())  # Output: 1
print("Dequeue:", queue.dequeue())  # Output: 2

queue.enqueue(4)
queue.enqueue(5)

print("Peek:", queue.peek())  # Output: 3
print("Dequeue:", queue.dequeue())  # Output: 3

print("Is empty:", queue.is_empty())  # Output: False

print("Dequeue:", queue.dequeue())  # Output: 4
print("Dequeue:", queue.dequeue())  # Output: 5

print("Is empty:", queue.is_empty())  # Output: True
