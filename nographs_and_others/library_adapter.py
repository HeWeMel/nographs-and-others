from collections.abc import Iterable, Callable, Sequence
from typing import Any, Optional

ToEdges = Iterable[tuple[int, float]]
NextEdges = Callable[[int, Any], ToEdges]


def _raise_not_implemented(class_name, method_name):
    raise NotImplementedError(
        "Method "
        + method_name
        + " not implemented by adaptor for library "
        + class_name
    )


def _undefined_next_edges(vertex: int, traversal: Any) -> ToEdges:
    raise RuntimeError("next_edges accessed before graph has been set")


class AdaptLibrary:
    name = "undefined"
    # Concrete sub class need to set this to True, if build_graph() should
    # be called by a test case to allow the library to build up a graph before
    # starting the analysis.
    has_build_graph = True

    @classmethod
    def warm_up(cls):
        """Called only once by the benchmark, before all tests. Can be used for
        test and graph independent preparation, e.g., for setting up the connection to
        the library."""
        return

    def __init__(self) -> None:
        """In sub classes, do not do any computation work here, since it will
        not be covered by the benchmark."""
        self.next_edges: NextEdges = _undefined_next_edges
        self.max_vertex: int = -1
        self.graph_size: int = -1

    def set_graph_specs(
        self, next_edges: NextEdges, max_vertex: int, graph_size: int
    ) -> None:
        """Do not overwrite or extend this, since what you do will not be
        covered by the benchmark."""
        self.next_edges = next_edges
        self.max_vertex = max_vertex
        self.graph_size = graph_size

    def build_graph(self):
        """Called once per test graph. Can be used for computing a graph from
        the given data, so that it can be used for several tests."""
        pass

    def breadth_first_search(self, start_vertex: int, goal_vertex: int) -> int:
        """Return depth of goal_vertex from start_vertex."""
        _raise_not_implemented(self.name, "breadth_first_search")
        return -1

    def dijkstra_distances(
        self, start_vertex: int, goal_vertices: Sequence[int]
    ) -> float:
        """Return distance of goal_vertex from start_vertex."""
        _raise_not_implemented(self.name, "dijkstra_distance")
        return float("infinity")

    def dijkstra_path_and_distance(
        self, start_vertex: int, goal_vertex: int
    ) -> tuple[float, Sequence[int]]:
        """Return distance of goal_vertex from start_vertex and (one of)
        the shortest paths from start_vertex to end_vertex.
        A return value of -1 for float means, the library adapter only
        implemented the path computation, but not the computation of the
        length of the path."""
        _raise_not_implemented(self.name, "dijkstra_path_and_distance")
        return float("infinity"), ()

    def depth_first_search(self, start_vertex: int, goal_vertex: int) -> int:
        """Return lenght (edges) or fount path to goal_vertex from start_vertex."""
        _raise_not_implemented(self.name, "depth_first_search")
        return -1
