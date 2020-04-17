#!/usr/bin/env python3
def heap_sort(l, n):
    for i in reversed(range(n//2)):
        move_down(l, n, i)
    
    for i in reversed(range(n)):
        l[0], l[i] = l[i], l[0]
        move_down(l, i, 0)

def move_down(l, n, i):
    leftChild, rightChild, largest = 2*i+1, 2*i+2, i
    
    if leftChild < n and l[leftChild] > l[largest]:
        largest = leftChild
    if rightChild < n and l[rightChild] > l[largest]:
        largest = rightChild
    
    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        move_down(l, n, largest)

if __name__ == "__main__":
    list_test = [2,4,7,1,3,2,10,9,10,11,34]
    heap_sort(list_test, len(list_test))
    print(list_test)

    