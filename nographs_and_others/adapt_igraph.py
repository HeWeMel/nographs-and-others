from collections.abc import Sequence
from typing import Optional

from nographs_and_others.library_adapter import AdaptLibrary, NextEdges

import igraph as ig  # type: ignore


class AdaptIgraph(AdaptLibrary):
    name = "igraph"

    @classmethod
    def warm_up(cls):
        # The first time a graph is build up costs extra time with this
        # library. The following graph of minimal size allows for measuring
        # this time, and makes the following tests independent of this effect.
        g = ig.Graph(n=2, directed=True)
        g.add_edges([(0, 1)], {"weight": [1]})

    def __init__(self) -> None:
        super().__init__()
        self.g: Optional[ig.Graph] = None

    def build_graph(self) -> None:
        # No vertex to id translation necessary, since example fits
        # to the index space of the library.
        self.g = g = ig.Graph(n=self.graph_size, directed=True)

        # Load chunks of about 10 000 edges per step into the library.
        # (Balance between too much calls and too large python lists...)
        edges = []
        weights = []
        for i in range(self.max_vertex + 1):
            for (j, w) in self.next_edges(i, None):
                edges.append((i, j))
                weights.append(w)
            if len(edges) > 10000:
                g.add_edges(edges, {"weight": weights})
                edges = []
                weights = []
        if len(edges) > 0:
            g.add_edges(edges, {"weight": weights})

    def breadth_first_search(self, start_vertex: int, goal_vertex: int) -> int:
        assert self.g is not None
        bfs_iter = self.g.bfsiter(vid=start_vertex, mode="out", advanced=True)
        for vertex, distance, parent in bfs_iter:
            if vertex.index == goal_vertex:
                return distance
        raise KeyError("Vertex not found")

    def dijkstra_distances(
        self, start_vertex: int, goal_vertices: Sequence[int]
    ) -> float:
        assert self.g is not None
        distances = self.g.shortest_paths(
            source=start_vertex, target=goal_vertices, weights="weight", mode="out"
        )
        return sum(distances[0][i] for i in range(len(goal_vertices)))

    def dijkstra_path_and_distance(
        self, start_vertex: int, goal_vertex: int
    ) -> tuple[float, Sequence[int]]:
        assert self.g is not None
        paths = self.g.get_shortest_paths(
            start_vertex, to=goal_vertex, weights="weight", output="vpath"
        )
        return -1, paths[0]  # first (only) path is the needed one
