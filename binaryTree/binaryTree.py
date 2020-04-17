class Node(object):
    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data

    @property
    def value(self):
        return self._data
    
    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right
    
    @value.setter
    def value(self, data):
        self._data = data
    
    @left.setter
    def left(self, newLeft):
        self._left = newLeft

    @right.setter
    def right(self, newRight):
        self._right = newRight

class BinaryTree(object):
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        assert(node is not None)
        if node.value > data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def traverseLevelOrder(self):
        h = self.height(self.root)
        for i in range(1, h+1):
            self.traverseGivenLevel(self.root, i)

    def traverseGivenLevel(self, node, h):
        if not node:
            return
        if h == 1:
            print('%d ' % node.value)
        elif h > 1:
            self.traverseGivenLevel(node.left, h-1)
            self.traverseGivenLevel(node.right, h-1)

    def height(self, node):
        if not node:
            return 0
        else:
            lHeight = self.height(node.left)
            rHeight = self.height(node.right)
            return lHeight+1 if lHeight > rHeight else rHeight+1

    def traverseLevelOrder_v2(self):
        h = 1
        while self.traverseGivenLevel_v2(self.root, h):
            h += 1

    def traverseGivenLevel_v2(self, node, h):
        if not node:
            return False
        
        if h == 1:
            print('%d' % node.value)
            return True
        
        left = self.traverseGivenLevel_v2(node.left, h-1)
        right = self.traverseGivenLevel_v2(node.right, h-1)

        return left or right

    def BFS(self):
        if self.root is None:
            return
        
        queue = []

        queue.append(self.root)
        while queue:
            print(queue[0].value)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
    
    def inorder_traverse(self):
        self._inorder(self.root)

    def _inorder(self, node):
        '''
        inorder traversal order: 
        1.left subtree
        2.root node
        3.right subtree
        '''
        if not node:
            return
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

    def preorder_traverse(self):
        self._preorder(self.root)

    def _preorder(self, node):
        '''
        preorder traversal order:
        1.root node
        2.left subtree
        3.right subtree
        '''
        if not node:
            return
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)

    def postorder_traverse(self):
        self._postorder(self.root)

    def _postorder(self, node):
        '''
        postorder traversal order:
        1.left subtree
        2.right subtree
        3.root node
        '''
        if not node:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value)
        
if __name__ == "__main__":
    testTree = BinaryTree(Node(10))
    testTree.insert(2)
    testTree.insert(3)
    testTree.insert(11)
    testTree.insert(34)
    testTree.insert(4)
    testTree.traverseLevelOrder()
    print('v2:')
    testTree.traverseLevelOrder_v2()
    print('BFS(with queue)')
    testTree.BFS()
    print('inorder traversal:')
    testTree.inorder_traverse()
    print('preorder tarversal:')
    testTree.preorder_traverse()
    print('postorder traversal:')
    testTree.postorder_traverse()

    
