import numpy as np

# DSA Queue class
class DSAQueue():
    def __init__(self, capacity=100):
        self.queue = np.zeros(capacity, dtype=object)
        self.capacity = capacity
        self.front = 0  # for circular queue 1st element of queue
        self.rear = 0  # for circular queue last element
        self.count = 0

    def getCount(self):
        return self.count

# DSA Circular Queue
class Circular_Queue(DSAQueue):
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, value):  # take a value add it to end of queue
        if self.isFull():  # if queue is full
            raise Exception("Queue is Full")
        else:
            self.queue[self.rear] = value  # add val to rear pointer & update it to point to next index
            self.rear = (self.rear + 1) % self.capacity  # once rear pointer reach end queue, wrap arnd the beginning of queue
            self.count += 1

    def dequeue(self):  # remove and return the 1st item in queue
        if self.isEmpty():  # check queue whether empty or not
            raise Exception("Queue is empty")
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity  # once front pointer reach end queue, wrap arnd the beginning of queue
        self.count -= 1
        return temp

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:  # retrieve 1st value in the front queue
            return self.queue[self.front]


# DSA Stack class
class DSAStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        return self.stack[-1]

