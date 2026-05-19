class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def isEmpty(self):
        return (self.front is None)
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.isEmpty():
            self.front = self.rear = new_node
            self._size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self._size +=1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        v = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -=1
        return v
    
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        return self.front.data
    
    def getRear(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        return self.rear.data
    
    def size(self):
        return self._size
    
    def to_list(self):
        lst = [] 
        crr = self.front
        while crr:
            lst.append(crr.data)
            crr = crr.next
        return lst
