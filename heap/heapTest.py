import heapq

def min_idx(x, pos1, pos2):
    return pos1 if x[pos1] < x[pos2] else pos2

def max_idx(x, pos1, pos2):
    return pos1 if x[pos1] > x[pos2] else pos2

class MyHeap(object):
    @classmethod
    def heapify(cls, x):
        n = len(x)

        for i in reversed(xrange(n//2)):
            cls.minHeapify(x, i)
    
    @classmethod
    def minHeapify(cls, heap, pos):
        childLeft = (pos << 1) + 1
        childRight = childLeft + 1

        minPos = cls.minPos(heap, len(heap), pos, childLeft, childRight)
        if minPos != pos:
            heap[pos], heap[minPos] = heap[minPos], heap[pos]
            cls.minHeapify(heap, minPos)

    @classmethod
    def minPos(cls, heap, n, parentPos, childLeft, childRight):
        if childRight < n:
            return min_idx(heap, parentPos, min_idx(heap, childLeft, childRight))
        elif childLeft < n:
            return min_idx(heap, parentPos, childLeft)
        else:
            return parentPos

    @classmethod
    def minHeapPop(cls, heap):
        lastValue = heap.pop()
        if heap:
            retValue = heap[0]
            heap[0] = lastValue
            cls.minHeapify(heap, 0)
        else:
            retValue = lastValue
        return retValue
    @classmethod
    def minHeapSort(cls, x):
        cls.heapify(x)
        retList = []
        while x:
            retList.append(cls.minHeapPop(x))
        return retList
if __name__ == "__main__":
    # a = [1,2,3,4,5]
    # b = [3,5,10,44,3,1,4,5,4,11,12]
    # MyHeap.heapify(a)
    # MyHeap.heapify(b)

    # print a
    # while a:
    #     print MyHeap.minHeapPop(a)
    # print b
    # while b:
    #     print MyHeap.minHeapPop(b)

    c = [3,5,10,44,3,1,4,5,4,11,12]
    c = MyHeap.minHeapSort(c)
    print c
    
    
