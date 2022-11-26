import gc
from collections.abc import Iterable, Callable, Sequence, Iterator
from typing import Any, Protocol
from abc import abstractmethod, ABC

from nographs_and_others.library_adapter import AdaptLibrary

import nographs as nog  # Only used to determine size information for other libraries


def test_next_edges(i, *_):
    j = (i + i // 6) % 6
    yield i + 1, j * 2 + 1
    if i % 2 == 0:
        yield i + 6, 7 - j
    elif i % 1200000 > 5:
        yield i - 6, 1


class TestCase(ABC):
    """Abstract base class for test cases.

    Concrete subclasses need to provide an __init__() method without parameters,
    and an implementation for do_search, and need to set the following
    instance variables:

    - next_edges
    - vertices_count
    - max_vertex
    - max_vertex_told
    - graph_size

    max_vertex is the highest vertex necessary to visit in order to solve
    the task. The edges from this vertex are to be regarded, and thus,
    also the vertices they lead to.

    vertices_count is the number of vertices that need to be regarded.
    """
    name: str = "undefined"

    def __init__(self) -> None:
        def empty_next_edges(i, *_):
            return []
        self.next_edges: Callable[
            [int, Any], Iterable[tuple[int, float]]
        ] = empty_next_edges
        self.vertices_count = 0
        self.max_vertex = 0
        self.max_vertex_told = 0
        self.graph_size = 0

    def _define(self,
                next_edges: Callable[[int, Any], Iterable[tuple[int, float]]],
                vertices_count: int, max_vertex: int, max_vertex_told: int
                ) -> None:
        """ Save next_edges function and test case attributes. Compute graph_size.

        max_vertex is the highest vertex necessary to visit in order to solve
        the task. The edges from this vertex are to be regarded, and thus,
        also the vertices they lead to.

        vertices_count is the number of vertices that need to be regarded.
        """

        self.next_edges = next_edges
        self.vertices_count = vertices_count
        self.max_vertex = max_vertex
        self.max_vertex_told = max_vertex_told

        # Compute highest vertex number that can be directly reached from one of
        # the vertices up to max_vertex. The sub graph to be regarded needs vertices
        # up to this maximum.
        self.graph_size = (
                              max(t for f in range(self.max_vertex_told + 1)
                                  for t, *_ in self.next_edges(f, None))
                          ) + 1

    def _compute_graph_size(self) -> None:
        """Compute graph size, the
        highest vertex number that can be directly reached from one of
        the vertices up to max_vertex. The sub graph to be regarded needs vertices
        up to this maximum.
        """
        self.graph_size = (
            max(t for f in range(self.max_vertex_told + 1)
                for t, *_ in self.next_edges(f, None))
        ) + 1

    def next_edges_function(
            self
    ) -> Callable[[int, None], Iterable[tuple[int, float]]]:
        """Just return the next edges function. The test frame will call this
        to make sure, that subsequent accesses to the function that happen
        during a test run need no time or memory for initialisation, because
        it is not the first access to it."""
        return self.next_edges

    def set_graph_specs(self, library_adaptor: AdaptLibrary) -> None:
        """Give the library adapter the prepared information about the graph.
        The library adapter is not allowed to do anything else than storing
        the information.
        """
        library_adaptor.set_graph_specs(
            self.next_edges_function(), self.max_vertex_told, self.graph_size
        )

    def build_graph(self, library_adaptor: AdaptLibrary) -> None:
        """Tell the library adapter to compute a representation of the
        graph, if one is needed by the library.
        """
        library_adaptor.build_graph()

    def search(self, library_adaptor: AdaptLibrary,
               print_results: bool, gc_on_multiple_runs: bool) -> None:
        """Perform the search defines by method do_search of the concrete sub
        class. If the library adapter does not implement the method the test
        case calls, print error message."""
        try:
            self.do_search(library_adaptor, print_results, gc_on_multiple_runs)
        except NotImplementedError as e:
            # either do_search of the test case is not implemented,
            # or the search in the library adapter
            print("! " + str(e))

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool) -> None:
        """Call library_adaptor to execute the test case, print helpful
        result data and check results by an assertion.

        A concrete subclass needs to implement this.
        """
        raise NotImplementedError()

    def print_case_infos(self) -> None:
        """Call print_infos_from_iteration with a suitable vertex iterator to
        find out and print the needed data about the search of the test case,
        and check results for changes from the values published about the benchmark.
        """
        pass

    def compute_infos_from_iteration(
            self, start_vertices: Sequence[int],
            vertex_iterator: Iterator, goal_vertices: Iterable[int]
    ):
        """Compute and check the number of vertices that need to be regarded for solving
        the test case, and the highest vertex that needs to be explored together
        with its outgoing edges.

        The iterator needs to iterate all vertices that are needed to be
        regarded for the search of the test case and report each vertex just once.
        If start vertices are not reported, they need to be given by start_vertices,
        otherwise, start_vertices needs to be the empty list.
        """
        # print(">>> started")
        goal_vertices = set(goal_vertices)
        vertices_count = len(start_vertices)
        max_vertex = 0 if vertices_count == 0 else max(start_vertices)

        min_vertex = min(start_vertices)

        for vertex in vertex_iterator:
            # print(">>", vertex)
            vertices_count += 1
            if vertex > max_vertex:
                max_vertex = vertex

            if vertex < min_vertex:
                min_vertex = vertex

            if vertex in goal_vertices:
                goal_vertices.discard(vertex)
                if len(goal_vertices) == 0:
                    print(f"{self.name}:")
                    print(f"  {vertices_count=}, "
                          + f"{min_vertex=}, {max_vertex=}")
                    assert vertices_count == self.vertices_count
                    assert max_vertex == self.max_vertex
                    # todo: copy values to cases and add assert here
                    break
        else:
            raise RuntimeError("Vertex not found")


