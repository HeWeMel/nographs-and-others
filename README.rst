**This project**

The purpose of this project is to compare the performance of the
python graph library NoGraphs with other graph libraries.

Homepage of the documentation of NoGraphs: https://nographs.readthedocs.io

**The libraries**

- NoGraphs

  - Description: "Graph analysis - the lazy (evaluation) way: Analysis
    on the fly, for graphs, that are computed and/or adapted on the fly."
  - Languages: Python
  - PyPI package: https://pypi.org/project/nographs

- igraph

  - Description: "Python interface to the igraph high performance graph
    library, primarily aimed at complex network research and analysis."
  - Languages: Python and C
  - PyPI package: https://pypi.org/project/igraph

- retworkx

  - Description: "High performance graph data structures and algorithms"
  - Languages: Python and Rust
  - PyPI package: https://pypi.org/project/retworkx

- networkx

  - Description: "Python package for creating and manipulating graphs and networks"
  - Languages: Python
  - PyPI package: https://pypi.org/project/networkx

All libraries are used in the newest version available at Nov. 13th 2022.

**The setup**

Test machine: Core i5-4570, 3.2 Ghz, 4 cores, 16 GB memory, Windows.

In other words: A small office PC, that is nine years old.

Python: 3.10

(Will be updated to 3.11 when all used dependencies can be fulfilled)


**The graph**

The graph used in the test is defined by the following function. For a
given vertex i, it yields the edges starting at i as tuples (vertex, weight).

