import heapq
def heappop_max(heap):
    """Pop the largest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
    else:
        returnitem = lastelt
    return returnitem

def heappush_max(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)

def cal_depth(heap):
    h_n = len(heap)
    depth = i = 0
    while i < h_n:
        depth += 1
        i = 2*i+1
    return depth
def gen_heap_graph(heap_graph, heap, pos, depth, level):
    if len(heap) < pos+1:
        return
    num_empty = 2**depth-1
    empty_list = [" " for i in range(num_empty)]
    line = empty_list + [heap[pos]] + empty_list
    if len(heap_graph) < level+1:
        heap_graph.append(line)
    else:
        heap_graph[level] = heap_graph[level] + [' '] + line
    childleft = 2*pos + 1
    childright = childleft + 1
    gen_heap_graph(heap_graph, heap, childleft, depth-1, level+1)
    gen_heap_graph(heap_graph, heap, childright, depth-1, level+1)

def print_heap(heap):
    depth = cal_depth(heap)
    heap_graph = []
    gen_heap_graph(heap_graph, heap, 0, depth-1, 0)
    for line in heap_graph:
        linestr = ''.join([str(item) for item in line])
        print linestr

if __name__ == "__main__":
    h1 = [12,2,33,4,5,6,7,81,9,10]
    heapq._heapify_max(h1)
    print heappop_max(h1)
    heappush_max(h1, 50)
    print_heap(h1)