class CaseBreadthFirstSearch(TestCase):
    name = "Breadth first search, 1.20 M vertices, 1 goal"

    def __init__(self) -> None:
        super().__init__()
        super()._define(next_edges=test_next_edges, vertices_count=1199991,
                        max_vertex=1200000, max_vertex_told=1200000)
        self.start_vertex = 0
        self.goal_vertices = [1200000]

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool) -> None:
        depth: int = library_adaptor.breadth_first_search(
            self.start_vertex, self.goal_vertices[0]
        )
        if print_results:
            print("Computed depth:", depth)
        assert depth == 200000

    def print_case_infos(self) -> None:
        traversal = nog.TraversalBreadthFirst[int, int](next_edges=self.next_edges)
        traversal.start_from(self.start_vertex)
        self.compute_infos_from_iteration(
            (self.start_vertex,), iter(traversal), self.goal_vertices
        )


class CaseDepthFirstSearch(TestCase):
    name = "Depth first search, 1M vertices, exhaustive search"

    def __init__(self) -> None:

        # import random
        #
        # def test_dfs_next_edges(v, *_):
        #     """ 5 random edges from each vertex. Slow. """
        #     random.seed(v, 2)
        #     for i in range(4):
        #         yield random.randrange(0, 480000), 1

        # def test_dfs_next_edges(v, *_):
        #     """ 5 pseudo-random edges in range(1000000) for each vertex"""
        #     for i in range(4):
        #         yield hash(1/(v*10+i+1)) % 1000000, 1
        #
        # super().__init__()
        # super()._define(next_edges=test_dfs_next_edges, vertices_count=739817,
        #                 max_vertex=999999, max_vertex_told=999999)
        # self.start_vertex = 0
        # self.goal_vertices = [500000]
        # ..
        # assert depth == 650189

        def test_dfs_next_edges(v, *_):
            """ 5 pseudo-random edges in range(1000000) for each vertex"""
            for i in range(9):
                yield hash(1/(v*10+i+1)) % 1000000, 1

        super().__init__()
        super()._define(next_edges=test_dfs_next_edges, vertices_count=975509,
                        max_vertex=999999, max_vertex_told=999999)
        self.start_vertex = 0
        self.goal_vertices = [500000]

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool) -> None:
        depth: int = library_adaptor.depth_first_search(
            self.start_vertex, self.goal_vertices[0]
        )
        if print_results:
            print("Computed #reachable:", depth)
        assert depth == 999867

    def print_case_infos(self) -> None:
        traversal = nog.TraversalDepthFirst[int, int](next_edges=self.next_edges)
        traversal.start_from(self.start_vertex)
        self.compute_infos_from_iteration(
            (self.start_vertex,), iter(traversal), self.goal_vertices
        )


# -- Dijkstra cases --


