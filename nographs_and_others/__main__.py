from collections.abc import Container

from nographs_and_others.ressources import libraries, libraries_missing
from nographs_and_others.run import run_tests
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

if "intbitset" in libraries:
    from nographs_and_others.adapt_nographs_all_int_and_bitset import *
from nographs_and_others.adapt_nographs_all_int_id_shift import *
if "igraph" in libraries:
    from nographs_and_others.adapt_igraph import *
if "rustworkx" in libraries:
    from nographs_and_others.adapt_rustworkx import *
if "networkx" in libraries:
    from nographs_and_others.adapt_networkx import *

# --- Print found libraries ---

print("Libraries:", ", ".join(libraries) if libraries else "-")
print("Missing libraries:", ", ".join(libraries_missing) if libraries_missing else "-")


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

# Library adapter classes and allowed test ids per adapter
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
]
if "intbitset" in libraries:
    adapter_and_allowed_tests.append((AdaptNoGraphsAllIntAndBitset, range(99)))
adapter_and_allowed_tests.append((AdaptNoGraphsAllIntAndIDsShift, {2}))
if "igraph" in libraries:
    adapter_and_allowed_tests.append((AdaptIgraph, range(6)))
if "rustworkx" in libraries:
    # excluded from test 4 because of memory overflow
    adapter_and_allowed_tests.append((AdaptRustworkX, {0, 1, 2, 3, 5}))
if "networkx" in libraries:
    # excluded from test 4 because of runtime
    adapter_and_allowed_tests.append((AdaptNetworkX, {0, 1, 2, 3, 5}))

# Test parameters
no_of_test_runs = 5  # Perform each runtime test 5 times
test_runs_with_memory_test = range(1)  # Test memory consumption only at run 0
compute_regarded_vertices = True  # Needed for test documentation only

# --- Execute tests ---
run_tests(
    tests_and_id,
    adapter_and_allowed_tests,
    no_of_test_runs,
    test_runs_with_memory_test,
    compute_regarded_vertices,
)
