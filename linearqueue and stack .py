# #1
# def LinearQueue():
#   queue = {"items": [], "front": None, "rear": None}
#   return queue

# def isEmpty(queue):
#   return queue["front"] is None

# def size(queue):
#       return len(queue["items"])

# def enqueue(queue, item):

#   if isEmpty(queue):
#     queue["front"] = queue["rear"] = item
#   else:
#     queue["items"].append(item)
#     queue["rear"] = queue["items"][-1]

# def dequeue(queue):
#   if isEmpty(queue):
#     return "Queue is empty"
#   item = queue["front"]
#   if queue["front"] == queue["rear"]:
#     queue["front"] = queue["rear"] = None
#   else:
#     queue["front"] = queue["items"][1]
#   return item

# def peek(queue):
#   if isEmpty(queue):
#      print("Queue is empty")
#   return queue["front"]
# myQueue = LinearQueue()

# enqueue(myQueue, 1)
# enqueue(myQueue, 2)

# print(dequeue(myQueue)) 
# print(peek(myQueue)) 
# print(size(myQueue))  



#2 circular queue
# def CircularQueue(maxSize):
#   queue = [None] * maxSize 
#   front = -1 
#   rear = -1 
#   return queue, front, rear

# def isEmpty(queue, front):
  
#   return front == -1

# def isFull(queue, maxSize, rear):
#   return (rear + 1) % maxSize == front

# def size(queue, front, rear):
#   if isEmpty(queue, front):
#     return 0
#   return (rear + 1) % maxSize - front

# def enqueue(queue, maxSize, rear, item):
#   if isFull(queue, maxSize, rear):
#     raise IndexError("Queue overflow")

#   if isEmpty(queue, rear):
#     front = 0 
#   rear = (rear + 1) % maxSize
#   queue[rear] = item  

# def dequeue(queue, maxSize, front):
#   if isEmpty(queue, front):
#     raise IndexError("Queue underflow")

#   item = queue[front]  
#   queue[front] = None 

#   if front == rear:
#     front = rear = -1 
#   else:
#     front = (front + 1) % maxSize  

#   return item

# def peek(queue, front):
#   if isEmpty(queue, front):
#     raise IndexError("Queue is empty")
#   return queue[front]

# maxSize = 5
# queue, front, rear = CircularQueue(maxSize)  

# enqueue(queue, maxSize, rear, 1)
# enqueue(queue, maxSize, rear, 2)
# enqueue(queue, maxSize, rear, 3)

# print(dequeue(queue, maxSize, front))




class LinearQueue:
  """
  A simple implementation of a linear queue using a list.
  """
  def __init__(self, maxSize):
    """
    Initializes the queue with a maximum size.

    Args:
        maxSize: The maximum number of elements the queue can hold.
    """
    self.items = [None] * maxSize  # Pre-allocate space for efficiency
    self.front = 0  # Initially, queue is empty (front points to the first element)
    self.rear = -1  # Initially, queue is empty (rear points to nothing)
    self.maxSize = maxSize  # Store the maximum size for reference

  def isEmpty(self):
    """
    Checks if the queue is empty.

    Returns:
        True if the queue is empty, False otherwise.
    """
    return self.front > self.rear  # Queue is empty when front is ahead of rear

  def isFull(self):
    """
    Checks if the queue is full.

    Returns:
        True if the queue is full, False otherwise.
    """
    return self.rear == self.maxSize - 1  # Queue is full when rear reaches the end

  def enqueue(self, item):
    """
    Inserts an item at the rear of the queue (enqueue).

    Args:
        item: The item to be enqueued.

    Raises:
        IndexError: If the queue is full.
    """
    if self.isFull():
      raise IndexError("Queue overflow")
    self.rear += 1  # Update rear to point to the next position
    self.items[self.rear] = item  # Add the item to the rear position

  def dequeue(self):
    """
    Removes and returns the item at the front of the queue (dequeue).

    Returns:
        The item at the front of the queue.

    Raises:
        IndexError: If the queue is empty.
    """
    if self.isEmpty():
      raise IndexError("Queue underflow")
    item = self.items[self.front]  # Get the item at the front
    self.front += 1  # Update front to point to the next element
    return item

  def peek(self):
    """
    Returns the item at the front of the queue without removing it.

    Raises:
        IndexError: If the queue is empty.
    """
    if self.isEmpty():
      raise IndexError("Queue is empty")
    return self.items[self.front]  # Return the item at the front

# Example usage
myQueue = LinearQueue(5)

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print(myQueue.dequeue())  # Output: 1
print(myQueue.peek())    # Output: 2