class CasesDijkstra(TestCase, ABC):
    def __init__(self,
                 next_edges: Callable[[int, None], Iterable[tuple[int, float]]],
                 start_vertex: int, goal_vertices: Sequence[int],
                 vertices_count: int, max_vertex: int, max_vertex_told) -> None:
        super().__init__()
        super()._define(next_edges, vertices_count, max_vertex, max_vertex_told)
        self.start_vertex = start_vertex
        self.goal_vertices = goal_vertices

    def print_case_infos(self) -> None:
        traversal = nog.TraversalShortestPaths[int, float, Any](self.next_edges)
        traversal.start_from(self.start_vertex)
        self.compute_infos_from_iteration(
            (self.start_vertex,), iter(traversal), self.goal_vertices
        )


class CaseDijkstraDistance(CasesDijkstra):
    name = "Dijkstra distances, 1,2 M vertices, 3 goals"

    def __init__(self):
        super().__init__(test_next_edges,
                         0, [1000000, 1150000, 1200000], vertices_count=1200002,
                         max_vertex=1200006, max_vertex_told=1200006)

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool):
        distance: float = library_adaptor.dijkstra_distances(
            self.start_vertex, self.goal_vertices
        )
        if print_results:
            print(f"Computed distance sum: {distance:.1f}")
        assert abs(distance - 2279877) < 0.001


class CaseDijkstraDistancePart(CasesDijkstra):
    name = "Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded"

    def __init__(self):
        super().__init__(test_next_edges,
                         1200000, [2400000], 1200000, 2400004, 3600000)

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool):
        distance: float = library_adaptor.dijkstra_distances(
            self.start_vertex, self.goal_vertices
        )
        if print_results:
            print(f"Computed distance sum: {distance:.1f}")
        assert abs(distance - 816670) < 0.001


class CaseDijkstraDistanceThreeTimes(CaseDijkstraDistance):
    name = "Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times"

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool):
        distances: list[float] = []
        for i in range(3):
            distances.append(library_adaptor.dijkstra_distances(
                self.start_vertex, self.goal_vertices
            ))
            if gc_on_multiple_runs:
                gc.collect()
        if print_results:
            print("Computed distance sums: " + " ".join([
                f"{distance:.1f}" for distance in distances]))
        assert sum(abs(distance - 2279877) for distance in distances) < 0.001


class CaseDijkstraPathAndDistanceSmall(CasesDijkstra):
    name = "Dijkstra path and distance, 100 T vertices, 1 goal"

    def __init__(self):
        super().__init__(test_next_edges,
                         0, [100000], 100002, 100008, 100008)

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool):
        distance: float
        path: Sequence[int]
        distance, path = library_adaptor.dijkstra_path_and_distance(
            self.start_vertex, self.goal_vertices[0]
        )
        if print_results:
            print(f"Computed distance sum: {distance:.1f}")
            print(f"Computed vertex count of path: {len(path):0,}")

        path_begin, path_end = tuple(path[0:5]), tuple(path[-5:-1])
        if print_results:
            print("Start and end of found path:", path_begin, "...", path_end)

        if abs(distance - (-1)) < 0.001:
            if print_results:
                print("Distance not computed")
        else:
            if print_results:
                print(f"Computed distance sum: {distance:.1f}")
            assert abs(distance - 68061) < 0.001
        assert path_begin == (0, 1, 2, 8, 14)
        assert path_end == (99976, 99982, 99988, 99994)


class CaseDijkstraPathAndDistance(CasesDijkstra):
    name = "Dijkstra path and distance, 1,2 M vertices, 1 goal"

    def __init__(self):
        super().__init__(test_next_edges,
                         0, [1200000], 1200002, 1200006, 1200006)

    def do_search(self, library_adaptor: AdaptLibrary,
                  print_results: bool, gc_on_multiple_runs: bool):
        distance: float
        path: Sequence[int]
        distance, path = library_adaptor.dijkstra_path_and_distance(
            self.start_vertex, self.goal_vertices[0]
        )
        if print_results:
            print(f"Computed distance sum: {distance:.1f}")
            print(f"Computed vertex count of path: {len(path):0,}")

        path_begin, path_end = tuple(path[:5]), tuple(path[-5:])
        if print_results:
            print("Start and end of found path:", path_begin, "...",path_end)

        if abs(distance - (-1)) < 0.001:
            if print_results:
                print("Distance not computed")
        else:
            if print_results:
                print(f"Computed distance sum: {distance:.1f}")
            assert abs(distance - 816674) < 0.001
        assert path_begin == (0, 1, 2, 8, 14)
        assert path_end == (1199976, 1199982, 1199988, 1199994, 1200000)