.. code-block:: python

    >>> def next_edges(i, _):
    ...     j = (i + i // 6) % 6
    ...     yield i + 1, j * 2 + 1
    ...     if i % 2 == 0:
    ...         yield i + 6, 7 - j
    ...     elif i % 1200000 > 5:
    ...         yield i - 6, 1

**Tasks and demanded results**

A. **Base scenario: Full search**

  In this scenario, a graph has to be (nearly) **fully searched**
  for solving the respective analysis task.

  1. **BFS: 1.2 M vertices.**
     Compute depth of vertex 1,200,000 from start vertex 0.

  2. **Dijkstra: 1,2 M vertices.**
     Compute distances of vertices 1,000,000 and 1,150,000 and 1,200,000
     from vertex 0.

  3. **Dijkstra: 1,2 M vertices.**
     Compute shortest path from vertex 0 to vertex 1,200,000.

  4. **Dijkstra, simplified task: 100 T vertices.**
     Compute shortest path to vertex 100,000.

B. **Scenario variant: Partial search 33%**

   **Dijkstra: 3,6 M vertices.**
   Compute distance of vertex 2,400,000 from vertex 1,200,000.

   The analysis results shows, that only 33% of the graph really needs
   to be regarded for solving this task.

C. **Scenario variant: Three analysis runs**

   **Dijkstra: 1,2 M vertices (like in 2.)**

   In this scenario, three analysis runs are performed for a graph built
   only once.

NoGraphs can directly solve these tasks based on the given infinite graph.
The other libraries get as hint, what part of the graph they can focus on
to solve the tasks.

**The results**

The following tables show the results of the tests.

Please see the homepage of the documentation of NoGraphs
(https://nographs.readthedocs.io)
for an interpretation of these results.

A. 1. Breadth first search, 1.20 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.14 | ____________0 | ____67,948,224 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __1.66 | ____________0 | _______164,906 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B | _0.00 | __1.30 | ____________0 | _____1,232,556 |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __1.17 | ____________0 | ____10,781,476 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __1.66 | ____________0 | _______161,232 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B | _0.00 | __1.29 | ____________0 | _____1,232,412 |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __1.68 | ____________0 | _______160,976 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __1.69 | ____________0 | _______160,976 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   | _0.00 | __1.33 | ____________0 | _____1,232,156 |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __1.14 | ____________0 | _______169,686 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.95 | _14.58 | ___21,531,780 | ____21,531,780 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.64 | __2.66 | ___33,594,160 | ____76,761,129 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _8.86 | _10.65 | 1,417,015,717 | _1,479,936,905 |
+-----------+-------+--------+---------------+----------------+

A. 2. Dijkstra distances, 1,2 M vertices, 3 goals:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.45 | ____________0 | ____82,489,608 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __2.04 | ____________0 | _____9,619,092 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __2.04 | ____________0 | _____9,616,420 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __2.28 | ____________0 | _____4,915,489 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __2.05 | ____________0 | _____9,616,420 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __2.28 | ____________0 | _____4,915,089 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __2.27 | ____________0 | _____4,915,089 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.82 | _14.34 | ___21,530,892 | ____21,530,892 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.62 | __1.97 | ___33,593,824 | ____33,596,252 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _8.86 | _11.60 | 1,417,016,696 | _1,541,442,000 |
+-----------+-------+--------+---------------+----------------+

B. Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.44 | ____________0 | ____82,494,776 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __2.03 | ____________0 | ____19,482,160 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __2.03 | ____________0 | ____19,482,160 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __2.35 | ____________0 | ____10,166,713 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __2.04 | ____________0 | ____19,482,160 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __2.35 | ____________0 | ____10,166,713 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __2.35 | ____________0 | ____10,166,713 |
+-----------+-------+--------+---------------+----------------+
| nog+shift | _0.00 | __2.75 | ____________0 | _____4,916,593 |
+-----------+-------+--------+---------------+----------------+
| igraph    |110.30 | 110.90 | ___59,975,244 | ____59,975,244 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _4.89 | __5.66 | __100,793,656 | ___100,794,448 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

C. Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __7.33 | ____________0 | ____82,488,320 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __6.08 | ____________0 | _____9,617,068 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __6.08 | ____________0 | _____9,617,068 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __6.79 | ____________0 | _____4,915,729 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __6.07 | ____________0 | _____9,617,068 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __6.80 | ____________0 | _____4,915,729 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __6.79 | ____________0 | _____4,915,729 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.17 | _14.63 | ___21,530,892 | ____21,530,892 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.63 | __2.58 | ___33,593,824 | ____33,594,756 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

A. 3. Dijkstra path and distance, 1,2 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.62 | ____________0 | ___126,332,524 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __2.19 | ____________0 | ____46,153,544 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __2.20 | ____________0 | ____46,153,544 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __2.43 | ____________0 | ____41,452,352 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __2.22 | ____________0 | ____26,988,580 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __2.45 | ____________0 | ____22,287,388 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __2.63 | ____________0 | ____22,287,388 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.25 | _13.78 | ___21,530,892 | ____30,690,568 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

A. 4. Dijkstra path and distance, 100 T vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.22 | ____________0 | ____15,793,736 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.18 | ____________0 | _____4,004,268 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.18 | ____________0 | _____4,002,956 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.20 | ____________0 | _____3,532,748 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.18 | ____________0 | _____2,331,378 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.21 | ____________0 | _____1,860,380 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __0.21 | ____________0 | _____1,859,932 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _0.19 | __0.23 | ____2,867,708 | _____2,867,708 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _0.14 | _57.84 | ____2,793,880 | _____2,989,541 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _0.67 | _82.67 | __123,319,124 | _9,593,863,188 |
+-----------+-------+--------+---------------+----------------+

Extra: Depth first search, 1 M vertices, random graph, exhaustive traverse

(So far, not part of the benchmark. Will be included in future versions.)

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __7.22 | ____________0 | ___270,432,188 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __7.25 | ____________0 | ___211,978,102 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B | _0.00 | __5.98 | ____________0 | ___212,871,191 |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __6.75 | ____________0 | ___219,924,256 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __7.89 | ____________0 | ___211,978,102 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B | _0.00 | __5.97 | ____________0 | ___212,871,191 |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __7.36 | ____________0 | ____23,904,842 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __7.36 | ____________0 | ____23,904,842 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   | _0.00 | __6.05 | ____________0 | ____24,797,931 |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __5.59 | ____________0 | ____23,911,252 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+


The following text is the detailed output of the tests::

    ===== Warmup of libraries =====
    -- NoGraphs --
    > Time for warmup 0.000 seconds
    -- nog@IntId --
    > Time for warmup 0.000 seconds
    -- @IntIdA0B --
    > Time for warmup 0.000 seconds
    -- @IntIdL0B --
    > Time for warmup 0.000 seconds
    -- @IntIdF --
    > Time for warmup 0.000 seconds
    -- @IntIdF0B --
    > Time for warmup 0.000 seconds
    -- nog@Int --
    > Time for warmup 0.000 seconds
    -- @IntF --
    > Time for warmup 0.000 seconds
    -- @IntF0B --
    > Time for warmup 0.000 seconds
    -- nog+intset --
    > Time for warmup 0.000 seconds
    -- nog+shift --
    > Time for warmup 0.000 seconds
    -- igraph --
    > Time for warmup 0.812 seconds
    -- RetworkX --
    > Time for warmup 0.000 seconds
    -- NetworkX --
    > Time for warmup 0.000 seconds

    ---- Characteristics of the test cases ----
    Breadth first search, 1.20 M vertices, 1 goal:
      vertices_count=1199991, min_vertex=0, max_vertex=1200000
    Dijkstra distances, 1,2 M vertices, 3 goals:
      vertices_count=1200002, min_vertex=0, max_vertex=1200006
    Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded:
      vertices_count=1200000, min_vertex=1200000, max_vertex=2400004
    Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times:
      vertices_count=1200002, min_vertex=0, max_vertex=1200006
    Dijkstra path and distance, 100 T vertices, 1 goal:
      vertices_count=100002, min_vertex=0, max_vertex=100008
    Dijkstra path and distance, 1,2 M vertices, 1 goal:
      vertices_count=1200002, min_vertex=0, max_vertex=1200006
    Depth first search, 1M vertices, exhaustive search:
      vertices_count=975509, min_vertex=0, max_vertex=999999

    ===== Test case: Breadth first search, 1.20 M vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 67,948,224 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.139 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.150 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.145 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.133 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.136 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 164,906 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.662 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.658 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.656 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.656 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.665 seconds


    ---- Test run number 0  ----
    -- @IntIdA0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,232,556 bytes
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 1.299 seconds

    ---- Test run number 1  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 1.289 seconds

    ---- Test run number 2  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 1.296 seconds

    ---- Test run number 3  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 1.342 seconds

    ---- Test run number 4  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 1.292 seconds


    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 10,781,476 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.173 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.171 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.169 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.173 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.171 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 161,232 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.659 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.657 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.658 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.662 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.655 seconds


    ---- Test run number 0  ----
    -- @IntIdF0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,232,412 bytes
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 1.290 seconds

    ---- Test run number 1  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 1.291 seconds

    ---- Test run number 2  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 1.291 seconds

    ---- Test run number 3  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 1.292 seconds

    ---- Test run number 4  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 1.295 seconds


    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 160,976 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 1.683 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.680 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.674 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.683 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.681 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 160,976 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 1.689 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.686 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.706 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.681 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.685 seconds


    ---- Test run number 0  ----
    -- @IntF0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,232,156 bytes
    -- @IntF0B runtime --
    > Time for graph and analysis: 1.330 seconds

    ---- Test run number 1  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 1.329 seconds

    ---- Test run number 2  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 1.330 seconds

    ---- Test run number 3  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 1.327 seconds

    ---- Test run number 4  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 1.368 seconds


    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 169,686 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 1.147 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.139 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.152 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.143 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.144 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,531,780 bytes
    Computed depth: 200000
    > Total peak memory for graph and analysis: 21,531,780 bytes
    -- igraph runtime --
    > Time for graph definition: 13.958 seconds
    > Time for graph and analysis: 14.590 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 13.940 seconds
    > Time for graph and analysis: 14.574 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 13.955 seconds
    > Time for graph and analysis: 14.582 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 13.902 seconds
    > Time for graph and analysis: 14.524 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 13.953 seconds
    > Time for graph and analysis: 14.576 seconds


    ---- Test run number 0  ----
    -- RetworkX memory --
    > Peak memory for graph definition: 33,594,160 bytes
    Computed depth: 200000
    > Total peak memory for graph and analysis: 76,761,129 bytes
    -- RetworkX runtime --
    > Time for graph definition: 1.635 seconds
    > Time for graph and analysis: 2.638 seconds

    ---- Test run number 1  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.629 seconds
    > Time for graph and analysis: 2.675 seconds

    ---- Test run number 2  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.650 seconds
    > Time for graph and analysis: 2.657 seconds

    ---- Test run number 3  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.638 seconds
    > Time for graph and analysis: 2.664 seconds

    ---- Test run number 4  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.625 seconds
    > Time for graph and analysis: 2.632 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 1,417,015,717 bytes
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,479,936,905 bytes
    -- NetworkX runtime --
    > Time for graph definition: 8.799 seconds
    > Time for graph and analysis: 10.584 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.889 seconds
    > Time for graph and analysis: 10.703 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 9.204 seconds
    > Time for graph and analysis: 11.088 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.863 seconds
    > Time for graph and analysis: 10.646 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.790 seconds
    > Time for graph and analysis: 10.571 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __1.14 | ____________0 | ____67,948,224 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __1.66 | ____________0 | _______164,906 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B | _0.00 | __1.30 | ____________0 | _____1,232,556 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __1.17 | ____________0 | ____10,781,476 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __1.66 | ____________0 | _______161,232 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B | _0.00 | __1.29 | ____________0 | _____1,232,412 |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __1.68 | ____________0 | _______160,976 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __1.69 | ____________0 | _______160,976 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   | _0.00 | __1.33 | ____________0 | _____1,232,156 |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __1.14 | ____________0 | _______169,686 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 13.95 | _14.58 | ___21,531,780 | ____21,531,780 |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  | _1.64 | __2.66 | ___33,594,160 | ____76,761,129 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _8.86 | _10.65 | 1,417,015,717 | _1,479,936,905 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 82,489,608 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.442 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.454 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.447 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.455 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.450 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 9,619,092 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.042 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.039 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.037 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.050 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.033 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 9,616,420 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.034 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.041 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.039 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.045 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.044 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 4,915,489 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.282 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.280 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.280 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.289 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.561 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 9,616,420 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 2.032 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.046 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.043 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.046 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.046 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 4,915,089 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 2.279 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.273 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.274 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.278 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.276 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 4,915,089 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 2.277 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.276 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.273 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.273 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.270 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,530,892 bytes
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 21,530,892 bytes
    -- igraph runtime --
    > Time for graph definition: 13.857 seconds
    > Time for graph and analysis: 14.405 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 13.755 seconds
    > Time for graph and analysis: 14.295 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 13.817 seconds
    > Time for graph and analysis: 14.338 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 14.358 seconds
    > Time for graph and analysis: 14.872 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 13.814 seconds
    > Time for graph and analysis: 14.329 seconds


    ---- Test run number 0  ----
    -- RetworkX memory --
    > Peak memory for graph definition: 33,593,824 bytes
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 33,596,252 bytes
    -- RetworkX runtime --
    > Time for graph definition: 1.625 seconds
    > Time for graph and analysis: 1.973 seconds

    ---- Test run number 1  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.626 seconds
    > Time for graph and analysis: 1.971 seconds

    ---- Test run number 2  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.623 seconds
    > Time for graph and analysis: 1.973 seconds

    ---- Test run number 3  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.625 seconds
    > Time for graph and analysis: 1.976 seconds

    ---- Test run number 4  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.618 seconds
    > Time for graph and analysis: 1.964 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 1,417,016,696 bytes
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 1,541,442,000 bytes
    -- NetworkX runtime --
    > Time for graph definition: 8.857 seconds
    > Time for graph and analysis: 11.601 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.865 seconds
    > Time for graph and analysis: 11.642 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.799 seconds
    > Time for graph and analysis: 11.520 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.857 seconds
    > Time for graph and analysis: 11.597 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 8.797 seconds
    > Time for graph and analysis: 11.530 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __2.45 | ____________0 | ____82,489,608 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __2.04 | ____________0 | _____9,619,092 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __2.04 | ____________0 | _____9,616,420 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __2.28 | ____________0 | _____4,915,489 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __2.05 | ____________0 | _____9,616,420 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __2.28 | ____________0 | _____4,915,089 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __2.27 | ____________0 | _____4,915,089 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 13.82 | _14.34 | ___21,530,892 | ____21,530,892 |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  | _1.62 | __1.97 | ___33,593,824 | ____33,596,252 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _8.86 | _11.60 | 1,417,016,696 | _1,541,442,000 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 82,494,776 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.434 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.436 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.448 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.439 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.434 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 19,482,160 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.037 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.025 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.027 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.030 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.033 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 19,482,160 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.031 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.037 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.031 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.029 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.027 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 10,166,713 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.344 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.346 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.354 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.349 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.349 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 19,482,160 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 2.035 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.035 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.026 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.034 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.040 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 10,166,713 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 2.345 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.355 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.343 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.345 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.341 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 10,166,713 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 2.346 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.346 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.349 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.343 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.348 seconds


    ---- Test run number 0  ----
    -- nog+shift memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 4,916,593 bytes
    -- nog+shift runtime --
    > Time for graph and analysis: 2.799 seconds

    ---- Test run number 1  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 2.740 seconds

    ---- Test run number 2  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 2.744 seconds

    ---- Test run number 3  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 2.864 seconds

    ---- Test run number 4  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 2.745 seconds


    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 59,975,244 bytes
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 59,975,244 bytes
    -- igraph runtime --
    > Time for graph definition: 110.159 seconds
    > Time for graph and analysis: 110.791 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 110.152 seconds
    > Time for graph and analysis: 110.768 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 110.296 seconds
    > Time for graph and analysis: 110.897 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 111.354 seconds
    > Time for graph and analysis: 111.987 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 110.383 seconds
    > Time for graph and analysis: 110.986 seconds


    ---- Test run number 0  ----
    -- RetworkX memory --
    > Peak memory for graph definition: 100,793,656 bytes
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 100,794,448 bytes
    -- RetworkX runtime --
    > Time for graph definition: 4.893 seconds
    > Time for graph and analysis: 5.655 seconds

    ---- Test run number 1  ----
    -- RetworkX runtime --
    > Time for graph definition: 4.890 seconds
    > Time for graph and analysis: 5.656 seconds

    ---- Test run number 2  ----
    -- RetworkX runtime --
    > Time for graph definition: 4.900 seconds
    > Time for graph and analysis: 5.672 seconds

    ---- Test run number 3  ----
    -- RetworkX runtime --
    > Time for graph definition: 4.866 seconds
    > Time for graph and analysis: 5.627 seconds

    ---- Test run number 4  ----
    -- RetworkX runtime --
    > Time for graph definition: 4.871 seconds
    > Time for graph and analysis: 5.636 seconds



    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __2.44 | ____________0 | ____82,494,776 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __2.03 | ____________0 | ____19,482,160 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __2.03 | ____________0 | ____19,482,160 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __2.35 | ____________0 | ____10,166,713 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __2.04 | ____________0 | ____19,482,160 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __2.35 | ____________0 | ____10,166,713 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __2.35 | ____________0 | ____10,166,713 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift | _0.00 | __2.75 | ____________0 | _____4,916,593 |
    +-----------+-------+--------+---------------+----------------+
    | igraph    |110.30 | 110.90 | ___59,975,244 | ____59,975,244 |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  | _4.89 | __5.66 | __100,793,656 | ___100,794,448 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 82,488,320 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.340 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.314 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.316 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.344 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.333 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 9,617,068 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 6.077 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 6.063 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 6.083 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 6.079 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 6.086 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 9,617,068 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.109 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.067 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.083 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.068 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.077 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 4,915,729 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 6.780 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 6.807 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 6.838 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 6.785 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 6.795 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 9,617,068 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 6.069 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 6.074 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 6.064 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 6.071 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 6.079 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 4,915,729 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 6.783 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 6.794 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 6.796 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 6.806 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 6.806 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 4,915,729 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 6.787 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 6.788 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 6.793 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 6.801 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 6.796 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,530,892 bytes
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 21,530,892 bytes
    -- igraph runtime --
    > Time for graph definition: 13.185 seconds
    > Time for graph and analysis: 14.640 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 13.157 seconds
    > Time for graph and analysis: 14.611 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 13.199 seconds
    > Time for graph and analysis: 14.653 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 13.172 seconds
    > Time for graph and analysis: 14.629 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 13.061 seconds
    > Time for graph and analysis: 14.507 seconds


    ---- Test run number 0  ----
    -- RetworkX memory --
    > Peak memory for graph definition: 33,593,824 bytes
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 33,594,756 bytes
    -- RetworkX runtime --
    > Time for graph definition: 1.617 seconds
    > Time for graph and analysis: 2.573 seconds

    ---- Test run number 1  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.627 seconds
    > Time for graph and analysis: 2.579 seconds

    ---- Test run number 2  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.631 seconds
    > Time for graph and analysis: 2.589 seconds

    ---- Test run number 3  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.628 seconds
    > Time for graph and analysis: 2.574 seconds

    ---- Test run number 4  ----
    -- RetworkX runtime --
    > Time for graph definition: 1.620 seconds
    > Time for graph and analysis: 2.576 seconds



    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __7.33 | ____________0 | ____82,488,320 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __6.08 | ____________0 | _____9,617,068 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __6.08 | ____________0 | _____9,617,068 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __6.79 | ____________0 | _____4,915,729 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __6.07 | ____________0 | _____9,617,068 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __6.80 | ____________0 | _____4,915,729 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __6.79 | ____________0 | _____4,915,729 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 13.17 | _14.63 | ___21,530,892 | ____21,530,892 |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  | _1.63 | __2.58 | ___33,593,824 | ____33,594,756 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra path and distance, 1,2 M vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 126,332,524 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.623 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.624 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.620 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.613 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.619 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 46,153,544 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.198 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.187 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.189 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.192 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.183 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 46,153,544 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.209 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.199 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.196 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.186 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.200 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 41,452,352 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.430 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.430 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.427 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.427 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 2.428 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 26,988,580 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 2.225 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.215 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.214 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.219 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.221 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 22,287,388 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 2.456 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.445 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.451 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.438 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 2.459 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 22,287,388 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 2.634 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.630 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.630 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.635 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.632 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,530,892 bytes
    Computed distance sum: -1.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Distance not computed
    > Total peak memory for graph and analysis: 30,690,568 bytes
    -- igraph runtime --
    > Time for graph definition: 13.248 seconds
    > Time for graph and analysis: 13.769 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 13.308 seconds
    > Time for graph and analysis: 13.834 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 13.220 seconds
    > Time for graph and analysis: 13.780 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 13.244 seconds
    > Time for graph and analysis: 13.781 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 13.271 seconds
    > Time for graph and analysis: 13.817 seconds




    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __2.62 | ____________0 | ___126,332,524 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __2.19 | ____________0 | ____46,153,544 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __2.20 | ____________0 | ____46,153,544 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __2.43 | ____________0 | ____41,452,352 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __2.22 | ____________0 | ____26,988,580 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __2.45 | ____________0 | ____22,287,388 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __2.63 | ____________0 | ____22,287,388 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 13.25 | _13.78 | ___21,530,892 | ____30,690,568 |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra path and distance, 100 T vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 15,793,736 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.226 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.222 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.226 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.223 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.223 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 4,004,268 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.180 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.188 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.180 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.181 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.180 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 4,002,956 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.179 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.186 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.181 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.184 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.181 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 3,532,748 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.204 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.206 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.204 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.204 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.205 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 2,331,378 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 0.182 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.188 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.182 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.184 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.182 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 1,860,380 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 0.204 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.211 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.206 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.205 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.207 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 1,859,932 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 0.204 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.210 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.207 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.207 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.209 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 2,867,708 bytes
    Computed distance sum: -1.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Distance not computed
    > Total peak memory for graph and analysis: 2,867,708 bytes
    -- igraph runtime --
    > Time for graph definition: 0.202 seconds
    > Time for graph and analysis: 0.245 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 0.187 seconds
    > Time for graph and analysis: 0.231 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 0.184 seconds
    > Time for graph and analysis: 0.227 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 0.185 seconds
    > Time for graph and analysis: 0.228 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 0.186 seconds
    > Time for graph and analysis: 0.228 seconds


    ---- Test run number 0  ----
    -- RetworkX memory --
    > Peak memory for graph definition: 2,793,880 bytes
    Computed distance sum: -1.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Distance not computed
    > Total peak memory for graph and analysis: 2,989,541 bytes
    -- RetworkX runtime --
    > Time for graph definition: 0.137 seconds
    > Time for graph and analysis: 37.615 seconds

    ---- Test run number 1  ----
    -- RetworkX runtime --
    > Time for graph definition: 0.136 seconds
    > Time for graph and analysis: 51.053 seconds

    ---- Test run number 2  ----
    -- RetworkX runtime --
    > Time for graph definition: 0.138 seconds
    > Time for graph and analysis: 57.842 seconds

    ---- Test run number 3  ----
    -- RetworkX runtime --
    > Time for graph definition: 0.151 seconds
    > Time for graph and analysis: 65.491 seconds

    ---- Test run number 4  ----
    -- RetworkX runtime --
    > Time for graph definition: 0.151 seconds
    > Time for graph and analysis: 65.562 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 123,319,124 bytes
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 9,593,863,188 bytes
    -- NetworkX runtime --
    > Time for graph definition: 0.673 seconds
    > Time for graph and analysis: 91.608 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.674 seconds
    > Time for graph and analysis: 80.517 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.672 seconds
    > Time for graph and analysis: 82.669 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.667 seconds
    > Time for graph and analysis: 88.156 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.670 seconds
    > Time for graph and analysis: 73.647 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.22 | ____________0 | ____15,793,736 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.18 | ____________0 | _____4,004,268 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.18 | ____________0 | _____4,002,956 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.20 | ____________0 | _____3,532,748 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.18 | ____________0 | _____2,331,378 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.21 | ____________0 | _____1,860,380 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __0.21 | ____________0 | _____1,859,932 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _0.19 | __0.23 | ____2,867,708 | _____2,867,708 |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  | _0.14 | _57.84 | ____2,793,880 | _____2,989,541 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _0.67 | _82.67 | __123,319,124 | _9,593,863,188 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Depth first search, 1M vertices, exhaustive search =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 270,432,188 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.223 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.222 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.249 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.226 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 7.223 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 211,978,102 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 7.247 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 7.243 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 7.254 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 7.253 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 7.248 seconds


    ---- Test run number 0  ----
    -- @IntIdA0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 212,871,191 bytes
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 5.988 seconds

    ---- Test run number 1  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 5.983 seconds

    ---- Test run number 2  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 5.977 seconds

    ---- Test run number 3  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 5.988 seconds

    ---- Test run number 4  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 5.975 seconds


    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 219,924,256 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.241 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.319 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.755 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.856 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 6.860 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 211,978,102 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 7.898 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 7.896 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 7.890 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 7.864 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 7.852 seconds


    ---- Test run number 0  ----
    -- @IntIdF0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 212,871,191 bytes
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 5.992 seconds

    ---- Test run number 1  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 5.973 seconds

    ---- Test run number 2  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 5.987 seconds

    ---- Test run number 3  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 5.961 seconds

    ---- Test run number 4  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 5.965 seconds


    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 23,904,842 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 7.367 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 7.374 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 7.356 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 7.353 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 7.361 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 23,904,842 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 7.372 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 7.357 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 7.358 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 7.352 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 7.354 seconds


    ---- Test run number 0  ----
    -- @IntF0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 24,797,931 bytes
    -- @IntF0B runtime --
    > Time for graph and analysis: 6.042 seconds

    ---- Test run number 1  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 6.050 seconds

    ---- Test run number 2  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 6.055 seconds

    ---- Test run number 3  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 6.064 seconds

    ---- Test run number 4  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 6.045 seconds


    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 23,911,252 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 5.618 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 5.585 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 5.589 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 5.587 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 5.597 seconds






    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __7.22 | ____________0 | ___270,432,188 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __7.25 | ____________0 | ___211,978,102 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B | _0.00 | __5.98 | ____________0 | ___212,871,191 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __6.75 | ____________0 | ___219,924,256 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __7.89 | ____________0 | ___211,978,102 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B | _0.00 | __5.97 | ____________0 | ___212,871,191 |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __7.36 | ____________0 | ____23,904,842 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __7.36 | ____________0 | ____23,904,842 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   | _0.00 | __6.05 | ____________0 | ____24,797,931 |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __5.59 | ____________0 | ____23,911,252 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
