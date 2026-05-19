class Node:
    def __init__(self, v):
        self.data = v
        self.prev = None
        self.next = None


class DeQueue:
    def __init__(self):
        self.front = self.rear = None
        self._size = 0
    
    def insertFront(self, x):
        if self.front is None:
            self.front = self.rear = Node(x)
            return
        N = Node(x)
        N.next = self.front 
        self.front.prev = N
        self.front = N
        self._size += 1
    
    def insertRear(self, x):
        if self.front is None:
            self.front = self.rear = Node(x)
            return
        N = Node(x)
        self.rear.next = N
        N.prev = self.rear
        self.rear = N
        self._size += 1
    
    def deleteFront(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        v = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
            return v
        self.front = self.front.next
        self.front.prev = None
        self._size -= 1
        return v
    
    def deleteRear(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        v = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
            return v
        self.rear = self.rear.prev
        self.rear.next = None
        self._size -= 1
        return v
    
    def isEmpty(self):
        return (self.front is None)
    
    def getFront(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        return self.front.data
    
    def getRear(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        return self.rear.data
    
    def size(self):
        return self._size
    
    def to_list(self):
        if self.front is None:
            return []
        lst = []
        crr = self.front
        while crr:
            lst.append(crr.data)
            crr = crr.next
        return lst
    

