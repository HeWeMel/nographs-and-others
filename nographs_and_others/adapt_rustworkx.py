from collections.abc import Sequence
from typing import Optional, Any

from nographs_and_others.library_adapter import AdaptLibrary, NextEdges

import rustworkx as rx  # type: ignore


class AdaptRustworkX(AdaptLibrary):
    name = "rustworkx"

    def __init__(self) -> None:
        super().__init__()
        self.g: Optional[rx.PyDiGraph] = None
        self.index_of_vertex: Any = None

    def build_graph(self) -> None:
        next_edges = self.next_edges
        self.g = g = rx.PyDiGraph()

        # API works with vertex indices
        index_of_vertex = g.add_nodes_from(range(self.graph_size))
        self.index_of_vertex = index_of_vertex

        # For Python 3.10 and with a previous version of Rustworkx, adding edges
        # one by one was fast. This was the code used:
        # for from_vertex in range(self.max_vertex + 1):
        #     from_vertex_index = index_of_vertex[from_vertex]
        #     for to_vertex, weight in next_edges(from_vertex, None):
        #         to_vertex_index = index_of_vertex[to_vertex]
        #         g.add_edge(from_vertex_index, to_vertex_index, weight)

        # Load chunks of about 10 000 edges per step into the library.
        # (Balance between too much calls and too large python lists...)
        edges = []
        for from_vertex in range(self.max_vertex + 1):
            from_vertex_index = index_of_vertex[from_vertex]
            for (to_vertex, weight) in next_edges(from_vertex, None):
                to_vertex_index = index_of_vertex[to_vertex]
                edges.append((from_vertex_index, to_vertex_index, weight))
            if len(edges) > 10000:
                g.add_edges_from(edges)
                edges = []
        if len(edges) > 0:
            g.add_edges_from(edges)

    def breadth_first_search(self, start_vertex: int, goal_vertex: int) -> int:
        class DepthVisitor(rx.visit.BFSVisitor):
            def __init__(self):
                self.depths = [0] * graph_size
                self.depths[from_vertex_index] = 0

            def tree_edge(self, edge):
                vertex_from, vertex_to, weight = edge
                self.depths[vertex_to] = self.depths[vertex_from] + 1

        from_vertex_index = self.index_of_vertex[start_vertex]
        goal_vertex_index = self.index_of_vertex[goal_vertex]
        graph_size = self.graph_size
        vis = DepthVisitor()
        rx.bfs_search(self.g, [from_vertex_index], vis)
        return vis.depths[goal_vertex_index]

    def breadth_first_search_alternative(
        self, start_vertex: int, goal_vertex: int
    ) -> int:
        """Alternative implementation. Not in use. Much slower (8.77secs)."""
        g = self.g
        from_vertex_index = self.index_of_vertex[start_vertex]
        goal_vertex_index = self.index_of_vertex[goal_vertex]
        # The docs say:
        # "digraph_dijkstra_shortest_path_lengths(graph, node, edge_cost_fn, /, goal=None)"
        # This seams to be wrong. By try and error, I found that the signature
        # is like that from digraph_dijkstra_shortest_paths.
        lengths = rx.digraph_dijkstra_shortest_paths(
            g,
            from_vertex_index,
            goal_vertex_index,
            lambda edge: 1,
        )
        return lengths[goal_vertex_index]

    def dijkstra_distances(
        self, start_vertex: int, goal_vertices: Sequence[int]
    ) -> float:
        g = self.g
        index_of_vertex = self.index_of_vertex
        from_vertex_index = index_of_vertex[start_vertex]
        lengths = rx.dijkstra_shortest_path_lengths(
            g, from_vertex_index, edge_cost_fn=float
        )
        return sum(lengths[index_of_vertex[i]] for i in goal_vertices)

    def dijkstra_path_and_distance(
        self, start_vertex: int, goal_vertex: int
    ) -> tuple[float, Sequence[int]]:
        assert self.g is not None
        g = self.g
        from_vertex_index = self.index_of_vertex[start_vertex]
        goal_vertex_index = self.index_of_vertex[goal_vertex]
        # The following call takes unusually much time.
        paths = rx.digraph_dijkstra_shortest_paths(
            g, from_vertex_index, goal_vertex_index, weight_fn=float
        )
        # Only one path is returned, so that is not the problem.
        path = paths[goal_vertex_index]
        return -1, tuple(g[index] for index in path)
