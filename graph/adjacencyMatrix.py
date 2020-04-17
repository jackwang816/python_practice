# indirected granph
from __future__ import print_function

class Graph(object):
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjacentMatrix = [[0]*numVertices for x in range(numVertices)]
        self.vertices = {}
        self.verticesList = [None] * numVertices

    def set_vertex(self, vtx, id):
        assert(vtx < self.numVertices and vtx >= 0)
        # remove original vertex, pop(None) when there was no vertex before 
        self.vertices.pop(self.verticesList[vtx], None)
        self.verticesList[vtx] = id
        self.vertices[id] = vtx
 
    def set_edge(self, ida, idb, weight=1):
        try:
            a = self.vertices[ida]
            b = self.vertices[idb]
        except KeyError as e:
            print('No vertex named %s'% e)
        self.adjacentMatrix[a][b], self.adjacentMatrix[b][a] = weight, weight

    def get_vertices(self):
        return self.verticesList

    def get_edges(self):
        ret_list = []
        for i in range(self.numVertices):
            for j in range(i+1):
                if self.adjacentMatrix[i][j] != 0:
                    temp = (self.verticesList[i], self.verticesList[j], self.adjacentMatrix[i][j])
                    ret_list.append(temp)
        return ret_list

    def adjacent(self, vidx, vidy):
        return self.adjacentMatrix[vidx][vidy] != 0

    def neibours(self, vid):
        try:
            vt = self.vertices[vid]
        except KeyError as e:
            print('No vertex named %s' % e)
        ret_list = []
        for index, weight in enumerate(self.adjacentMatrix[vt]):
            if weight != 0:
                temp = (index, self.verticesList[index], weight)
                ret_list.append(temp)
        return ret_list

    def get_matrix(self):
        return self.adjacentMatrix

class Graph_simple(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacentMatrix = [[0]*vertices for x in range(vertices)]
    
    def add_edge(self, vx, vy, weight=1):
        assert(vx < self.vertices and vy < self.vertices)
        self.adjacentMatrix[vx][vy] = self.adjacentMatrix[vy][vx] = weight

    def adjacent(self, vx, vy):
        assert(vx < self.vertices and vy < self.vertices)
        return self.adjacentMatrix[vx][vy] != 0

    def neibours(self, vid):
        assert(vid < self.vertices)
        ret_list = []
        for index, weight in enumerate(self.adjacentMatrix[vid]):
            if weight != 0:
                ret_list.append(index)
        return ret_list

    def print_graph(self):
        for i in range(self.vertices):
            print('Ajacent vertices list of vertex %d:\nHead' % i, end='')
            for vt in self.neibours(i):
                print('->{}'.format(vt), end='')
            print('')

if __name__ == "__main__":
    G =Graph(6)
    G.set_vertex(0,'a')
    G.set_vertex(1,'b')
    G.set_vertex(2,'c')
    G.set_vertex(3,'d')
    G.set_vertex(4,'e')
    G.set_vertex(5,'f')
    G.set_edge('a','e',10)
    G.set_edge('a','c',20)
    G.set_edge('c','b',30)
    G.set_edge('b','e',40)
    G.set_edge('e','d',50)
    G.set_edge('f','e',60)
    print("Vertices of Graph")
    print(G.get_vertices())
    print("Edges of Graph")
    print(G.get_edges())
    print("Adjacency Matrix of Graph")
    print(G.get_matrix())

    print("=======test for simple Graph")
    graph = Graph_simple(6)
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