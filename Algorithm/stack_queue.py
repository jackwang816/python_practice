class Stack(object):
    def __init__(self, list=[]):
        self._size = len(list)
        self._list = list
    
    def push(self, node):
        if node is not None:
            self._list.append(node)
            self._size += 1

    def pop(self):
        tmp = self._list.pop() if self._size> 0 else None
        self._size = self._size - 1 if self._size > 0 else 0
        return tmp
    
    def print_stack(self):
        print self._list

from collections import deque
class Queue(object):
    def __init__(self, list=[]):
        self._size = len(list)
        self.queue = deque(list)

    def enque(self, node):
        self.queue.append(node)
        self._size += 1

    def deque(self):
        tmp = self.queue.popleft() if self._size > 0 else None
        self._size = self._size - 1 if self._size > 0 else 0
        return tmp

# a = []
# a.append(1)
# a.pop()
# a.pop()
# a_queue = Queue([3,4])
# a_queue.enque(1)
# a_queue.enque(2)
# print a_queue.deque()
# print a_queue.deque()
# a_stack = Stack()
# a_stack.push(1)
# a_stack.push(2)
# print a_stack.pop()
# print a_stack.pop()

class Queue_s(object):
    def __init__(self, list=[]):
        self._size = len(list)
        self._stack_in = Stack(list)
        self._stack_out = Stack()
    
    def enque(self, node):
        self._size += 1
        self._stack_in.push(node)

    def deque(self):
        if self._stack_in._size and not self._stack_out._size:
            self._move()
        tmp = self._stack_out.pop() if self._size > 0 else None
        self._size = self._size - 1 if self._size > 0 else 0
        return tmp

    def _move(self):
        # print "mov stack in:"
        # self._stack_in.print_stack()
        # print self._size
        for idx in range(self._size):
            tmp = self._stack_in.pop()
            # print "mov {}".format(tmp)
            self._stack_out.push(tmp)
    
q_s = Queue_s([1,2,3,4])
for idx in range(3):
    print q_s.deque()
q_s.enque(7)
print q_s.deque()
q_s.enque(8)
print q_s.deque()
print q_s.deque()