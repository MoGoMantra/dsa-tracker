class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Circular array implementation is important as it removes the fixed array problems, LL implementation is just for understanding
class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.front is None:
            self.front = self.rear = new_node
        
        self.rear.next = new_node
        new_node.next = self.front
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        v = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
            return
        self.rear.next = self.front.next
        self.front = self.front.next
        return v
    
    def to_list(self):
        lst = []
        if self.front is None:
            return []
        crr = self.front
        while True:
            lst.append(crr.data)
            if crr == self.rear:
                break
            crr = crr.next
        return lst
    
    def size(self):
        size = 1
        crr = self.front
        while crr!=self.rear:
            size+=1
            crr = crr.next
        return size
