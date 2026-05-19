class QueueArrFix:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [None]*cap
        self.size = 0
    
    def enqueue(self, x):
        if self.size == self.capacity:
            raise OverflowError("Queue Overflow")
        self.arr[self.size] = x
        self.size+=1
    
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        v = self.arr[0]
        for i in range(self.size):
            self.arr[i] = self.arr[i+1]
        self.size-=1
        return v
    
    def getFront(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        return self.arr[0]
    
    def getRear(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        return self.arr[self.size - 1]
    
    def size(self):
        return self.size
    
    def isEmpty(self):
        return (self.size == 0)
    
    def isFull(self):
        return (self.size == self.capacity)
    
    def to_list(self):
        lst = []
        for i in range(self.size):
            lst.append(self.arr[i])
        return lst