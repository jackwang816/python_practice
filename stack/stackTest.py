class Stack(object):
    def __init__(self, list=None):
        self.list = list or []
        self.size = len(self.list)

    def pop(self):
        assert(self.size > 0)
        self.size -= 1
        return self.list.pop()

    def push(self, item):
        assert(item is not None)
        self.size += 1
        self.list.append(item)

    def peek(self):
        return self.list[-1] if self.size > 0 else None

    def printDebug(self):
        print("Stack size: %d, list:%s" % (self.size, str(self.list)))

    def getLen(self):
        return self.size

def testStack():
    test_stack = Stack()
    assert(test_stack.peek() is None)
    assert(test_stack.getLen() == 0)
    test_stack.push(0)
    assert(test_stack.getLen() == 1)
    assert(test_stack.peek() == 0)
    test_stack.push(1)
    assert(test_stack.peek() == 1)
    assert(test_stack.pop() == 1)
    assert(test_stack.getLen() == 1)
    assert(test_stack.pop() == 0)

if __name__ == "__main__":
    testStack()
