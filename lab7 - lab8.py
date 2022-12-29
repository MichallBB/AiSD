from enum import Enum
from typing import Optional


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    def __init__(self, data, index):
        self.data = data
        self.index = index

    def __repr__(self):
        return f'{self.data}'


class Edge:
    def __init__(self, source, destination, weight=None):
        self.weight = weight
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f'{self.source} -> {self.destination}'


class Graph:
    def __init__(self, adjacencies={}):
        self.adjacencies = adjacencies

    def create_vertex(self, data) -> Vertex:
        new = Vertex(data, len(self.adjacencies))
        self.adjacencies[new] = []
        return new

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        new = Edge(source, destination, weight)
        self.adjacencies[source].append(new)

    def add_undirected_edge(self, source, destination, weight=None):
        new = Edge(source, destination, weight)
        new2 = Edge(destination, source, weight)
        self.adjacencies[source].append(new)
        self.adjacencies[destination].append(new2)

    def add(self, edge, source, destination, weight=None):
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)


graf = Graph()
A = graf.create_vertex('A')
B = graf.create_vertex('B')
C = graf.create_vertex('C')
D = graf.create_vertex('D')
E = graf.create_vertex('E')
F = graf.create_vertex('F')

graf.add_directed_edge(A, C, 2)
graf.add_directed_edge(A, C, 2)
graf.add_directed_edge(A, C, 2)