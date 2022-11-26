from collections.abc import Callable

from nographs_and_others.adapt_nographs import AdaptNoGraphsABC

import nographs as nog


def ids_for_vertices_starting_at(start: int) -> Callable[[int], int]:
    """Return a function that shifts vertices given as integers in
    range start... to integers in range 0...

    >>> vertex_to_id = ids_for_vertices_starting_at(100)
    >>> [vertex_to_id(v) for v in range(100, 104)
    [0, 1, 2, 3]
    """
    return lambda v: v - start


def ids_for_vertices_around(start: int) -> Callable[[int], int]:
    """Return a function that shifts vertices given as integers
    around start to integers in range 0...

    >>> vertex_to_id = ids_for_vertices_around(100)
    >>> [vertex_to_id(v) for v in range(95, 106)]
    [9, 7, 5, 3, 1, 0, 2, 4, 6, 8, 10]
    """
    return lambda v: 2*abs(v-start) - (v < start)


class AdaptNoGraphsAllIntAndIDsShift(AdaptNoGraphsABC):
    name = "nog+shift"
    gear = nog.GearForIntVerticesAndIDsAndCFloats[None](False)

    @staticmethod
    def factory_vertex_to_id(start_vertex: int
                             ) -> Callable[[int], int]:
        return ids_for_vertices_starting_at(start_vertex)
