class LinkedList(object):
    ''' class linked list
    '''
    class __Node:
        ''' inner class Node
        data node inner use for linded list, contains data and next link
        '''
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def setVal(self, data):
            self.data = data

        def setNext(self, node):
            self.next = node

        def getNext(self):
            return self.next

    def __init__(self):
        self.head = LinkedList.__Node(None)
    
    def append(self, data):
        iterNode = self.head
        while iterNode.getNext() is not None:
            iterNode = iterNode.getNext()
        iterNode.setNext(LinkedList.__Node(data))
    
    def __iter__(self):
        iterNode = self.head
        while iterNode.getNext() is not None:
            yield iterNode.getNext()
            iterNode = iterNode.getNext()

if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    for node in l1:
        print(node.data)



