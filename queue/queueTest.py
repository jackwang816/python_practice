from collections import deque
class MyQueue:
    ''' define my queue class
    '''
    def __init__(self, list=None):
        self.queue = deque(list or [])
        self.size = len(self.queue)

    def push(self, data):
        assert(data is not None)
        self.queue.append(data)
        self.size += 1

    def pop(self):
        assert(self.size > 0)
        self.size -= 1
        return self.queue.popleft()

    def peek(self):
        return self.queue[0] if self.size > 0 else None

    def getLen(self):
        return self.size

def testMyQueue():
    test_queue = MyQueue()
    assert(test_queue.peek() is None)
    assert(test_queue.getLen() == 0)
    test_queue.push(0)
    assert(test_queue.getLen() == 1)
    assert(test_queue.peek() == 0)
    test_queue.push(1)
    assert(test_queue.peek() == 0)
    assert(test_queue.pop() == 0)
    assert(test_queue.getLen() == 1)
    assert(test_queue.pop() == 1)

if __name__ == "__main__":
    testMyQueue()
    # deque(double ended queue) test
    queue = deque([1,2,3])
    print queue.pop()
    print queue.popleft()
    queue.appendleft(0)
    queue.append(4)
    print queue.count(1) # count 1 in queue
    for iter in queue:
        print iter