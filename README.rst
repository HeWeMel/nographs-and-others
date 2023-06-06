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

- rustworkx

  - Description: "High performance general purpose graph library."
  - Languages: Python and Rust
  - PyPI package: https://pypi.org/project/rustworkx

- networkx

  - Description: "Python package for creating and manipulating graphs and networks."
  - Languages: Python
  - PyPI package: https://pypi.org/project/networkx

Each library is used in its newest version available at May 31, 2023. See
file requirements.txt for details.

**The setup**

Test machine: Core i5-13400, 2500 MHz, 10 cores, 16 logical cores, Windows.

In other words: A small office PC.

Interpreters:

- CPython 3.11.3 running Python 3.11
- PyPy 7.3.11 running Python 3.9.16

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

``A.`` **Base scenario: Full search**

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

``B.`` **Scenario variant: Partial search 33%**

   **Dijkstra: 3,6 M vertices.**
   Compute distance of vertex 2,400,000 from vertex 1,200,000.

   The analysis results shows, that only 33% of the graph really needs
   to be regarded for solving this task.

``C.`` **Scenario variant: Three analysis runs**

   **Dijkstra: 1,2 M vertices (like in 2.)**

   In this scenario, three analysis runs are performed for a graph built
   only once.

NoGraphs can directly solve these tasks based on the given infinite graph.
The other libraries get as hint, what part of the graph they can focus on
to solve the tasks.

