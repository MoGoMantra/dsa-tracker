from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class PBT:
    def __init__(self):
        self.root = None
        self._size = 0
    
    def is_perfact_size(self, n):
        return (n>0 and ( (n & (n+1)) == 0))
    
    def build_tree(self, arr):
        if not arr:
            return self.root
        n = len(arr)

        if not self.is_perfact_size(n):
            raise ValueError("Not a PBT")
        
        self.root = Node(arr[0])
        self._size +=1
        q = deque([self.root])
        i = 1
        while i<n:
            crr = q.popleft()
            if i<n:
                crr.left = Node(arr[i])
                q.append(crr.left)
                i +=1
                self._size +=1
            if i<n:
                crr.right = Node(arr[i])
                q.append(crr.right)
                i +=1
                self._size +=1
        return self.root
    
    def isPBT(self):
        if self.root is None:
            return False
        return self.is_perfact_size(self._size)
    
    def insert(self, key):
        if self.isPBT():
            raise ValueError("No insertion allowed in already PBT")
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            self._size +=1
            return self.root
        q = deque([self.root])
        while q:
            crr = q.popleft()
            if crr.left:
                q.append(crr.left)
            else:
                crr.left = new_node
                self._size +=1
                break
            if crr.right:
                q.append(crr.right)
            else:
                crr.right = new_node
                self._size +=1
                break
        return self.root
    
    def size(self):
        return self._size
    
    def height(self):
        if self.root is None:
            raise ValueError("Empty Tree")
        h = 0
        crr = self.root
        while crr.left:
            h+=1
            crr = crr.left
        return h
    
    def leaf_count(self):
        lc = 0
        if self.root is None:
            return 0
        return (2**(self.height()))
    
    def internal_nodes(self):
        return (self.leaf_count() - 1)
    
    def level_count(self):
        return (self.height() + 1)
    
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
    
    def leaves(self):
        res = []
        def _leafRecusive(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                res.append(node.data)
                return
            _leafRecusive(node.left)
            _leafRecusive(node.right)
        _leafRecusive(self.root)
        return res
    
    def level_nodes(self, level):
        if level < 0:
            raise ValueError("Invalid")
        result = []
        def _dfs(node, lev):
            if node is None:
                return
            if lev == level:
                result.append(node.data)
                return
            _dfs(node.left, lev+1)
            _dfs(node.right, lev+1)
        _dfs(self.root, 0)
        return result
    
    def isPBT(self):
        h = self.height()
        def _check(node, depth, level):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return depth == level
            if node.left is None or node.right is None:
                return False
            return (_check(node.left, depth, level+1) and _check(node.right, depth, level+1))
        
        return _check(self.root, h, 0)


    def isFullBinaryTree(self):
        def _check(node):
            if node is None:
                return True # considering empty BT is FBT but not PBT                
            if node.left is None and node.right is None:
                return True
            if node.left is None or node.right is None:
                return False        # using short circuit
            
            return (_check(node.left) and _check(node.right))
        
        return _check(self.root)