from collections import deque

class Node:
    def __init__(self, data: int):
        self.data:  int  = data
        self.left= None
        self.right= None
        self.height = 1      # height of subtree rooted here

    def __init__(self):
        self.root= None
        self._size = 0

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node) -> None:
        node.height = 1 + max(self._height(node.left),self._height(node.right))

    def _rotate_right(self, z) -> Node:
        
        y  = z.left
        T3 = y.right
        y.right = z
        z.left  = T3
        self._update_height(z)
        self._update_height(y)
        return y   # new root of this subtree

    def _rotate_left(self, z: Node):
        
        y  = z.right
        T2 = y.left
        y.left  = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _balance(self, node: Node):
        """Apply the correct rotation(s) to restore AVL balance."""
        self._update_height(node)
        bf = self._balance_factor(node)

        # Left Heavy
        if bf > 1:
            if self._balance_factor(node.left) < 0:      # Left-Right case
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)               # Left-Left case

        # Right Heavy
        if bf < -1:
            if self._balance_factor(node.right) > 0:     # Right-Left case
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)                # Right-Right case

        return node   # already balanced

    def insert(self, data: int):
        """Insert data and rebalance. Duplicates are ignored."""
        self.root, inserted = self._insert(self.root, data)
        if inserted:
            self._size += 1

    def _insert(self, node, data):
        if node is None:
            return Node(data), True
        if data < node.data:
            node.left,  inserted = self._insert(node.left,  data)
        elif data > node.data:
            node.right, inserted = self._insert(node.right, data)
        else:
            return node, False      # duplicate — ignore
        return self._balance(node), inserted

    def delete(self, data):
        """Delete data and rebalance. Returns True if found & deleted."""
        self.root, deleted = self._delete(self.root, data)
        if deleted:
            self._size -= 1
        return deleted

    def _delete(self, node, data):
        if node is None:
            return None, False

        if data < node.data:
            node.left,  deleted = self._delete(node.left,  data)
        elif data > node.data:
            node.right, deleted = self._delete(node.right, data)
        else:
            deleted = True
            # Node with one or no child
            if node.left is None:
                return node.right, deleted
            if node.right is None:
                return node.left,  deleted
            # Node with two children — replace with inorder successor
            successor       = self._min_node(node.right)
            node.data       = successor.data
            node.right, _   = self._delete(node.right, successor.data)

        return self._balance(node), deleted

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, data):
        """BST search. O(log n)"""
        node = self.root
        while node:
            if   data == node.data: return node
            elif data <  node.data: node = node.left
            else:                   node = node.right
        return None

    def is_balanced(self) -> bool:
        """Check AVL balance property for every node."""
        def _check(node):
            if node is None:
                return True
            if abs(self._balance_factor(node)) > 1:
                return False
            return _check(node.left) and _check(node.right)
        return _check(self.root)

    def is_valid_bst(self) -> bool:
        """Check BST ordering property."""
        def _check(node, lo, hi):
            if node is None:
                return True
            if not (lo < node.data < hi):
                return False
            return (_check(node.left,  lo,        node.data) and
                    _check(node.right, node.data,  hi))
        return _check(self.root, float("-inf"), float("inf"))

    def inorder(self) -> list[int]:
        """Inorder of a BST always returns sorted values."""
        result = []
        def _in(node):
            if node:
                _in(node.left); result.append(node.data); _in(node.right)
        _in(self.root)
        return result

    def level_order(self) -> list[int]:
        if not self.root:
            return []
        result, q = [], deque([self.root])
        while q:
            node = q.popleft()
            result.append(node.data)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        return result

    def size(self)     -> int:  return self._size
    def is_empty(self) -> bool: return self._size == 0
    def height(self)   -> int:  return self._height(self.root) - 1  # edges
