from collections.abc import Sequence
from typing import Optional, Any

from nographs_and_others.library_adapter import AdaptLibrary, NextEdges

import retworkx as rx  # type: ignore


class AdaptRetworkX(AdaptLibrary):
    name = "RetworkX"

    def __init__(self) -> None:
        super().__init__()
        self.g: Optional[rx.PyDiGraph] = None
        self.index_of_vertex: Any = None

    def build_graph(self) -> None:
        self.g = g = rx.PyDiGraph()

        # API works with vertex indices
        index_of_vertex = g.add_nodes_from(range(self.graph_size))
        self.index_of_vertex = index_of_vertex

        # Adding single edges is fast for this library, so gone
        # the easy way here
        next_edges = self.next_edges
        for from_vertex in range(self.max_vertex + 1):
            from_vertex_index = index_of_vertex[from_vertex]
            for to_vertex, weight in next_edges(from_vertex, None):
                to_vertex_index = index_of_vertex[to_vertex]
                g.add_edge(from_vertex_index, to_vertex_index, weight)

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
