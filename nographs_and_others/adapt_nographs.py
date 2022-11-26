from collections.abc import Sequence, Callable
from typing import Optional, Any

from nographs_and_others.library_adapter import AdaptLibrary, ToEdges

import nographs as nog


class AdaptNoGraphsABC(AdaptLibrary):
    """Generic adapter for library NoGraphs. Adapter name and a concrete
    gear is defined by a concrete sub class. A factory function that computes
    a vertex_to_id function from the start vertex can be defined."""
    name: str  # Needs to be overridden
    has_build_graph = False
    gear: nog.Gear[int, int, float, Any]  # Needs to be overridden

    @staticmethod
    def factory_vertex_to_id(start_vertex: int
                             ) -> Callable[[int], int]:
        return nog.vertex_as_id

    # It would be easily possible to prune the graph according to the
    # max_vertex and graph_size limits given as part of the test case
    # input, but NoGraphs can find that out automatically, and faster.
    # def pruned_next_edges(self):
    #
    #     org_next_edges = self.next_edges
    #     max_vertex = self.max_vertex
    #
    #     def next_edges(v: int, t) -> ToEdges:
    #         return org_next_edges(v, t) if v <= max_vertex else ()
    #     return next_edges

    def breadth_first_search(
            self, start_vertex: int, goal_vertex: int
    ) -> int:
        traversal = nog.TraversalBreadthFirstFlex[int, int, None](
            next_edges=self.next_edges, gear=self.gear,
            vertex_to_id=self.factory_vertex_to_id(start_vertex)
        )
        traversal.start_from(start_vertex)
        _ = traversal.go_to(goal_vertex)
        return traversal.depth

    def dijkstra_distances(
        self, start_vertex: int, goal_vertices: Sequence[int]
    ) -> float:
        traversal = nog.TraversalShortestPathsFlex[int, int, float, None](
            next_edges=self.next_edges, gear=self.gear,
            vertex_to_id=self.factory_vertex_to_id(start_vertex)
        )
        traversal.start_from(start_vertex)
        distances = [
            traversal.distance
            for vertex in traversal.go_for_vertices_in(goal_vertices)
        ]
        return sum(distances)

    def dijkstra_path_and_distance(
        self, start_vertex: int, goal_vertex: int
    ) -> tuple[float, Sequence[int]]:
        traversal = nog.TraversalShortestPathsFlex[int, int, float, None](
            next_edges=self.next_edges, gear=self.gear,
            vertex_to_id=self.factory_vertex_to_id(start_vertex)
        )
        traversal.start_from(start_vertex, build_paths=True)
        v = traversal.go_to(goal_vertex)
        p = tuple(traversal.paths.iter_vertices_from_start(v))
        return traversal.distance, p

    def depth_first_search(
            self, start_vertex: int, goal_vertex: int
    ) -> int:
        traversal = nog.TraversalDepthFirstFlex[int, int, None](
        # traversal = nog.TraversalNeighborsThenDepthFlex[int, int, None](
            next_edges=self.next_edges, gear=self.gear,
            vertex_to_id=self.factory_vertex_to_id(start_vertex)
        )
        traversal.start_from(start_vertex)
        return sum(1 for v in traversal)  # not depth, but #reachable


class AdaptNoGraphs(AdaptNoGraphsABC):
    name = "NoGraphs"
    gear = nog.GearDefault[int, int, float, None]()
