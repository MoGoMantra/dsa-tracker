class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

                                # INSERT

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        # duplicates ignored

                                # SEARCH

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.data:
            return True
        if value < node.data:
            return self._search(node.left, value)
        return self._search(node.right, value)

                                # DELETE

    def delete(self, value):
        if self.root is None:
            raise ValueError("Empty tree")
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            raise ValueError(f"{value} not found in tree")
        if value < node.data:
            node.left = self._delete(node.left, value)
        elif value > node.data:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None and node.right is None:   # leaf
                return None
            if node.left is None:                          # one child
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_node(node.right)         # two children
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

                                # TRAVERSALS

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)
    
    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def max_value(self):
        if self.root is None:
            raise ValueError("Empty tree")
        crr = self.root
        while crr.right:
            crr = crr.right
        return crr.data    
    

    def is_empty(self):
        return self.root is None
    
    def demo():
        pass
    
