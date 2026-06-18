from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class CompleteBT:
    def __init__(self):
        self.root = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def isEmpty(self):
        return (self.root is None)
    
    def height(self):
        if self.root is None:
            raise ValueError("Empty Tree")
        h = 0
        crr = self.root
        while crr.left:
            crr = crr.left
            h+= 1
        return h
    
    def insert(self, arr):
        if not arr:
            return self.root
        self.root = Node(arr[0])
        self._size += 1
        n = len(arr)
        q = deque([self.root])
        i = 1
        while i<n:
            crr = q.popleft()
            if i<n:
                crr.left = Node(arr[i])
                q.append(crr.left)
                i += 1
                self._size +=1
            if i<n:
                crr.right = Node(arr[i])
                q.append(crr.right)
                i+=1
                self._size += 1
        return self.root
    
    def delete(self, key):
        if self.root is None:
            raise ValueError("Empty Tree")
        # Edge case only root node and data found
        if self._size == 1:
            if self.root.data == key:
                self.root = None
                self._size -= 1
                return self.root
            raise ValueError("Value Not Found")
        
        target = None
        last = None
        last_parent = None
        isLeft = False
        q = deque([(self.root, None, False)])
        while q:
            crr, parent, left = q.popleft()
            if crr.data == key:
                target = crr
            last = crr
            last_parent = parent
            isLeft = left
            if crr.left:
                q.append((crr.left, crr, True))
            if crr.right:
                q.append((crr.right, crr, False))
        
        if target is None:
            raise ValueError("Not Found")
        target.data = last.data

        if isLeft:
            last_parent.left = None
        else:
            last_parent.right = None
        
        self._size -= 1
        return self.root
    
    def search(self, key):
        if self.root is None:
            raise ValueError("Empty List")
        q = deque([self.root])
        while q:
            crr = q.popleft()
            if crr.data == key:
                return True
            if crr.left:
                q.append(crr.left)
            if crr.right:
                q.append(crr.right)
        return False
    
    def levelOrder(self):
        if self.root is None:
            return []
        res, q = [], deque([self.root])
        while q:
            crr = q.popleft()
            res.append(crr.data)
            if crr.left:
                q.append(crr.left)
            if crr.right:
                q.append(crr.right)
        return res
    
    def inOrder(self):
        if self.root is None:
            return []
        res = []        # two function as we do not want to reinitialize the res variable each recursion

        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.data)
                _inorder(node.right)
        
        _inorder(self.root)
        return res
    
    def preOrder(self):
        if self.root is None:
            return []
        res = []

        def _preorder(node):
            if node:
                res.append(node.data)
                _preorder(node.left)
                _preorder(node.right)
        
        _preorder(self.root)
        return res
    
    def postOrder(self):
        if self.root is None:
            return []
        res = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                res.append(node.data)
        
        _postorder(self.root)
        return res
    
    def isComplete(self):
        if self.root is None:
            return True
        flag = False # is incomplete
        q = deque([self.root])
        while q:
            crr = q.popleft()
            if crr.left:
                if flag:
                    return False
                else:
                    q.append(crr.left)
            else:
                flag = True
            if crr.right:
                if flag:
                    return False
                else:
                    q.append(crr.right)
            else:
                flag = True
        
        return True
    
    def levelPrint(self):
        if self.root is None:
            return []
        q = deque([(self.root, 0)])
        crr_level = 0
        line = []
        res = []
        while q:
            crr, level = q.popleft()
            if level != crr_level:
                res.append(line)
                line = []
                crr_level = level
            line.append(crr.data)
            if crr.left:
                q.append((crr.left, level +1))
            if crr.right:
                q.append((crr.right, level +1))
        if line:
            res.append(line)
        return res
    


