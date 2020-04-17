#!/usr/bin/env python3
def max_heapify(h):
    n = len(h)

    for i in reversed(range(n//2)): #use xrange for python2.x
        move_down_max(h, i)

def move_down_max(h, i):
    n = len(h)
    leftChild, rightChild, largest = i*2+1, i*2+2, i
    
    if leftChild < n and h[leftChild] >= h[largest]:
        largest = leftChild
    if rightChild < n and h[rightChild] >= h[largest]:
        largest = rightChild

    if largest != i:
        h[i], h[largest] = h[largest], h[i]
        move_down_max(h, largest)
    
def max_heap_insert(h, x):
    h.append(x)
    n = len(h) - 1
    parent = (n-1) >> 1
    while parent >= 0:
        if h[parent] < h[n]:
            h[parent], h[n] = h[n], h[parent]
        if parent == 0:
            break
        parent, n = (parent-1)>>1, parent

def max_heap_pop(h):
    r, h[0] = h[0], h[-1]
    h.pop()
    move_down_max(h, 0)
    return r

def move_down_max_nonrecrusive(h, i):
    parent, n = i, len(h)
    while parent < n:        
        leftChild, rightChild, largest = parent*2+1, parent*2+2, parent
        if leftChild < n and h[leftChild] >= h[largest]:
            largest = leftChild
        if rightChild < n and h[rightChild] >= h[largest]:
            largest = rightChild

        if largest == parent:
            break
        h[parent], h[largest] = h[largest], h[parent]
        parent = largest

if __name__ == "__main__":
    list_a = [1, 4, 2, 3, 4, 5]
    max_heapify(list_a)
    print(list_a)
    max_heap_insert(list_a, 6)
    print(list_a)
    max_heap_insert(list_a, 3)
    print(list_a)
    print(max_heap_pop(list_a))
    print(list_a)