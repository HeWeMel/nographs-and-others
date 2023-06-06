from collections.abc import Sequence
from typing import Optional

from nographs_and_others.library_adapter import AdaptLibrary, NextEdges

import networkx as nx  # type: ignore


class AdaptNetworkX(AdaptLibrary):
    name = "NetworkX"

    def __init__(self) -> None:
        super().__init__()
        self.G: Optional[nx.DiGraph] = None

    def build_graph(self) -> None:
        self.G = nx.DiGraph()
        for i in range(self.max_vertex + 1):
            self.G.add_weighted_edges_from(
                (i, j, w) for (j, w) in self.next_edges(i, None)
            )

    def breadth_first_search(self, start_vertex: int, goal_vertex: int) -> int:
        assert self.G is not None
        distance = nx.shortest_path_length(
            self.G, start_vertex, goal_vertex, weight=None
        )
        return distance

    def dijkstra_distances(
        self, start_vertex: int, goal_vertices: Sequence[int]
    ) -> float:
        assert self.G is not None
        distances = nx.single_source_dijkstra_path_length(G=self.G, source=start_vertex)
        return sum(distances[i] for i in goal_vertices)

    def dijkstra_path_and_distance(
        self, start_vertex: int, goal_vertex: int
    ) -> tuple[float, Sequence[int]]:
        assert self.G is not None
        distance, path = nx.single_source_dijkstra(
            self.G, start_vertex, target=goal_vertex
        )
        return distance, path
