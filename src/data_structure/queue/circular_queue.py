class CircularQueue:

    def __init__(self, n):
        self.capacity = n
        self.arr = [None]*n
        self.front = 0
        self._size = 0
    
    def enqueue(self, x):
        if self._size == self.capacity:
            raise OverflowError("Queue overflow")
        rear = (self.front + self._size)%self.capacity
        self.arr[rear] = x
        self._size+=1
    
    def dequeue(self):
        if self._size == 0:
            raise IndexError("Empty Queue")
        v = self.arr[self.front]
        self.front = (self.front + 1)%self.capacity
        self._size-=1
        return v
    
    def getFront(self):
        if self._size == 0:
            raise IndexError("Empty Queue")
        return self.arr[self.front]
    
    def getRear(self):
        if self._size == 0:
            raise IndexError("Empty Queue")
        rear = (self.front + self._size - 1) % self.capacity
        return self.arr[rear]
    
    def isEmpty(self):
        return (self._size == 0)
    
    def isFull(self):
        return (self._size == self.capacity)
    
    def to_list(self):
        lst = []
        if self._size == 0:
            return []
        for i in range(self._size):
            lst.append(self.arr[(i+self.front)%self.capacity])
        return lst
    
    def size(self):
        return self._size
    