Please see the homepage of the documentation of NoGraphs
(https://nographs.readthedocs.io)
for an interpretation of the following test results.


**The results für CPython**

The following tables show the results of the tests.

``A. 1.`` Breadth first search, 1.20 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.56 | ____________0 | ____71,952,406 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.76 | ____________0 | _______162,852 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B | _0.00 | __0.63 | ____________0 | _____1,233,700 |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.57 | ____________0 | ____10,782,564 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.76 | ____________0 | _______162,356 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B | _0.00 | __0.63 | ____________0 | _____1,233,444 |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.78 | ____________0 | _______162,004 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.78 | ____________0 | _______161,948 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   | _0.00 | __0.63 | ____________0 | _____1,233,092 |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __0.54 | ____________0 | _______169,858 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _8.72 | __8.99 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| rustworkx | 27.73 | _28.15 | ___39,898,108 | ____86,476,080 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _4.57 | __5.33 | 1,297,009,024 | _1,359,923,768 |
+-----------+-------+--------+---------------+----------------+

``A. 2.`` Dijkstra distances, 1,2 M vertices, 3 goals:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.22 | ____________0 | ____85,283,776 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.97 | ____________0 | _____9,623,396 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.98 | ____________0 | _____9,617,892 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __1.09 | ____________0 | _____4,916,757 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.98 | ____________0 | _____9,617,780 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __1.09 | ____________0 | _____4,916,349 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __1.09 | ____________0 | _____4,916,349 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _8.57 | __8.79 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| rustworkx | 24.68 | _24.82 | ___39,898,300 | ____39,898,300 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _4.56 | __5.73 | 1,297,014,184 | _1,424,230,152 |
+-----------+-------+--------+---------------+----------------+

``B.`` Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.21 | ____________0 | ____85,291,456 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.97 | ____________0 | ____19,483,460 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.97 | ____________0 | ____19,483,460 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __1.13 | ____________0 | ____10,167,969 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.97 | ____________0 | ____19,483,460 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __1.12 | ____________0 | ____10,167,969 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __1.12 | ____________0 | ____10,167,969 |
+-----------+-------+--------+---------------+----------------+
| nog+shift | _0.00 | __1.28 | ____________0 | _____4,916,621 |
+-----------+-------+--------+---------------+----------------+
| igraph    | 74.06 | _74.35 | ___60,035,232 | ____60,035,232 |
+-----------+-------+--------+---------------+----------------+
| rustworkx | 72.24 | _72.56 | __116,698,108 | ___116,698,108 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | 13.78 | _16.33 | 4,016,894,984 | _4,271,338,140 |
+-----------+-------+--------+---------------+----------------+

``C.`` Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __3.66 | ____________0 | ____85,283,480 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __2.91 | ____________0 | _____9,617,916 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __2.92 | ____________0 | _____9,617,916 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __3.27 | ____________0 | _____4,916,517 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __2.91 | ____________0 | _____9,617,916 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __3.27 | ____________0 | _____4,916,517 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __3.27 | ____________0 | _____4,916,517 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _8.31 | __8.99 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| rustworkx | 24.31 | _24.71 | ___39,898,300 | ____39,898,300 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _4.50 | __7.43 | 1,297,014,072 | _1,424,230,128 |
+-----------+-------+--------+---------------+----------------+

``A. 3.`` Dijkstra path and distance, 1,2 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.29 | ____________0 | ___130,551,348 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __1.03 | ____________0 | ____49,354,272 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __1.03 | ____________0 | ____49,353,368 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __1.15 | ____________0 | ____44,652,028 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __1.06 | ____________0 | ____26,989,554 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __1.17 | ____________0 | ____22,287,592 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __1.16 | ____________0 | ____22,287,592 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _8.28 | __8.52 | ___21,590,880 | ____31,823,628 |
+-----------+-------+--------+---------------+----------------+
| rustworkx |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

``A. 4.`` Dijkstra path and distance, 100 T vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.11 | ____________0 | ____16,171,992 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.09 | ____________0 | _____4,269,216 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.09 | ____________0 | _____4,269,168 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.10 | ____________0 | _____3,798,928 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.09 | ____________0 | _____2,330,368 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.10 | ____________0 | _____1,860,128 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __0.10 | ____________0 | _____1,860,128 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _0.09 | __0.11 | ____2,927,552 | _____2,927,552 |
+-----------+-------+--------+---------------+----------------+
| rustworkx | _2.40 | _49.23 | ____4,698,364 | _____4,698,364 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _0.32 | _79.22 | __113,316,144 | _9,584,256,016 |
+-----------+-------+--------+---------------+----------------+

Extra: Depth first search, 1 M vertices, random graph, exhaustive traverse

(So far, not part of the benchmark. Will be included in future versions.)

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __3.79 | ____________0 | ___207,510,148 |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __3.29 | ____________0 | ___144,766,134 |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B | _0.00 | __2.65 | ____________0 | ___145,659,147 |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __2.75 | ____________0 | ___152,712,212 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __3.29 | ____________0 | ___144,766,094 |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B | _0.00 | __2.65 | ____________0 | ___145,659,147 |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __3.29 | ____________0 | ____14,770,914 |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __3.30 | ____________0 | ____14,770,914 |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   | _0.00 | __2.65 | ____________0 | ____15,663,967 |
+-----------+-------+--------+---------------+----------------+
| nog+intset| _0.00 | __2.37 | ____________0 | ____14,776,752 |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| rustworkx |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+


The following text is the detailed output of the tests::

    Libraries: rustworkx, networkx, intbitset, igraph
    Missing libraries: -
    Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)]
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
    > Time for warmup 0.482 seconds
    -- rustworkx --
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
    Dijkstra path and distance, 1,2 M vertices, 1 goal:
      vertices_count=1200002, min_vertex=0, max_vertex=1200006
    Dijkstra path and distance, 100 T vertices, 1 goal:
      vertices_count=100002, min_vertex=0, max_vertex=100008
    Depth first search, 1M vertices, exhaustive search:
      vertices_count=975509, min_vertex=0, max_vertex=999999

    ===== Test case: Breadth first search, 1.20 M vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 71,952,406 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.566 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.563 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.564 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.564 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.573 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 162,852 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.759 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.761 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.760 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.757 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.758 seconds


    ---- Test run number 0  ----
    -- @IntIdA0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,233,700 bytes
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.623 seconds

    ---- Test run number 1  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.625 seconds

    ---- Test run number 2  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.628 seconds

    ---- Test run number 3  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.631 seconds

    ---- Test run number 4  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.628 seconds


    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 10,782,564 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.569 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.566 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.568 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.565 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.571 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 162,356 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.760 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.768 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.764 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.764 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.761 seconds


    ---- Test run number 0  ----
    -- @IntIdF0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,233,444 bytes
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.628 seconds

    ---- Test run number 1  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.639 seconds

    ---- Test run number 2  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.633 seconds

    ---- Test run number 3  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.629 seconds

    ---- Test run number 4  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.624 seconds


    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 162,004 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 0.779 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.781 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.778 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.781 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.777 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 161,948 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 0.777 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.787 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.777 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.779 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.774 seconds


    ---- Test run number 0  ----
    -- @IntF0B memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,233,092 bytes
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.631 seconds

    ---- Test run number 1  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.632 seconds

    ---- Test run number 2  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.628 seconds

    ---- Test run number 3  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.630 seconds

    ---- Test run number 4  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.627 seconds


    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed depth: 200000
    > Total peak memory for graph and analysis: 169,858 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 0.537 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.538 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.539 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.542 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.538 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,590,880 bytes
    Computed depth: 200000
    > Total peak memory for graph and analysis: 21,590,880 bytes
    -- igraph runtime --
    > Time for graph definition: 8.730 seconds
    > Time for graph and analysis: 9.001 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 8.702 seconds
    > Time for graph and analysis: 8.983 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 8.804 seconds
    > Time for graph and analysis: 9.081 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 8.682 seconds
    > Time for graph and analysis: 8.956 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 8.717 seconds
    > Time for graph and analysis: 8.990 seconds


    ---- Test run number 0  ----
    -- rustworkx memory --
    > Peak memory for graph definition: 39,898,108 bytes
    Computed depth: 200000
    > Total peak memory for graph and analysis: 86,476,080 bytes
    -- rustworkx runtime --
    > Time for graph definition: 27.631 seconds
    > Time for graph and analysis: 28.048 seconds

    ---- Test run number 1  ----
    -- rustworkx runtime --
    > Time for graph definition: 27.732 seconds
    > Time for graph and analysis: 28.151 seconds

    ---- Test run number 2  ----
    -- rustworkx runtime --
    > Time for graph definition: 27.776 seconds
    > Time for graph and analysis: 28.197 seconds

    ---- Test run number 3  ----
    -- rustworkx runtime --
    > Time for graph definition: 27.743 seconds
    > Time for graph and analysis: 28.155 seconds

    ---- Test run number 4  ----
    -- rustworkx runtime --
    > Time for graph definition: 27.641 seconds
    > Time for graph and analysis: 28.058 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 1,297,009,024 bytes
    Computed depth: 200000
    > Total peak memory for graph and analysis: 1,359,923,768 bytes
    -- NetworkX runtime --
    > Time for graph definition: 4.565 seconds
    > Time for graph and analysis: 5.329 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.573 seconds
    > Time for graph and analysis: 5.317 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.578 seconds
    > Time for graph and analysis: 5.350 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.535 seconds
    > Time for graph and analysis: 5.300 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.596 seconds
    > Time for graph and analysis: 5.346 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.56 | ____________0 | ____71,952,406 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.76 | ____________0 | _______162,852 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B | _0.00 | __0.63 | ____________0 | _____1,233,700 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.57 | ____________0 | ____10,782,564 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.76 | ____________0 | _______162,356 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B | _0.00 | __0.63 | ____________0 | _____1,233,444 |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.78 | ____________0 | _______162,004 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.78 | ____________0 | _______161,948 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   | _0.00 | __0.63 | ____________0 | _____1,233,092 |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __0.54 | ____________0 | _______169,858 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _8.72 | __8.99 | ___21,590,880 | ____21,590,880 |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx | 27.73 | _28.15 | ___39,898,108 | ____86,476,080 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _4.57 | __5.33 | 1,297,009,024 | _1,359,923,768 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 85,283,776 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.221 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.219 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.217 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.218 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.219 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 9,623,396 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.976 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.974 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.972 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.975 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.977 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 9,617,892 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.974 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.978 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.976 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.977 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.976 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 4,916,757 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.092 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.091 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.093 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.091 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.094 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 9,617,780 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 0.978 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.976 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.976 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.972 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.976 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 4,916,349 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 1.094 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.091 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.090 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.087 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.096 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 4,916,349 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 1.093 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.095 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.095 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.094 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.087 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,590,880 bytes
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 21,590,880 bytes
    -- igraph runtime --
    > Time for graph definition: 8.513 seconds
    > Time for graph and analysis: 8.754 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 8.544 seconds
    > Time for graph and analysis: 8.782 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 8.713 seconds
    > Time for graph and analysis: 8.957 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 8.733 seconds
    > Time for graph and analysis: 8.965 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 8.570 seconds
    > Time for graph and analysis: 8.794 seconds


    ---- Test run number 0  ----
    -- rustworkx memory --
    > Peak memory for graph definition: 39,898,300 bytes
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 39,898,300 bytes
    -- rustworkx runtime --
    > Time for graph definition: 25.287 seconds
    > Time for graph and analysis: 25.420 seconds

    ---- Test run number 1  ----
    -- rustworkx runtime --
    > Time for graph definition: 24.682 seconds
    > Time for graph and analysis: 24.824 seconds

    ---- Test run number 2  ----
    -- rustworkx runtime --
    > Time for graph definition: 23.346 seconds
    > Time for graph and analysis: 23.486 seconds

    ---- Test run number 3  ----
    -- rustworkx runtime --
    > Time for graph definition: 24.739 seconds
    > Time for graph and analysis: 24.872 seconds

    ---- Test run number 4  ----
    -- rustworkx runtime --
    > Time for graph definition: 23.404 seconds
    > Time for graph and analysis: 23.541 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 1,297,014,184 bytes
    Computed distance sum: 2279877.0
    > Total peak memory for graph and analysis: 1,424,230,152 bytes
    -- NetworkX runtime --
    > Time for graph definition: 4.547 seconds
    > Time for graph and analysis: 5.715 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.524 seconds
    > Time for graph and analysis: 5.689 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.563 seconds
    > Time for graph and analysis: 5.732 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.565 seconds
    > Time for graph and analysis: 5.734 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.584 seconds
    > Time for graph and analysis: 5.752 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __1.22 | ____________0 | ____85,283,776 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.97 | ____________0 | _____9,623,396 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.98 | ____________0 | _____9,617,892 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __1.09 | ____________0 | _____4,916,757 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.98 | ____________0 | _____9,617,780 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __1.09 | ____________0 | _____4,916,349 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __1.09 | ____________0 | _____4,916,349 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _8.57 | __8.79 | ___21,590,880 | ____21,590,880 |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx | 24.68 | _24.82 | ___39,898,300 | ____39,898,300 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _4.56 | __5.73 | 1,297,014,184 | _1,424,230,152 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 85,291,456 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.211 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.218 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.217 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.212 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.212 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 19,483,460 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.969 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.967 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.969 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.970 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.975 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 19,483,460 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.969 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.968 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.967 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.974 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.968 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 10,167,969 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.130 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.130 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.128 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.128 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.124 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 19,483,460 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 0.976 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.971 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.970 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.965 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.965 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 10,167,969 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 1.116 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.124 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.141 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.125 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.123 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 10,167,969 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 1.125 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.123 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.121 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.123 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.123 seconds


    ---- Test run number 0  ----
    -- nog+shift memory --
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 4,916,621 bytes
    -- nog+shift runtime --
    > Time for graph and analysis: 1.285 seconds

    ---- Test run number 1  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 1.282 seconds

    ---- Test run number 2  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 1.281 seconds

    ---- Test run number 3  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 1.281 seconds

    ---- Test run number 4  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 1.279 seconds


    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 60,035,232 bytes
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 60,035,232 bytes
    -- igraph runtime --
    > Time for graph definition: 73.866 seconds
    > Time for graph and analysis: 74.176 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 74.011 seconds
    > Time for graph and analysis: 74.317 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 74.058 seconds
    > Time for graph and analysis: 74.354 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 74.961 seconds
    > Time for graph and analysis: 75.275 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 74.158 seconds
    > Time for graph and analysis: 74.479 seconds


    ---- Test run number 0  ----
    -- rustworkx memory --
    > Peak memory for graph definition: 116,698,108 bytes
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 116,698,108 bytes
    -- rustworkx runtime --
    > Time for graph definition: 71.985 seconds
    > Time for graph and analysis: 72.298 seconds

    ---- Test run number 1  ----
    -- rustworkx runtime --
    > Time for graph definition: 71.991 seconds
    > Time for graph and analysis: 72.288 seconds

    ---- Test run number 2  ----
    -- rustworkx runtime --
    > Time for graph definition: 72.241 seconds
    > Time for graph and analysis: 72.555 seconds

    ---- Test run number 3  ----
    -- rustworkx runtime --
    > Time for graph definition: 72.247 seconds
    > Time for graph and analysis: 72.563 seconds

    ---- Test run number 4  ----
    -- rustworkx runtime --
    > Time for graph definition: 72.260 seconds
    > Time for graph and analysis: 72.576 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 4,016,894,984 bytes
    Computed distance sum: 816670.0
    > Total peak memory for graph and analysis: 4,271,338,140 bytes
    -- NetworkX runtime --
    > Time for graph definition: 13.893 seconds
    > Time for graph and analysis: 16.482 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 13.705 seconds
    > Time for graph and analysis: 16.265 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 13.778 seconds
    > Time for graph and analysis: 16.349 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 13.700 seconds
    > Time for graph and analysis: 16.299 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 13.794 seconds
    > Time for graph and analysis: 16.326 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __1.21 | ____________0 | ____85,291,456 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.97 | ____________0 | ____19,483,460 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.97 | ____________0 | ____19,483,460 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __1.13 | ____________0 | ____10,167,969 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.97 | ____________0 | ____19,483,460 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __1.12 | ____________0 | ____10,167,969 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __1.12 | ____________0 | ____10,167,969 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift | _0.00 | __1.28 | ____________0 | _____4,916,621 |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 74.06 | _74.35 | ___60,035,232 | ____60,035,232 |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx | 72.24 | _72.56 | __116,698,108 | ___116,698,108 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | 13.78 | _16.33 | 4,016,894,984 | _4,271,338,140 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 85,283,480 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.670 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.663 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.653 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.669 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.662 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 9,617,916 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.911 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.911 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.908 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.911 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 2.902 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 9,617,916 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.916 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.916 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.918 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.920 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.914 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 4,916,517 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.269 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.271 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.265 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.276 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.275 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 9,617,916 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 2.913 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.919 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.916 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.913 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 2.912 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 4,916,517 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 3.269 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.267 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.266 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.272 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.264 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 4,916,517 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 3.272 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 3.267 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 3.262 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 3.275 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 3.271 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,590,880 bytes
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 21,590,880 bytes
    -- igraph runtime --
    > Time for graph definition: 8.307 seconds
    > Time for graph and analysis: 8.995 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 8.408 seconds
    > Time for graph and analysis: 9.050 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 8.354 seconds
    > Time for graph and analysis: 8.992 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 8.313 seconds
    > Time for graph and analysis: 8.960 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 8.255 seconds
    > Time for graph and analysis: 8.895 seconds


    ---- Test run number 0  ----
    -- rustworkx memory --
    > Peak memory for graph definition: 39,898,300 bytes
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 39,898,300 bytes
    -- rustworkx runtime --
    > Time for graph definition: 23.729 seconds
    > Time for graph and analysis: 24.103 seconds

    ---- Test run number 1  ----
    -- rustworkx runtime --
    > Time for graph definition: 24.351 seconds
    > Time for graph and analysis: 24.727 seconds

    ---- Test run number 2  ----
    -- rustworkx runtime --
    > Time for graph definition: 24.346 seconds
    > Time for graph and analysis: 24.736 seconds

    ---- Test run number 3  ----
    -- rustworkx runtime --
    > Time for graph definition: 24.312 seconds
    > Time for graph and analysis: 24.707 seconds

    ---- Test run number 4  ----
    -- rustworkx runtime --
    > Time for graph definition: 23.809 seconds
    > Time for graph and analysis: 24.206 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 1,297,014,072 bytes
    Computed distance sums: 2279877.0 2279877.0 2279877.0
    > Total peak memory for graph and analysis: 1,424,230,128 bytes
    -- NetworkX runtime --
    > Time for graph definition: 4.545 seconds
    > Time for graph and analysis: 7.486 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.467 seconds
    > Time for graph and analysis: 7.401 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.503 seconds
    > Time for graph and analysis: 7.435 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.452 seconds
    > Time for graph and analysis: 7.394 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 4.577 seconds
    > Time for graph and analysis: 7.509 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __3.66 | ____________0 | ____85,283,480 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __2.91 | ____________0 | _____9,617,916 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __2.92 | ____________0 | _____9,617,916 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __3.27 | ____________0 | _____4,916,517 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __2.91 | ____________0 | _____9,617,916 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __3.27 | ____________0 | _____4,916,517 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __3.27 | ____________0 | _____4,916,517 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _8.31 | __8.99 | ___21,590,880 | ____21,590,880 |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx | 24.31 | _24.71 | ___39,898,300 | ____39,898,300 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _4.50 | __7.43 | 1,297,014,072 | _1,424,230,128 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra path and distance, 1,2 M vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 130,551,348 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.297 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.285 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.287 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.299 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.286 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 49,354,272 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.045 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.031 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.033 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.038 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.034 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 49,353,368 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.027 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.028 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.035 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.029 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.035 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 44,652,028 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.157 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.149 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.151 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.148 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.166 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 26,989,554 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 1.058 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.061 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.059 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.058 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.059 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 22,287,592 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 1.167 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.167 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.165 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.163 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.160 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 816674.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Computed distance sum: 816674.0
    > Total peak memory for graph and analysis: 22,287,592 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 1.159 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.156 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.156 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.156 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 1.161 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 21,590,880 bytes
    Computed distance sum: -1.0
    Computed vertex count of path: 283,331
    Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
    Distance not computed
    > Total peak memory for graph and analysis: 31,823,628 bytes
    -- igraph runtime --
    > Time for graph definition: 8.284 seconds
    > Time for graph and analysis: 8.518 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 8.191 seconds
    > Time for graph and analysis: 8.428 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 8.216 seconds
    > Time for graph and analysis: 8.439 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 8.298 seconds
    > Time for graph and analysis: 8.547 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 8.376 seconds
    > Time for graph and analysis: 8.602 seconds




    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __1.29 | ____________0 | ___130,551,348 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __1.03 | ____________0 | ____49,354,272 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __1.03 | ____________0 | ____49,353,368 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __1.15 | ____________0 | ____44,652,028 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __1.06 | ____________0 | ____26,989,554 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __1.17 | ____________0 | ____22,287,592 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __1.16 | ____________0 | ____22,287,592 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _8.28 | __8.52 | ___21,590,880 | ____31,823,628 |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx |  n.a. |   n.a. |          n.a. |           n.a. |
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
    > Total peak memory for graph and analysis: 16,171,992 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.107 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.110 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.110 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.109 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.109 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 4,269,216 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.085 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.085 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.085 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.085 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.084 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 4,269,168 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.084 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.085 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.088 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.086 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.085 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 3,798,928 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.094 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.094 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.097 seconds



    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 2,330,368 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 0.088 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.087 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.086 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.088 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.088 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 1,860,128 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 0.096 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.099 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.099 seconds



    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 1,860,128 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.098 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.096 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 0.096 seconds



    ---- Test run number 0  ----
    -- igraph memory --
    > Peak memory for graph definition: 2,927,552 bytes
    Computed distance sum: -1.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Distance not computed
    > Total peak memory for graph and analysis: 2,927,552 bytes
    -- igraph runtime --
    > Time for graph definition: 0.087 seconds
    > Time for graph and analysis: 0.106 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 0.089 seconds
    > Time for graph and analysis: 0.108 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 0.090 seconds
    > Time for graph and analysis: 0.109 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 0.089 seconds
    > Time for graph and analysis: 0.107 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 0.091 seconds
    > Time for graph and analysis: 0.111 seconds


    ---- Test run number 0  ----
    -- rustworkx memory --
    > Peak memory for graph definition: 4,698,364 bytes
    Computed distance sum: -1.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Distance not computed
    > Total peak memory for graph and analysis: 4,698,364 bytes
    -- rustworkx runtime --
    > Time for graph definition: 2.563 seconds
    > Time for graph and analysis: 35.049 seconds

    ---- Test run number 1  ----
    -- rustworkx runtime --
    > Time for graph definition: 2.397 seconds
    > Time for graph and analysis: 49.235 seconds

    ---- Test run number 2  ----
    -- rustworkx runtime --
    > Time for graph definition: 2.406 seconds
    > Time for graph and analysis: 52.961 seconds

    ---- Test run number 3  ----
    -- rustworkx runtime --
    > Time for graph definition: 2.380 seconds
    > Time for graph and analysis: 47.069 seconds

    ---- Test run number 4  ----
    -- rustworkx runtime --
    > Time for graph definition: 2.143 seconds
    > Time for graph and analysis: 51.074 seconds


    ---- Test run number 0  ----
    -- NetworkX memory --
    > Peak memory for graph definition: 113,316,144 bytes
    Computed distance sum: 68061.0
    Computed vertex count of path: 23,611
    Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
    Computed distance sum: 68061.0
    > Total peak memory for graph and analysis: 9,584,256,016 bytes
    -- NetworkX runtime --
    > Time for graph definition: 0.321 seconds
    > Time for graph and analysis: 69.218 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.328 seconds
    > Time for graph and analysis: 73.155 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.343 seconds
    > Time for graph and analysis: 79.359 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.321 seconds
    > Time for graph and analysis: 79.219 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.319 seconds
    > Time for graph and analysis: 81.760 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.11 | ____________0 | ____16,171,992 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.09 | ____________0 | _____4,269,216 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.09 | ____________0 | _____4,269,168 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.10 | ____________0 | _____3,798,928 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.09 | ____________0 | _____2,330,368 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.10 | ____________0 | _____1,860,128 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __0.10 | ____________0 | _____1,860,128 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _0.09 | __0.11 | ____2,927,552 | _____2,927,552 |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx | _2.40 | _49.23 | ____4,698,364 | _____4,698,364 |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _0.32 | _79.22 | __113,316,144 | _9,584,256,016 |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Depth first search, 1M vertices, exhaustive search =====
    ---- Test run number 0  ----
    -- NoGraphs memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 207,510,148 bytes
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.784 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.787 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.777 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.814 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 3.788 seconds


    ---- Test run number 0  ----
    -- nog@IntId memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 144,766,134 bytes
    -- nog@IntId runtime --
    > Time for graph and analysis: 3.297 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 3.276 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 3.282 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 3.287 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 3.291 seconds


    ---- Test run number 0  ----
    -- @IntIdA0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 145,659,147 bytes
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 2.654 seconds

    ---- Test run number 1  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 2.653 seconds

    ---- Test run number 2  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 2.651 seconds

    ---- Test run number 3  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 2.650 seconds

    ---- Test run number 4  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 2.653 seconds


    ---- Test run number 0  ----
    -- @IntIdL0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 152,712,212 bytes
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.761 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.745 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.735 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.746 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 2.714 seconds


    ---- Test run number 0  ----
    -- @IntIdF memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 144,766,094 bytes
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.293 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.290 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.288 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.287 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 3.296 seconds


    ---- Test run number 0  ----
    -- @IntIdF0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 145,659,147 bytes
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 2.649 seconds

    ---- Test run number 1  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 2.639 seconds

    ---- Test run number 2  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 2.652 seconds

    ---- Test run number 3  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 2.647 seconds

    ---- Test run number 4  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 2.661 seconds


    ---- Test run number 0  ----
    -- nog@Int memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 14,770,914 bytes
    -- nog@Int runtime --
    > Time for graph and analysis: 3.279 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 3.290 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 3.289 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 3.290 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 3.290 seconds


    ---- Test run number 0  ----
    -- @IntF memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 14,770,914 bytes
    -- @IntF runtime --
    > Time for graph and analysis: 3.282 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.303 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.312 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.287 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 3.297 seconds


    ---- Test run number 0  ----
    -- @IntF0B memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 15,663,967 bytes
    -- @IntF0B runtime --
    > Time for graph and analysis: 2.634 seconds

    ---- Test run number 1  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 2.646 seconds

    ---- Test run number 2  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 2.648 seconds

    ---- Test run number 3  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 2.653 seconds

    ---- Test run number 4  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 2.660 seconds


    ---- Test run number 0  ----
    -- nog+intset memory --
    Computed #reachable: 999867
    > Total peak memory for graph and analysis: 14,776,752 bytes
    -- nog+intset runtime --
    > Time for graph and analysis: 2.347 seconds

    ---- Test run number 1  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.360 seconds

    ---- Test run number 2  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.390 seconds

    ---- Test run number 3  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.379 seconds

    ---- Test run number 4  ----
    -- nog+intset runtime --
    > Time for graph and analysis: 2.367 seconds






    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __3.79 | ____________0 | ___207,510,148 |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __3.29 | ____________0 | ___144,766,134 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B | _0.00 | __2.65 | ____________0 | ___145,659,147 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __2.75 | ____________0 | ___152,712,212 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __3.29 | ____________0 | ___144,766,094 |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B | _0.00 | __2.65 | ____________0 | ___145,659,147 |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __3.29 | ____________0 | ____14,770,914 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __3.30 | ____________0 | ____14,770,914 |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   | _0.00 | __2.65 | ____________0 | ____15,663,967 |
    +-----------+-------+--------+---------------+----------------+
    | nog+intset| _0.00 | __2.37 | ____________0 | ____14,776,752 |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | rustworkx |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


