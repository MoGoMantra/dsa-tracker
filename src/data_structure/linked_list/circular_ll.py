class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSinglyLL:
    def __init__(self):
        self.last = None
    
    def to_list(self):
        lst = []
        if self.last is None:
            return []
        crr = self.last.next
        while True:
            lst.append(crr.data)
            crr = crr.next
            if crr == self.last.next:
                break
        return lst
    
    def insert_at_front(self,value):
        new_node = Node(value)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node
    
    def insert_at_end(self,value):
        new_node = Node(value)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
    
    def insert_at_pos(self, pos, value):
        if not isinstance(pos, int):
            raise TypeError("Position should be integer")
        if pos < 1:
            raise IndexError("Position should be greater or equal to 1")
        new_node = Node(value)
        if pos == 1:
            self.insert_at_front(value)
            return
        if self.last is None:
            raise ValueError("Empty List")
        crr = self.last.next
        for _ in range(pos-2):
            if crr.next == self.last.next:
                raise IndexError("Position is out of bound")
            crr = crr.next
        if crr.next == self.last.next:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
            return
        new_node.next = crr.next
        crr.next = new_node
    

    def delete_at_start(self):
        if self.last is None:
            raise ValueError("Empty List")
        if self.last.next == self.last:
            self.last = None
            return
        self.last.next = self.last.next.next
    
    def delete_at_end(self):
        if self.last is None:
            raise ValueError("Empty List")
        if self.last.next == self.last:
            self.last = None
            return
        crr = self.last.next
        while crr.next != self.last:
            crr = crr.next
        crr.next = self.last.next
        self.last = crr
        # while True:
        #     crr = crr.next
        #     if crr.next == self.last:
        #         crr.next = self.last.next
        #         self.last = crr
        #         return
    
    def delete_at_pos(self,pos):
        if not isinstance(pos, int):
            raise TypeError("Position should be integer")
        if pos < 1:
            raise IndexError("Position should be greater than 1")
        if self.last is None:
            raise ValueError("Empty List")
        if pos == 1:
            self.delete_at_start() # as we are using delete @ start function we are also including the case of only 1 element and pos = 1
            return
        crr = self.last.next 
        for i in range(pos - 2):
            crr = crr.next
            if crr.next == self.last.next:
                raise IndexError("Position is out of bound")
        
        if crr.next == self.last:
            crr.next = self.last.next
            self.last = crr
            return
        
        crr.next = crr.next.next
    
    def delete_node(self, value):
        if self.last is None:
            raise ValueError("Empty List")
        if self.last.next.data == value:
            self.delete_at_start()
            return
        first = self.last.next
        crr = first.next
        while crr!=self.last.next:
            if crr.data == value:
                first.next = crr.next
                if crr == self.last:
                    self.last = first
                return
            first = crr
            crr = crr.next
        raise ValueError("Value Not found")
    
    def delete_list(self):
        if self.last is None:
            raise ValueError("Empty List")
        self.last = None
    
    def is_empty(self):
        if self.last is None:
            return True
        else:
            return False
    
    def search_pos(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position should be integer")
        if pos < 1:
            raise IndexError("Position should be >= 1")
        if self.last is None:
            raise ValueError("Empty List")
        crr = self.last.next
        for i in range(pos - 1):
            if crr.next == self.last.next:
                raise IndexError("Out of bound")
            crr = crr.next
        return crr.data
    
    def search_node(self, value):
        if self.last is None:
            raise ValueError("Empty List")
        crr = self.last.next
        count = 1
        while True:
            if crr.data == value:
                return count
            if crr.next == self.last.next:
                raise ValueError("Not found")
            crr = crr.next
            count+=1
    
    def reverse(self):
        if self.last is None:
            raise ValueError("Empty list")
        if self.last.next == self.last:
            return
        
        prev = self.last
        crr =first = self.last.next
        while True:
            temp = crr.next
            crr.next = prev
            prev = crr
            crr = temp
            if crr == first:
                break
        self.last = first

