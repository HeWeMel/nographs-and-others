import sys
import collections
from typing import Union
from collections.abc import Container

from nographs_and_others.performance_tests import PerformanceTestBuildAndAnalyze
from nographs_and_others.library_adapter import AdaptLibrary
from nographs_and_others.test_cases import TestCase
from performance_tests import can_do_memory_test

""" Perform tests of suite """


def _my_median(lst: Union[list[float], list[int]], fmt: str) -> str:
    """Return median of list formatted with given format as string,
    and "n.a." in case of empty list."""
    lst_length = len(lst)
    if lst_length == 0:
        return "n.a."
    lst_sorted = sorted(lst)
    lst_median = lst_sorted[lst_length // 2]
    return fmt.format(lst_median)


def run_tests(
    tests_and_id: list[tuple[type[TestCase], int]],
    adapter_and_allowed_tests: list[tuple[type[AdaptLibrary], Container[int]]],
    no_of_test_runs: int,
    test_runs_with_memory_test: Container[int],
    compute_regarded_vertices: bool,
):
    """
    Run the tests for the adapters they are allowed for.

    :param tests_and_id: Tests to run, and their respective number
    :param adapter_and_allowed_tests: Adapters to use, and the tests (number) to run
        for them
    :param no_of_test_runs: Number of times each test is to be performed. The median
        of the results of the test runs will be used as overall result.
    :param test_runs_with_memory_test: Also run memory tests, not only runtime tests.
    :param compute_regarded_vertices: Compute how many vertices have to be regarded
        to solve the respective problem.
    """
    print(f"Python {sys.version}")

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
                    if test_run in test_runs_with_memory_test and can_do_memory_test:
                        graph_mem, total_mem = test.test_needed_memory(
                            adapter_class, case
                        )
                        memory_graph[adapter_class.__name__].append(graph_mem)
                        memory_total[adapter_class.__name__].append(total_mem)
                    graph_seconds, total_seconds = test.test_runtime(
                        adapter_class, case
                    )
                    runtime_graph[adapter_class.__name__].append(graph_seconds)
                    runtime_total[adapter_class.__name__].append(total_seconds)
                    print()
            print()

        # Print result table
        result = list(result_header)
        for adapter_class, allowed_test_ids in adapter_and_allowed_tests:
            s = "| {:<10}|{:>6} |{:>7} |{:>14} |{:>15} |".format(
                adapter_class.name,
                _my_median(runtime_graph[adapter_class.__name__], "{:_>5.2f}"),
                _my_median(runtime_total[adapter_class.__name__], "{:_>6.2f}"),
                _my_median(memory_graph[adapter_class.__name__], "{:_>13,}"),
                _my_median(memory_total[adapter_class.__name__], "{:_>14,}"),
            )
            result.append(s)
            result.append(result_separator)
        print("\n".join(result))
        print()
        print()
