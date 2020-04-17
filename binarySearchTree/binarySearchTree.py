class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None 
        self.right = None

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root
        self.stack = []

    def find(self, data):
        return self._find(self.root, data)

    def _find(self, node, data):
        if not node:
            return False
        if node.value == data:
            return True
        elif node.value > data:
            return self._find(node.left, data)
        else:
            return self._find(node.right, data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node.value == data:
            return
        elif node.value > data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
    
    def inorder_stack(self):
        current = self.root
        while current:
            self.stack.append(current)
            current = current.left

    def __iter__(self):
        '''
        iterator for binary search tree
        using inorder traversal
        '''
        self.inorder_stack()
        while len(self.stack) != 0:
            next_node = self.stack.pop()
            current = next_node.right
            while current:
                self.stack.append(current)
                current = current.left
            yield next_node

if __name__ == "__main__":
    BST = BinarySearchTree()
    BST.insert(5)
    BST.insert(5)
    BST.insert(2)
    BST.insert(1)
    BST.insert(3)
    BST.insert(9)
    BST.insert(10)
    BST.insert(8)
    print(BST.find(3))
    print(BST.find(8))
    print(BST.find(11))
    print('inorder traverse:')
    for node in BST:
        if node:
            print(node.value)
    