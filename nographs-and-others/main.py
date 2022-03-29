import tracemalloc
import gc
import timeit

import nographs as nog
import networkx as nx


# -- Test functions --

def start_time_stats():
    gc.collect()
    return timeit.default_timer()


def print_time_stats(start, message="Time:"):
    stop = timeit.default_timer()
    print(message, round(stop - start, 2), "seconds")


def start_mem_stats():
    tracemalloc.start()
    tracemalloc.reset_peak()  # reset peak of previous execution parts


def print_mem_stats(message="Memory peak:"):
    mem_size, mem_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(message, f"{int(mem_peak):,} memory blocks")


def test_run(name, library, *args):
    print("--", name, "--")

    timer = start_time_stats()
    lib = library(args)
    lib.build_graph()
    print_time_stats(timer, "Time for graph definition:")
    distance, path = lib.search()
    lib = None
    print_time_stats(timer, "Time for search:")
    print("Computed distance:", distance)
    print("Start and end of found path:", path[0:5], "...", path[-5:-1])
    print()

    start_mem_stats()
    lib = library(args)
    lib.build_graph()
    lib.search()
    lib = None
    print_mem_stats()
    print()
    return distance, path


# -- Task --

def next_edges(i, *_):
    j = (i + i // 6) % 6
    yield i + 1, j * 2 + 1
    if i % 2 == 0:
        yield i + 6, 7 - j
    else:
        if i > 5:
            yield i - 6, 1


goal_vertex = 120000


# --  Searching with each library --

class TestNetworkX:
    def __init__(self, args):
        self.next_edges, self.goal_vertex, self.graph_size = args
        self.G = None

    def build_graph(self):
        self.G = nx.DiGraph()
        for i in range(self.graph_size):
            self.G.add_weighted_edges_from((i, j, w) for (j, w) in next_edges(i))

    def search(self):
        distance, path = nx.single_source_dijkstra(self.G, 0, target=goal_vertex)
        return distance, path


class TestNoGraphs:
    def __init__(self, args):
        self.next_edges, self.goal_vertex, self.graph_size = args

    def build_graph(self):
        pass

    def search(self):
        traversal = nog.TraversalShortestPaths(self.next_edges)
        v = traversal.start_from(0, build_paths=True).go_to(self.goal_vertex)
        return traversal.distance, traversal.paths[v]


graph_size = goal_vertex + 10
distance, path = test_run("NetworkX", TestNetworkX, next_edges, goal_vertex, graph_size)

distance, path = test_run("NoGraphs", TestNoGraphs, next_edges, goal_vertex, None)

print("-- Determine highest vertex on path --")
print("Highest vertex:", max(path))


""" -- Results --
-- NetworkX --
Time for graph definition: 0.72 seconds
Time for search: 118.27 seconds
Computed distance: 81673
Start and end of found path: [0, 1, 2, 8, 14] ... [119998, 120004, 120005, 119999]

Memory peak: 13,773,226,768 memory blocks

-- NoGraphs --
Time for graph definition: 0.0 seconds
Time for search: 0.26 seconds
Computed distance: 81673
Start and end of found path: (0, 1, 2, 8, 14) ... (119998, 120004, 120005, 119999)

Memory peak: 15,787,428 memory blocks

-- Determine highest vertex on path --
Highest vertex: 120005

Process finished with exit code 0
"""
