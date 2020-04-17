from __future__ import print_function
class AdjNode(object):
    def __init__(self, v):
        self.vertex = v
        self.next = None
# undirected Graph
class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjArray = [None] * self.vertices

    def add_edge(self, vx, vy):
        assert(vx < self.vertices and vy < self.vertices)
        # adding vx to vy adjacency list and adding vy to vx adjacency list
        nodex, nodey = AdjNode(vx), AdjNode(vy)
        nodex.next, nodey.next = self.adjArray[vy], self.adjArray[vx]
        self.adjArray[vy], self.adjArray[vx] = nodex, nodey
    
    def adjacent(self, vx, vy):
        assert(vx < self.vertices and vy < sefl.vertices)
        adjList = self.adjArray[vx]
        while adjList:
            if adjList.vertex == vy:
                return True
            adjList = adjList.next
        return False
    
    def neighbours(self, vid):
        assert(vid<self.vertices)
        adjList, retList = self.adjArray[vid], []
        while adjList:
            retList.append(adjList.vertex)
            adjList = adjList.next
        return retList

    def print_graph(self):
        for index in range(self.vertices):
            adjList = self.adjArray[index]
            print('Ajacent vertices list of vertex %d:\nHead'%index, end='')
            while adjList:
                print('->{}'.format(adjList.vertex), end='')
                adjList = adjList.next
            print('')
    
if __name__ == "__main__":
    print("=======test for adjacencyList Graph")
    graph = Graph(6)
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4)
    assert(graph.adjacent(0,1) and graph.adjacent(0,4))
    assert(not graph.adjacent(1, 5))
    graph.print_graph()