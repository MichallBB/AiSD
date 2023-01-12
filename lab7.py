from enum import Enum
from typing import Optional, Callable, Any, Dict, List
from queue import Queue


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
    def __init__(self, adjacencies: Dict[Vertex, List[Edge]]=None):
        if adjacencies is None:
            self.adjacencies = {}
        else:
            self.adjacencies = adjacencies

    def create_vertex(self, data) -> Vertex:
        new = Vertex(data, len(self.adjacencies))
        self.adjacencies[new] = []
        return new

    def add_directed_edge(self,
                          source: Vertex,
                          destination: Vertex,
                          weight: Optional[float] = None
                          ):
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

    def traverse_breadth_first(self) -> None:
        visited = []
        queue = []
        tekst = []
        first = list(self.adjacencies.keys())[0]
        visited.append(self.adjacencies[first])
        queue.append(self.adjacencies[first])
        tekst.append(first)
        while queue:
            v = queue.pop(0)
            for neighbour in v:
                if self.adjacencies[neighbour.destination] not in visited:
                    visited.append(self.adjacencies[neighbour.destination])
                    queue.append(self.adjacencies[neighbour.destination])
                    tekst.append(neighbour.destination)
        print(tekst)

    def traverse_breadth_first2(self, source=None) -> None:
        visited = {}
        bfs_traversal_output = []
        queue = Queue()
        for node in self.adjacencies.keys():
            visited[node] = False

        if source is None:
            s = list(self.adjacencies.keys())[0]
        else:
            s = source
        visited[s] = True
        queue.put(s)

        while not queue.empty():
            u = queue.get()
            bfs_traversal_output.append(u)

            for v in self.adjacencies[u]:
                if not visited[v.destination]:
                    visited[v.destination] = True
                    queue.put(v.destination)
        print(bfs_traversal_output)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        visited = []
        start = list(self.adjacencies.keys())[0]

        def dfs(v: Vertex):
            visit(v)
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited:
                    dfs(neighbour.destination)
        dfs(start)

    # def dijkstra(self, start):
    #     start.distance = 0
    #     queue = []
    #     heappush(queue, start)
    #     i=0
    #     while queue:
    #         current_vertex = heappop(queue)
    #         for neighbor in self.adjacencies[current_vertex]:
    #             xxx = self.adjacencies[current_vertex][i]
    #             distance = current_vertex.distance + xxx.weight
    #             i += 1
    #             if distance < neighbor.weight:
    #                 neighbor.weight = distance
    #                 heappush(queue, neighbor)
    #
    #     return {v.data: self.adjacencies[v] for v in self.adjacencies}


graf = Graph()
v0 = graf.create_vertex('v0')
v1 = graf.create_vertex('v1')
v2 = graf.create_vertex('v2')
v3 = graf.create_vertex('v3')
v4 = graf.create_vertex('v4')
v5 = graf.create_vertex('v5')

graf.add_directed_edge(v0, v1, 2)
graf.add_directed_edge(v0, v5, 2)
graf.add_directed_edge(v2, v3, 2)
graf.add_directed_edge(v2, v1, 2)
graf.add_directed_edge(v3, v4, 2)
graf.add_directed_edge(v4, v1, 2)
graf.add_directed_edge(v4, v5, 2)
graf.add_directed_edge(v5, v1, 2)
graf.add_directed_edge(v5, v2, 2)


def print_vertex(vertex):
    print(vertex.data)

print('Traverse breadth first')
graf.traverse_breadth_first()
print('Traverse breadth first')
graf.traverse_breadth_first2()
print('Traverse depth first')
graf.traverse_depth_first(print_vertex)
