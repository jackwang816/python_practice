from __future__ import print_function
from adjacencyList import Graph

def DFS_recursive(graph, vertex, visited):
    if vertex in visited:
        return
    visited.add(vertex)
    print('%d '%vertex, end='')
    for i in graph.neighbours(vertex):
        DFS_recursive(graph, i, visited)

def DFS_stack(graph, vertex, visited):
    if vertex in visited:
        return
    visited.add(vertex)
    stack = list()
    stack.append(vertex)
    while stack:
        start = stack.pop()
        print('%d '%start, end='')
        for i in graph.neighbours(start):
            if i not in visited:
                visited.add(i)
                stack.append(i)

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,4)
    graph.add_edge(4,3)

    visited = set()
    print('DFS graph recursive function:')
    for i in range(5):
        DFS_recursive(graph, i, visited)
    print('\nDFS graph using stack')

    visited = set()
    for i in range(5):
        DFS_stack(graph, i, visited)
