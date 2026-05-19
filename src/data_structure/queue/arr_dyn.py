class QueueArrDyn:
    def __init__(self):
        self.arr = []
        self._size = 0
    
    def size(self):
        return self._size
    
    def enqueue(self, x):
        self.arr.append(x)
        self._size += 1
    
    def dequeue(self):
        if self._size == 0:
            raise IndexError("Empty Queue")
        removed_value = self.arr.pop(0)
        self._size -= 1
        return removed_value
    
    def getFront(self):
        if self._size == 0:
            raise IndexError("Empty Queue")
        return self.arr[0]
    
    def getRear(self):
        if self._size == 0:
            raise IndexError("Empty Queue")
        return self.arr[self.size() - 1]
    
    def isEmpty(self):
        return self._size == 0
    
    def to_list(self):
        return self.arr