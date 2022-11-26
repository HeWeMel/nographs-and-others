import tracemalloc
import gc
import timeit

from nographs_and_others.library_adapter import AdaptLibrary


class PerformanceTest:
    def prepare_stats(self):
        gc.collect()

    def start_time_stats(self):
        return timeit.default_timer()

    def print_time_stats(self, start, message="Time:") -> int:
        stop = timeit.default_timer()
        seconds = round(stop - start, 3)
        print(message, f"{seconds:.3f}", "seconds")
        return seconds

    def start_mem_stats(self):
        tracemalloc.start()
        tracemalloc.reset_peak()  # reset peak of previous execution parts

    def current_mem_stats(self):
        mem_size, mem_peak = tracemalloc.get_traced_memory()
        return mem_peak

    def print_mem_stats(self, mem_peak, message="Memory peak:") -> int:
        mem_bytes = int(mem_peak)
        print(message, f"{mem_bytes:,} bytes")
        return mem_bytes

    def stop_mem_stats(self):
        tracemalloc.stop()


class PerformanceTestBuildAndAnalyze(PerformanceTest):
    def __init__(self):
        # warmup of measurement tools
        self.prepare_stats()
        self.start_time_stats()
        self.start_mem_stats()
        self.current_mem_stats()
        self.stop_mem_stats()

    def warmup(self, library_adaptor_cls: type[AdaptLibrary]) -> int:
        print("--", library_adaptor_cls.name, "--")

        # warmup of connection to library core
        self.prepare_stats()
        timer = self.start_time_stats()

        library_adaptor_cls.warm_up()
        return self.print_time_stats(timer, "> Time for warmup")

    def test_runtime(self,
                     library_adaptor_cls: type[AdaptLibrary],
                     test_case) -> tuple[int, int]:
        print("--", library_adaptor_cls.name, "runtime --")

        lib = library_adaptor_cls()
        has_build_graph = library_adaptor_cls.has_build_graph
        test_case.set_graph_specs(lib)
        self.prepare_stats()
        timer = self.start_time_stats()

        if has_build_graph:
            test_case.build_graph(lib)
            graph_seconds = self.print_time_stats(timer, "> Time for graph definition:")
        else:
            graph_seconds = 0

        test_case.search(lib, False, False)
        del lib
        total_seconds = self.print_time_stats(timer, "> Time for graph and analysis:")
        self.prepare_stats()
        return graph_seconds, total_seconds

    def test_needed_memory(self,
                           library_adaptor_cls: type[AdaptLibrary],
                           test_case) -> tuple[int, int]:
        print("--", library_adaptor_cls.name, "memory --")

        lib = library_adaptor_cls()
        has_build_graph = library_adaptor_cls.has_build_graph
        test_case.set_graph_specs(lib)
        self.prepare_stats()
        _ = test_case.next_edges_function()
        self.start_mem_stats()

        if has_build_graph:
            test_case.build_graph(lib)
            mem_peak = self.current_mem_stats()
            graph_mem = self.print_mem_stats(
                mem_peak, "> Peak memory for graph definition:")
        else:
            graph_mem = 0

        test_case.search(lib, True, True)
        mem_peak = self.current_mem_stats()
        total_mem = self.print_mem_stats(
            mem_peak, "> Total peak memory for graph and analysis:"
        )
        self.stop_mem_stats()
        del lib
        self.prepare_stats()
        return graph_mem, total_mem