**The results for PyPy**

The following tables show the results of the tests.

``A. 1.`` Breadth first search, 1.20 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.19 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.10 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B | _0.00 | __0.09 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.17 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.10 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B | _0.00 | __0.09 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.12 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.12 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   | _0.00 | __0.12 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 30.36 | _36.35 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _2.43 | __2.91 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

``A. 2.`` Dijkstra distances, 1,2 M vertices, 3 goals:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.69 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.57 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.57 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.51 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.57 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.51 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 30.54 | _31.04 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _2.51 | __3.61 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

``B.`` Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.67 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.57 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.57 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.52 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.57 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.51 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift | _0.00 | __0.51 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    |258.05 | 259.10 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _7.86 | _10.21 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

``C.`` Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.04 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __1.73 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __1.73 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __1.50 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __1.72 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __1.51 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 29.91 | _31.38 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _2.54 | __5.52 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

``A. 3.`` Dijkstra path and distance, 1,2 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.84 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.68 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.68 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.63 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.61 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.53 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 29.82 | _30.36 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

``A. 4.`` Dijkstra path and distance, 100 T vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.07 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.05 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __0.05 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.05 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.05 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.04 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _0.48 | __0.52 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _0.24 | _61.93 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

Extra: Depth first search, 1 M vertices, random graph, exhaustive traverse

