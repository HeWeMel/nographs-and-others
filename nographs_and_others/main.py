import collections
from collections.abc import Container
from typing import Union

from nographs_and_others.performance_tests import PerformanceTestBuildAndAnalyze
from nographs_and_others.test_cases import (
    TestCase,
    CaseBreadthFirstSearch,
    CaseDijkstraDistance,
    CaseDijkstraDistancePart,
    CaseDijkstraDistanceThreeTimes,
    CaseDijkstraPathAndDistance,
    CaseDijkstraPathAndDistanceSmall,
    CaseDepthFirstSearch,
)
from nographs_and_others.adapt_nographs import *
from nographs_and_others.adapt_nographs_int_ids import *
from nographs_and_others.adapt_nographs_all_int import *
from nographs_and_others.adapt_nographs_all_int_and_bitset import *
from nographs_and_others.adapt_nographs_all_int_id_shift import *
from nographs_and_others.adapt_igraph import *
from nographs_and_others.adapt_retworkx import *
from nographs_and_others.adapt_networkx import *


# --- Define test suite ---
# Test case classes and their assigned id
tests_and_id: list[tuple[type[TestCase], int]] = [
    (CaseBreadthFirstSearch, 0),
    (CaseDijkstraDistance, 1),
    (CaseDijkstraDistancePart, 2),
    (CaseDijkstraDistanceThreeTimes, 3),
    (CaseDijkstraPathAndDistance, 4),
    (CaseDijkstraPathAndDistanceSmall, 5),
    (CaseDepthFirstSearch, 6),
]
all_test_ids = {case_id for case, case_id in tests_and_id}
# Library adapter class and allowed test ids
adapter_and_allowed_tests: list[tuple[type[AdaptLibrary], Container[int]]] = [
    (AdaptNoGraphs, range(99)),  # base case "hashes", "flexibility optimum"
    (AdaptNoGraphsIntIDsBitsPreferArrays, range(99)),  # base case "int ids"
    (AdaptNoGraphsIntIDsNoBitsPreferArrays, {0, 6}),
    (AdaptNoGraphsIntIDsNoBitsPreferLists, range(99)),  # "speed optimum"
    (AdaptNoGraphsIntIDsFloatsBits, range(99)),  # "memory optimum for int vertices"
    (AdaptNoGraphsIntIDsFloatsNoBits, {0, 6}),
    (AdaptNoGraphsAllIntBits, range(99)),  # base case "int vertices & ids"
    (AdaptNoGraphsAllIntFloatsBits, range(99)),  # "memory optimum"
    (AdaptNoGraphsAllIntFloatsNoBits, {0, 6}),
    (AdaptNoGraphsAllIntAndBitset, range(99)),
    (AdaptNoGraphsAllIntAndIDsShift, {2}),
    (AdaptIgraph, range(6)),
    (AdaptRetworkX, {0, 1, 2, 3, 5}),  # excluded from test 4 because of memory overflow
    (AdaptNetworkX, {0, 1, 5}),  # excluded from test 2, 3, 4 because of runtime
]
# Perform each runtime test 5 times
no_of_test_runs = 5  # 5
# Test memory consumption only at first test run
test_runs_with_memory_test = range(1)  # 1

compute_regarded_vertices = True


# --- Setup, warmup, special computations ---
test = PerformanceTestBuildAndAnalyze()

print("===== Warmup of libraries =====")
for adapter_class, _ in adapter_and_allowed_tests:
    seconds = test.warmup(adapter_class)
print()

if compute_regarded_vertices:
    print("---- Characteristics of the test cases ----")
    for case_class, case_id in tests_and_id:
        case = case_class()
        case.print_case_infos()
    print()


# --- Perform tests of suite ---

def my_median(lst: Union[list[float], list[int]], fmt: str) -> str:
    """Return median of list formatted with given format as string,
    and "n.a." in case of empty list."""
    lst_length = len(lst)
    if lst_length == 0:
        return "n.a."
    lst_sorted = sorted(lst)
    lst_median = lst_sorted[lst_length // 2]
    return fmt.format(lst_median)


result_header = """\
+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
""".splitlines()
result_separator = result_header[2]

for case_class, case_id in tests_and_id:
    print("===== Test case:", case_class.name, "=====")
    case = case_class()

    # Execute test case
    runtime_graph = collections.defaultdict(list)
    runtime_total = collections.defaultdict(list)
    memory_graph = collections.defaultdict(list)
    memory_total = collections.defaultdict(list)
    for adapter_class, allowed_test_ids in adapter_and_allowed_tests:
        if case_id in allowed_test_ids:
            for test_run in range(no_of_test_runs):
                print("---- Test run number", test_run, " ----")
                if test_run in test_runs_with_memory_test:
                    graph_mem, total_mem = test.test_needed_memory(
                        adapter_class, case)
                    memory_graph[adapter_class.__name__].append(graph_mem)
                    memory_total[adapter_class.__name__].append(total_mem)
                graph_seconds, total_seconds = test.test_runtime(
                    adapter_class, case)
                runtime_graph[adapter_class.__name__].append(graph_seconds)
                runtime_total[adapter_class.__name__].append(total_seconds)
                print()
        print()

    # Print result table
    result = list(result_header)
    for adapter_class, allowed_test_ids in adapter_and_allowed_tests:
        s = "| {:<10}|{:>6} |{:>7} |{:>14} |{:>15} |".format(
            adapter_class.name,
            my_median(runtime_graph[adapter_class.__name__], "{:_>5.2f}"),
            my_median(runtime_total[adapter_class.__name__], "{:_>6.2f}"),
            my_median(memory_graph[adapter_class.__name__], "{:_>13,}"),
            my_median(memory_total[adapter_class.__name__], "{:_>14,}")
        )
        result.append(s)
        result.append(result_separator)
    print("\n".join(result))
    print()
    print()
