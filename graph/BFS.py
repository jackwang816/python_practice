from __future__ import print_function
from adjacencyList import Graph

def BFS(graph, vertex, visited):
    if vertex in visited:
        return
    visited.add(vertex)
    queue = list()
    queue.append(vertex)
    while queue:
        start = queue.pop(0)
        print('%d '%start, end='')
        for i in graph.neighbours(start):
            if i not in visited:
                visited.add(i)
                queue.append(i)

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,4)
    graph.add_edge(4,3)

    visited = set()
    print('BFS graph function:')
    for i in range(5):
        BFS(graph, i, visited)