(So far, not part of the benchmark. Will be included in future versions.)

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.42 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@IntId | _0.00 | __0.91 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdA0B | _0.00 | __0.96 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdL0B | _0.00 | __1.46 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF   | _0.00 | __0.92 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntIdF0B | _0.00 | __0.95 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog@Int   | _0.00 | __0.85 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF     | _0.00 | __0.85 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| @IntF0B   | _0.00 | __0.88 |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+


The following text is the detailed output of the tests::

    Libraries: igraph, networkx
    Missing libraries: rustworkx, intbitset
    Python 3.9.16 (feeb267ead3e6771d3f2f49b83e1894839f64fb7, Dec 29 2022, 14:45:38)
    [PyPy 7.3.11 with MSC v.1929 64 bit (AMD64)]
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
    -- nog+shift --
    > Time for warmup 0.000 seconds
    -- igraph --
    > Time for warmup 0.001 seconds
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
    Dijkstra path and distance, 1,2 M vertices, 1 goal:
      vertices_count=1200002, min_vertex=0, max_vertex=1200006
    Dijkstra path and distance, 100 T vertices, 1 goal:
      vertices_count=100002, min_vertex=0, max_vertex=100008
    Depth first search, 1M vertices, exhaustive search:
      vertices_count=975509, min_vertex=0, max_vertex=999999

    ===== Test case: Breadth first search, 1.20 M vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.201 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.189 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.192 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.191 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.194 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.109 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.102 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.102 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.096 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.100 seconds


    ---- Test run number 0  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.100 seconds

    ---- Test run number 1  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.093 seconds

    ---- Test run number 2  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.093 seconds

    ---- Test run number 3  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.089 seconds

    ---- Test run number 4  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.089 seconds


    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.176 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.161 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.165 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.158 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.168 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.090 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.097 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.096 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.104 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.101 seconds


    ---- Test run number 0  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.095 seconds

    ---- Test run number 1  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.093 seconds

    ---- Test run number 2  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.094 seconds

    ---- Test run number 3  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.092 seconds

    ---- Test run number 4  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.094 seconds


    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.145 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.123 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.119 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.124 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.125 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.126 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.122 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.126 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.116 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.125 seconds


    ---- Test run number 0  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.125 seconds

    ---- Test run number 1  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.117 seconds

    ---- Test run number 2  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.114 seconds

    ---- Test run number 3  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.118 seconds

    ---- Test run number 4  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.114 seconds



    ---- Test run number 0  ----
    -- igraph runtime --
    > Time for graph definition: 30.362 seconds
    > Time for graph and analysis: 36.349 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 29.950 seconds
    > Time for graph and analysis: 35.939 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 30.666 seconds
    > Time for graph and analysis: 36.716 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 30.079 seconds
    > Time for graph and analysis: 36.081 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 30.813 seconds
    > Time for graph and analysis: 36.861 seconds


    ---- Test run number 0  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.909 seconds
    > Time for graph and analysis: 3.112 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.434 seconds
    > Time for graph and analysis: 2.903 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.424 seconds
    > Time for graph and analysis: 2.903 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.433 seconds
    > Time for graph and analysis: 2.923 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.424 seconds
    > Time for graph and analysis: 2.913 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.19 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.10 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B | _0.00 | __0.09 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.17 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.10 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B | _0.00 | __0.09 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.12 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.12 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   | _0.00 | __0.12 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 30.36 | _36.35 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _2.43 | __2.91 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.772 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.690 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.689 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.688 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.682 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.657 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.577 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.573 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.568 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.566 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.578 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.572 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.578 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.568 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.565 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.569 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.506 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.505 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.503 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.511 seconds



    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.568 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.569 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.568 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.566 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.570 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.512 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.510 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.504 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.506 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.505 seconds




    ---- Test run number 0  ----
    -- igraph runtime --
    > Time for graph definition: 31.284 seconds
    > Time for graph and analysis: 31.794 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 30.710 seconds
    > Time for graph and analysis: 31.222 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 30.542 seconds
    > Time for graph and analysis: 31.036 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 30.353 seconds
    > Time for graph and analysis: 30.860 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 30.297 seconds
    > Time for graph and analysis: 30.788 seconds


    ---- Test run number 0  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.647 seconds
    > Time for graph and analysis: 3.442 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.513 seconds
    > Time for graph and analysis: 3.619 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.500 seconds
    > Time for graph and analysis: 3.609 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.506 seconds
    > Time for graph and analysis: 3.599 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.559 seconds
    > Time for graph and analysis: 3.654 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.69 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.57 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.57 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.51 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.57 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.51 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 30.54 | _31.04 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _2.51 | __3.61 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.675 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.666 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.671 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.673 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.665 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.570 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.563 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.571 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.576 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.571 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.565 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.573 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.570 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.573 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.572 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.516 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.513 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.511 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.515 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.516 seconds



    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.573 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.567 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.571 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.570 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.573 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.512 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.513 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.516 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.514 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.517 seconds



    ---- Test run number 0  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 0.587 seconds

    ---- Test run number 1  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 0.511 seconds

    ---- Test run number 2  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 0.512 seconds

    ---- Test run number 3  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 0.525 seconds

    ---- Test run number 4  ----
    -- nog+shift runtime --
    > Time for graph and analysis: 0.510 seconds


    ---- Test run number 0  ----
    -- igraph runtime --
    > Time for graph definition: 259.421 seconds
    > Time for graph and analysis: 260.423 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 256.708 seconds
    > Time for graph and analysis: 257.729 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 258.051 seconds
    > Time for graph and analysis: 259.098 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 259.595 seconds
    > Time for graph and analysis: 260.650 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 257.241 seconds
    > Time for graph and analysis: 258.270 seconds


    ---- Test run number 0  ----
    -- NetworkX runtime --
    > Time for graph definition: 7.876 seconds
    > Time for graph and analysis: 10.565 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 7.828 seconds
    > Time for graph and analysis: 10.198 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 7.860 seconds
    > Time for graph and analysis: 10.214 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 7.877 seconds
    > Time for graph and analysis: 10.261 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 7.855 seconds
    > Time for graph and analysis: 10.186 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.67 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.57 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.57 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.52 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.57 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.51 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift | _0.00 | __0.51 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    |258.05 | 259.10 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _7.86 | _10.21 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.062 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.035 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.038 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.045 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 2.037 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.736 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.707 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.714 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.737 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 1.733 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.724 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.741 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.726 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.731 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.713 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.502 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.503 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.513 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.510 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 1.501 seconds



    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.713 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.724 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.723 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.715 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.730 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.504 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.502 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.514 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.529 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 1.506 seconds




    ---- Test run number 0  ----
    -- igraph runtime --
    > Time for graph definition: 29.683 seconds
    > Time for graph and analysis: 31.138 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 30.265 seconds
    > Time for graph and analysis: 31.722 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 30.299 seconds
    > Time for graph and analysis: 31.732 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 29.910 seconds
    > Time for graph and analysis: 31.375 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 29.773 seconds
    > Time for graph and analysis: 31.188 seconds


    ---- Test run number 0  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.786 seconds
    > Time for graph and analysis: 5.489 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.598 seconds
    > Time for graph and analysis: 5.592 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.527 seconds
    > Time for graph and analysis: 5.516 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.537 seconds
    > Time for graph and analysis: 5.551 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 2.535 seconds
    > Time for graph and analysis: 5.461 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __2.04 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __1.73 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __1.73 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __1.50 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __1.72 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __1.51 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 29.91 | _31.38 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _2.54 | __5.52 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra path and distance, 1,2 M vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.892 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.845 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.837 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.836 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.840 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.695 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.676 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.672 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.678 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.677 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.677 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.678 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.674 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.677 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.675 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.657 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.620 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.617 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.629 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.626 seconds



    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.637 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.607 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.607 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.607 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.601 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.561 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.531 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.533 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.533 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.539 seconds




    ---- Test run number 0  ----
    -- igraph runtime --
    > Time for graph definition: 29.750 seconds
    > Time for graph and analysis: 30.320 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 29.817 seconds
    > Time for graph and analysis: 30.363 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 29.608 seconds
    > Time for graph and analysis: 30.170 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 30.521 seconds
    > Time for graph and analysis: 31.072 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 29.825 seconds
    > Time for graph and analysis: 30.378 seconds



    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.84 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.68 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.68 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.63 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.61 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.53 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | 29.82 | _30.36 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Dijkstra path and distance, 100 T vertices, 1 goal =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.061 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.081 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.072 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.070 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 0.078 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.051 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.049 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.050 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.050 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.049 seconds



    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.051 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.050 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.048 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.050 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 0.051 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.047 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.048 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.047 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.047 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.046 seconds



    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.046 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.046 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.046 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.050 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.048 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.044 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.044 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.047 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.046 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.044 seconds




    ---- Test run number 0  ----
    -- igraph runtime --
    > Time for graph definition: 0.468 seconds
    > Time for graph and analysis: 0.532 seconds

    ---- Test run number 1  ----
    -- igraph runtime --
    > Time for graph definition: 0.485 seconds
    > Time for graph and analysis: 0.527 seconds

    ---- Test run number 2  ----
    -- igraph runtime --
    > Time for graph definition: 0.478 seconds
    > Time for graph and analysis: 0.521 seconds

    ---- Test run number 3  ----
    -- igraph runtime --
    > Time for graph definition: 0.476 seconds
    > Time for graph and analysis: 0.520 seconds

    ---- Test run number 4  ----
    -- igraph runtime --
    > Time for graph definition: 0.480 seconds
    > Time for graph and analysis: 0.523 seconds


    ---- Test run number 0  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.243 seconds
    > Time for graph and analysis: 49.113 seconds

    ---- Test run number 1  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.233 seconds
    > Time for graph and analysis: 59.957 seconds

    ---- Test run number 2  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.231 seconds
    > Time for graph and analysis: 62.810 seconds

    ---- Test run number 3  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.244 seconds
    > Time for graph and analysis: 66.114 seconds

    ---- Test run number 4  ----
    -- NetworkX runtime --
    > Time for graph definition: 0.241 seconds
    > Time for graph and analysis: 61.933 seconds


    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __0.07 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.05 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __0.05 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.05 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.05 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.04 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    | _0.48 | __0.52 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  | _0.24 | _61.93 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+


    ===== Test case: Depth first search, 1M vertices, exhaustive search =====
    ---- Test run number 0  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.507 seconds

    ---- Test run number 1  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.403 seconds

    ---- Test run number 2  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.419 seconds

    ---- Test run number 3  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.419 seconds

    ---- Test run number 4  ----
    -- NoGraphs runtime --
    > Time for graph and analysis: 1.407 seconds


    ---- Test run number 0  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.988 seconds

    ---- Test run number 1  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.910 seconds

    ---- Test run number 2  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.914 seconds

    ---- Test run number 3  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.905 seconds

    ---- Test run number 4  ----
    -- nog@IntId runtime --
    > Time for graph and analysis: 0.895 seconds


    ---- Test run number 0  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 1.032 seconds

    ---- Test run number 1  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.960 seconds

    ---- Test run number 2  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.956 seconds

    ---- Test run number 3  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.949 seconds

    ---- Test run number 4  ----
    -- @IntIdA0B runtime --
    > Time for graph and analysis: 0.939 seconds


    ---- Test run number 0  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.330 seconds

    ---- Test run number 1  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.459 seconds

    ---- Test run number 2  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.468 seconds

    ---- Test run number 3  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.455 seconds

    ---- Test run number 4  ----
    -- @IntIdL0B runtime --
    > Time for graph and analysis: 1.473 seconds


    ---- Test run number 0  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.929 seconds

    ---- Test run number 1  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.918 seconds

    ---- Test run number 2  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.908 seconds

    ---- Test run number 3  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.925 seconds

    ---- Test run number 4  ----
    -- @IntIdF runtime --
    > Time for graph and analysis: 0.919 seconds


    ---- Test run number 0  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.965 seconds

    ---- Test run number 1  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.955 seconds

    ---- Test run number 2  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.955 seconds

    ---- Test run number 3  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.953 seconds

    ---- Test run number 4  ----
    -- @IntIdF0B runtime --
    > Time for graph and analysis: 0.959 seconds


    ---- Test run number 0  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 1.054 seconds

    ---- Test run number 1  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.855 seconds

    ---- Test run number 2  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.844 seconds

    ---- Test run number 3  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.847 seconds

    ---- Test run number 4  ----
    -- nog@Int runtime --
    > Time for graph and analysis: 0.860 seconds


    ---- Test run number 0  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.856 seconds

    ---- Test run number 1  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.842 seconds

    ---- Test run number 2  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.845 seconds

    ---- Test run number 3  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.853 seconds

    ---- Test run number 4  ----
    -- @IntF runtime --
    > Time for graph and analysis: 0.854 seconds


    ---- Test run number 0  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 1.033 seconds

    ---- Test run number 1  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.877 seconds

    ---- Test run number 2  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.877 seconds

    ---- Test run number 3  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.880 seconds

    ---- Test run number 4  ----
    -- @IntF0B runtime --
    > Time for graph and analysis: 0.885 seconds





    +-----------+-------+--------+--------------------------------+
    | lib+gear  | runtime (sec.) |   peak memory (bytes)          |
    +-----------+-------+--------+---------------+----------------+
    |           | graph |  total |     graph     |     total      |
    +===========+=======+========+===============+================+
    | NoGraphs  | _0.00 | __1.42 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@IntId | _0.00 | __0.91 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdA0B | _0.00 | __0.96 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdL0B | _0.00 | __1.46 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF   | _0.00 | __0.92 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntIdF0B | _0.00 | __0.95 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog@Int   | _0.00 | __0.85 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF     | _0.00 | __0.85 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | @IntF0B   | _0.00 | __0.88 |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | nog+shift |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
    | NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
    +-----------+-------+--------+---------------+----------------+
