class MyDequeu:
    def __init__(self, n):
        self.capacity = n
        self.arr = [None]*n
        self._size = 0
        self.front = 0
    
    def isEmpty(self):
        return self._size == 0
    
    def isFull(self):
        return self._size == self.capacity
    
    def size(self):
        return self._size
    
    def insertFront(self, x):
        if self.isFull():
            raise OverflowError("Queue is maxed out")
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = x
        self._size +=1
    
    def insertRear(self, x):
        if self.isFull():
            raise OverflowError("Queue is Maxed out")
        r = (self.front + self._size) % self.capacity
        self.arr[r] = x
        self._size +=1
    
    def deleteFront(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        v = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self._size -=1
        return v
    
    def deleteRear(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        r = (self.front + self._size -1 ) % self.capacity
        v = self.arr[r]
        self.arr[r] = None
        self._size -= 1
        return v
    
    def GetFront(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        return self.arr[self.front]
    
    def GetRear(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        return self.arr[(self.front + self._size -1 ) % self.capacity]
    
    def to_list(self):
        if self.isEmpty():
            return []
        lst = []
        for i in range(self._size):
            index = (i + self.front) % self.capacity
            lst.append(self.arr[index])
        return lst
