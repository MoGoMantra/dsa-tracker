# Tree travesal functions

from collections import deque

class Node:
    """
    Single node representation of a binary Tree consists:
    Attributes:
        -> Data = value stored in node
        -> Left(Node) = Reference to left child node
        -> Right(Node) = Reference to right child node
    """
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    Robust Implementation of a Binary Tree
    Attributes:
        -> root(Node)      = Reference to root node of Binary Tree
        -> pending(dequeu) = queue of pending states
    
    Functionalities:
    continuation_build_tree(array)   -> Build Tree either from scratch or continuing previous one -> O[n]
    serialize_levelorder()           -> levelorder traveral but with every value including Node   -> O[n]
    pending_queue()                  -> return the pending state of a binary tree                 -> O[n]
    inorder()                        -> return the inorder traversal of tree via recursion        -> O[n]
    preorder()                       -> return the preorder traversal of tree via recursion       -> O[n]
    postorder()                      -> return the postorder traversal of tree via recursion      -> O[n]
    preorder_itr()                   -> return preorder traversal of tree via iterative approach  -> O[n]
    inorder_itr()                    -> return inorder traversal of tree via iterative approach   -> O[n]
    postorder_itr()                  -> return postorder traversal of tree via iterative approach -> O[n]
    count()                          -> return total no. of nodes in tree                         -> O[n]
    count_deg2()                     -> return total no. of degree 2 nodes in tree                -> O[n]
    count_deg1()                     -> return total no. of degree 1 nodes in tree                -> O[n]
    count_leaf()                     -> return total no. of leaf nodes in tree                    -> O[n]
    count_internal()                 -> return total no. of Internal nodes in tree                -> O[n]
    sum_nodes()                      -> return sum of all nodes in tree                           -> O[n]
    height()                         -> return the height of binary tree                          -> O[n]
    Inorder_search(i, v, s, e)       -> return the index of v in i within range s to e            -> O[n]
    buildTreeRecursion(),buildTree() ->build binary tree from preorder and inorder                -> O[n^2]
    btr_in_post_recur(),btr_in_post()->build binary tree from postorder and inorder               -> O[n^2]
    """
    def __init__(self):
        self.root = None
        self.pending = deque() # class attribute for accounting of last pending state tells last leave nodes
        # next slot:
        # 0 if next insertion at left
        # 1 if next insertion at right
    
    def continuation_build_tree(self, num):
        """
        Building a binary tree either from scratch or with previous continuity
        In this build any type of binary tree can be constructed with an array input 
        Array input consists of level order and in absence of any child it should be None in the array
        """
        if not num:
            return self.root
        
        i =0

        if self.root is None:
            if num[0] is None:
                raise ValueError("root can't be None")
            self.root = Node(num[0])
            i+=1
            self.pending.append((self.root,0))
        
        n = len(num)
        while i<n:
            if not self.pending:
                raise RuntimeError("Alrady fully constructed no room to further extend")
            parent,slot = self.pending.popleft()
            if slot == 0:
                if num[i] is not None:
                    parent.left = Node(num[i])
                    self.pending.append((parent.left, 0)) # adding left children 
                # parent is yet to be finished 
                # insertion for right children
                i+=1
                self.pending.appendleft((parent,1))
            
            else:
                if num[i] is not None:
                    parent.right = Node(num[i])
                    self.pending.append((parent.right,0))
                    # parent traverse done
                i+=1
        
        return self.root
    
    def serialize_levelorder(self):
        """
        Level order traversal of Binary tree
        Keeping the 'None' in case of absence of any children
        """
        res = []
        q = deque([self.root])
        while q:
            crr = q.popleft()
            if crr:
                res.append(crr.data)
                q.append(crr.left)
                q.append(crr.right)
            else:
                res.append(None)
        
        while res and res[-1] is None:
            res.pop()
        
        return res
    
    def pending_queue(self):
        """
        Pending nodes to be produced children 
        """
        return [(node.data, "left" if slot == 0 else "right") for node,slot in self.pending]

    def inorder(self):
        """
        Recursive Inorder tree Traversal Function
        Inorder = Left Child -> Parent -> Right Child
        """
        res = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.data)
                _inorder(node.right)
    
        _inorder(self.root)
        return res
    
    def preorder(self):
        """
        Recursive Preorder tree Traversal Function
        Preorder =  Parent -> Left Child -> Right Child
        """
        res = []
        def _preorder(node):
            if node:
                res.append(node.data)
                _preorder(node.left)
                _preorder(node.right)
        
        _preorder(self.root)
        return res
    
    def postorder(self):
        """
        Recursive Postorder tree Traversal Function
        Postorder =  Left Child -> Right Child -> Parent 
        """
        res = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                res.append(node.data)
        
        _postorder(self.root)
        return res
    
    def levelorder(self):
        """
        Level wise tree traversal
        Using queue to access all level nodes
        """
        if self.root is None:
            return []
        res = []
        q = deque([self.root])
        while q:
            crr = q.popleft()
            res.append(crr.data)
            if crr.left:
                q.append(crr.left)
            if crr.right:
                q.append(crr.right)
        
        return res
    
    # Iterative approach of traversals

    def preorder_itr(self):
        res = []
        st = []
        crr = self.root
        while (crr is not None) or len(st) > 0:
            if crr:
                res.append(crr.data)
                st.append(crr)
                crr = crr.left
            else:
                crr=st.pop()
                crr = crr.right
        
        return res
    
    def inorder_itr(self):
        res = []
        st = []
        crr = self.root
        while (crr is not None) or len(st) > 0:
            if crr:
                st.append(crr)
                crr = crr.left
            else:
                crr = st.pop()
                res.append(crr.data)
                crr = crr.right
        
        return res
    
    def postorder_itr(self):
        res = []
        st =[]
        lvn = None
        crr = self.root
        while crr or st:
            if crr:
                st.append(crr)
                crr = crr.left
            else:
                temp = st[-1]
                if temp.right and temp.right != lvn:
                    crr = temp.right
                else:
                    res.append(temp.data)
                    lvn = st.pop()
        
        return res
    
    def count(self):
        """Total no. of nodes"""
        def _count(node):
            if node:
                return _count(node.left) + _count(node.right) + 1
            else:
                return 0
        
        return _count(self.root)
    
    def count_deg2(self):
        """No. of nodes with 2 children"""
        def _count2(node):
            if node:
                if node.left and node.right:
                    return _count2(node.left) + _count2(node.right) + 1
                else:
                    return _count2(node.left) + _count2(node.right)
            else:
                return 0
        
        return _count2(self.root)
    
    def count_deg1(self):
        """No. of nodes with exactly 1 child"""
        def _count1(node):
            if not node:
                return 0
            if node.left and not node.right:
                return 1+_count1(node.left)
            if node.right and not node.left:
                return 1 + _count1(node.right)
            return _count1(node.left) + _count1(node.right)
        
        return _count1(self.root)
    
    def count_leaf(self):
        """Counts the total no. of leaf nodes"""
        def _count_leaf(node):
            if not node:
                return 0 
            if not node.left and not node.right:
                return 1
            return _count_leaf(node.left) + _count_leaf(node.right)
        
        return _count_leaf(self.root)
    
    def count_internal(self):
        """Counts the total no. of Internal Nodes = 1child + 2 child"""
        def _count_internal(node):
            if not node:
                return 0
            if node.left or node.right:
                return _count_internal(node.left) + _count_internal(node.right) + 1
            
            return 0
        
        return _count_internal(self.root)
    
    def sum_nodes(self):
        """Return the sum of all node values"""
        def _sum_nodes(node):
            if node:
                return _sum_nodes(node.left) + _sum_nodes(node.right) + node.data
            else:
                return 0
        
        return _sum_nodes(self.root)
    
    def height(self):
        """Calculate the height of tree"""
        def _height(node):
            if not node:
                return -1 # to compensate in case of only 1 level so height will be 0
            return max(_height(node.left), _height(node.right)) + 1 
        
        return _height(self.root)
    
    def Inorder_search(self, inOrder, value, start, end):
        """Search for a node in Inorder Travesal"""
        for i in range(start, end+1):
            if inOrder[i] == value:
                return i
        return -1
    
    def buildTreeRecursion(self, preOrder, inOrder, pI, start, end):
        """Build Tree from Inorder and Preorder"""
        if start>end:
            return None
        rootValue = preOrder[pI[0]]
        pI[0] += 1
        root = Node(rootValue)
        Index = self.Inorder_search(inOrder, rootValue, start, end)
        root.left = self.buildTreeRecursion(preOrder, inOrder, pI, start, Index-1)
        root.right = self.buildTreeRecursion(preOrder, inOrder, pI, Index+1, end)

        return root

    def buildTree(self, preOrder,inOrder):
        pI = [0] # Because int is immutable but list is mutable hence behave like static variable 
        self.root = self.buildTreeRecursion(preOrder, inOrder, pI, 0, len(preOrder) -1)
        return self.root

    def btr_in_post_recur(self, postOrder, inOrder, postIndex,start, end):
        """Building tree from postorder and inorder"""
        if start>end: #Base Case for recursion
            return None
        
        root_value = postOrder[postIndex[0]]
        postIndex[0] -= 1
        root = Node(root_value)
        Index = self.Inorder_search(inOrder, root_value, start, end)

        root.right = self.btr_in_post_recur(postOrder, inOrder, postIndex, Index+1, end)
        root.left = self.btr_in_post_recur(postOrder, inOrder, postIndex, start, Index-1)

        return root
    
    def btr_in_post(self, postOrder, inOrder):
        n = len(inOrder)
        postIndex = [n-1]
        self.root = self.btr_in_post_recur(postOrder, inOrder, postIndex, 0, n-1)
        return self.root
    