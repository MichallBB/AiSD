from lab7 import Graph, Edge, Vertex
from typing import Dict, List


class Pathfinder:
    cost_set: Dict[Vertex, float]
    parent_set: Dict[Vertex, Vertex]
    graph: Graph

    def __init__(self, graph: Graph):
        self.cost_set = {}
        self.parent_set = {}
        self.graph = graph

    def dijkstra(self, start_node: Vertex, end_node: Vertex) -> List[Vertex]:
        open_set = []
        closed_set = []

        self.cost_set[start_node] = 0.0
        closed_set.append(start_node)
        for edge in self.graph.adjacencies[start_node]:
            open_set.append(edge)
            self.parent_set[edge.destination] = edge.source

        while True:
            # update costs
            for edge in open_set:
                if edge.destination not in self.cost_set or self.cost_set[edge.source] + edge.weight < self.cost_set[edge.destination]:
                    self.parent_set[edge.destination] = edge.source
                    self.cost_set[edge.destination] = self.cost_set[edge.source] + edge.weight

            # pop lowest cost
            edge_to_explore = self.pop_lowest_cost(open_set)
            vertex_to_explore = edge_to_explore.destination

            print(f'from: {edge_to_explore.source.data} to {edge_to_explore.destination.data}')

            if vertex_to_explore is end_node:
                print('Reached end!')
                return self.retrace_path(end_node, start_node)

            # add edges
            closed_set.append(vertex_to_explore)

            for edge in self.graph.adjacencies[vertex_to_explore]:
                if edge.destination not in closed_set:
                    open_set.append(edge)

    def pop_lowest_cost(self, open_set: List[Edge]):
        lowest_cost = float('inf')
        index = -1

        for i in range(len(open_set)):
            iedge = open_set[i]
            if self.cost_set[iedge.destination] < lowest_cost:
                lowest_cost = self.cost_set[iedge.destination]
                index = i

        return open_set.pop(index)

    def retrace_path(self, end_node: Vertex, start_node: Vertex) -> List[Vertex]:
        return_list = [end_node]
        pointer = end_node

        while pointer is not start_node:
            pointer = self.parent_set[pointer]
            return_list.append(pointer)

        return_list.reverse()
        return return_list


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

paf = Pathfinder(graf)
paf.dijkstra(v5,v4)
