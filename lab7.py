from typing import Any, Optional, Dict, List
from enum import Enum

class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data
        self.index = index

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight = None):
        self.weight = weight
        self.source = source
        self.destination = destination

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies = {}):
        self.adjacencies = adjacencies

    def create_vertex(self, data: Any):
        new = Vertex(data, len(self.adjacencies))
        self.adjacencies[new] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        krawedz = Edge(source, destination, weight)
        self.adjacencies[source].append(krawedz)

x = Graph()
x.create_vertex('a')
x.create_vertex('b')
x.add_directed_edge(list(x.adjacencies)[0], list(x.adjacencies)[1])
