A. 1. Breadth first search, 1.20 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.18 | ____________0 | ____71,951,182 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   | _0.00 | __1.16 | ____________0 | ____10,782,020 |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __1.34 | ____________0 | _____1,232,460 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit| _0.00 | __1.59 | ____________0 | _______161,460 |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __1.38 | ____________0 | _____1,232,108 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  | _0.00 | __1.64 | ____________0 | _______160,964 |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.97 | _14.63 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.64 | __2.57 | ___38,392,784 | ____86,348,224 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _8.38 | __9.90 | 1,297,009,024 | _1,359,923,608 |
+-----------+-------+--------+---------------+----------------+

A. 2. Dijkstra distances, 1,2 M vertices, 3 goals:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.32 | ____________0 | ____85,282,816 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __1.90 | ____________0 | _____9,617,764 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __2.17 | ____________0 | _____4,915,805 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.84 | _14.38 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.64 | __1.99 | ___38,392,976 | ____38,394,000 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _8.37 | _10.78 | 1,297,014,184 | _1,424,230,152 |
+-----------+-------+--------+---------------+----------------+

B. Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.31 | ____________0 | ____85,290,496 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __1.92 | ____________0 | ____19,482,508 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __2.26 | ____________0 | ____10,166,961 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    | _0.00 | __2.60 | ____________0 | _____4,915,565 |
+-----------+-------+--------+---------------+----------------+
| igraph    |110.45 | 111.08 | ___60,035,232 | ____60,035,232 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _4.85 | __5.60 | __115,192,784 | ___115,193,516 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

C. Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __6.91 | ____________0 | ____85,282,520 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __5.67 | ____________0 | _____9,616,860 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __6.99 | ____________0 | _____4,915,461 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 14.13 | _15.72 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.76 | __2.82 | ___38,392,976 | ____38,393,872 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

A. 3. Dijkstra path and distance, 100 T vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.23 | ____________0 | ____16,173,180 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __0.18 | ____________0 | _____4,269,928 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __0.21 | ____________0 | _____1,860,614 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _0.20 | __0.24 | ____2,927,552 | _____2,927,552 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _0.15 | _62.21 | ____3,193,040 | _____3,387,925 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _0.60 | _70.10 | __113,316,224 | _9,584,256,096 |
+-----------+-------+--------+---------------+----------------+

A. 4. Dijkstra path and distance, 1,2 M vertices, 1 goal:

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.67 | ____________0 | ___130,549,488 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __2.20 | ____________0 | ____49,352,856 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __2.52 | ____________0 | ____22,287,184 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 14.19 | _14.77 | ___21,590,880 | ____31,823,628 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+

Extra: Depth first search, 1 M vertices, exhaustive traverse

+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __7.67 | ____________0 | ___297,206,116 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   | _0.00 | __6.43 | ____________0 | ___243,124,864 |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __6.42 | ____________0 | ___236,071,719 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit| _0.00 | __7.23 | ____________0 | ___235,178,722 |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __6.56 | ____________0 | ____24,798,135 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  | _0.00 | __7.49 | ____________0 | ____23,905,082 |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+


"C:\Users\Anwender\SynologyDrive\Mit CAS\GitHubHome\nographs-and-others\venv\Scripts\python.exe" main.py
===== Warmup of libraries =====
-- NoGraphs --
> Time for warmup 0.000 seconds
-- +IntIdL --
> Time for warmup 0.000 seconds
-- +IntIdA --
> Time for warmup 0.000 seconds
-- +IntIdABit --
> Time for warmup 0.000 seconds
-- +Ints --
> Time for warmup 0.000 seconds
-- +IntsBit --
> Time for warmup 0.000 seconds
-- +Shift --
> Time for warmup 0.000 seconds
-- igraph --
> Time for warmup 0.850 seconds
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
> Total peak memory for graph and analysis: 71,951,182 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 1.198 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 1.199 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 1.174 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 1.175 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 1.177 seconds


---- Test run number 0  ----
-- +IntIdL memory --
Computed depth: 200000
> Total peak memory for graph and analysis: 10,782,020 bytes
-- +IntIdL runtime --
> Time for graph and analysis: 1.180 seconds

---- Test run number 1  ----
-- +IntIdL runtime --
> Time for graph and analysis: 1.157 seconds

---- Test run number 2  ----
-- +IntIdL runtime --
> Time for graph and analysis: 1.182 seconds

---- Test run number 3  ----
-- +IntIdL runtime --
> Time for graph and analysis: 1.164 seconds

---- Test run number 4  ----
-- +IntIdL runtime --
> Time for graph and analysis: 1.159 seconds


---- Test run number 0  ----
-- +IntIdA memory --
Computed depth: 200000
> Total peak memory for graph and analysis: 1,232,460 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 1.326 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.338 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.374 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.339 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.341 seconds


---- Test run number 0  ----
-- +IntIdABit memory --
Computed depth: 200000
> Total peak memory for graph and analysis: 161,460 bytes
-- +IntIdABit runtime --
> Time for graph and analysis: 1.594 seconds

---- Test run number 1  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 1.598 seconds

---- Test run number 2  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 1.591 seconds

---- Test run number 3  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 1.594 seconds

---- Test run number 4  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 1.613 seconds


---- Test run number 0  ----
-- +Ints memory --
Computed depth: 200000
> Total peak memory for graph and analysis: 1,232,108 bytes
-- +Ints runtime --
> Time for graph and analysis: 1.387 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 1.378 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 1.375 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 1.367 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 1.369 seconds


---- Test run number 0  ----
-- +IntsBit memory --
Computed depth: 200000
> Total peak memory for graph and analysis: 160,964 bytes
-- +IntsBit runtime --
> Time for graph and analysis: 1.637 seconds

---- Test run number 1  ----
-- +IntsBit runtime --
> Time for graph and analysis: 1.631 seconds

---- Test run number 2  ----
-- +IntsBit runtime --
> Time for graph and analysis: 1.638 seconds

---- Test run number 3  ----
-- +IntsBit runtime --
> Time for graph and analysis: 1.647 seconds

---- Test run number 4  ----
-- +IntsBit runtime --
> Time for graph and analysis: 1.643 seconds



---- Test run number 0  ----
-- igraph memory --
> Peak memory for graph definition: 21,590,880 bytes
Computed depth: 200000
> Total peak memory for graph and analysis: 21,590,880 bytes
-- igraph runtime --
> Time for graph definition: 13.958 seconds
> Time for graph and analysis: 14.625 seconds

---- Test run number 1  ----
-- igraph runtime --
> Time for graph definition: 13.956 seconds
> Time for graph and analysis: 14.620 seconds

---- Test run number 2  ----
-- igraph runtime --
> Time for graph definition: 13.970 seconds
> Time for graph and analysis: 14.633 seconds

---- Test run number 3  ----
-- igraph runtime --
> Time for graph definition: 14.572 seconds
> Time for graph and analysis: 15.232 seconds

---- Test run number 4  ----
-- igraph runtime --
> Time for graph definition: 13.967 seconds
> Time for graph and analysis: 14.626 seconds


---- Test run number 0  ----
-- RetworkX memory --
> Peak memory for graph definition: 38,392,784 bytes
Computed depth: 200000
> Total peak memory for graph and analysis: 86,348,224 bytes
-- RetworkX runtime --
> Time for graph definition: 1.644 seconds
> Time for graph and analysis: 2.578 seconds

---- Test run number 1  ----
-- RetworkX runtime --
> Time for graph definition: 1.647 seconds
> Time for graph and analysis: 2.573 seconds

---- Test run number 2  ----
-- RetworkX runtime --
> Time for graph definition: 1.642 seconds
> Time for graph and analysis: 2.572 seconds

---- Test run number 3  ----
-- RetworkX runtime --
> Time for graph definition: 1.642 seconds
> Time for graph and analysis: 2.572 seconds

---- Test run number 4  ----
-- RetworkX runtime --
> Time for graph definition: 1.652 seconds
> Time for graph and analysis: 2.584 seconds


---- Test run number 0  ----
-- NetworkX memory --
> Peak memory for graph definition: 1,297,009,024 bytes
Computed depth: 200000
> Total peak memory for graph and analysis: 1,359,923,608 bytes
-- NetworkX runtime --
> Time for graph definition: 8.381 seconds
> Time for graph and analysis: 9.905 seconds

---- Test run number 1  ----
-- NetworkX runtime --
> Time for graph definition: 8.309 seconds
> Time for graph and analysis: 9.838 seconds

---- Test run number 2  ----
-- NetworkX runtime --
> Time for graph definition: 8.425 seconds
> Time for graph and analysis: 9.991 seconds

---- Test run number 3  ----
-- NetworkX runtime --
> Time for graph definition: 8.570 seconds
> Time for graph and analysis: 10.161 seconds

---- Test run number 4  ----
-- NetworkX runtime --
> Time for graph definition: 8.372 seconds
> Time for graph and analysis: 9.900 seconds


+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __1.18 | ____________0 | ____71,951,182 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   | _0.00 | __1.16 | ____________0 | ____10,782,020 |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __1.34 | ____________0 | _____1,232,460 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit| _0.00 | __1.59 | ____________0 | _______161,460 |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __1.38 | ____________0 | _____1,232,108 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  | _0.00 | __1.64 | ____________0 | _______160,964 |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.97 | _14.63 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.64 | __2.57 | ___38,392,784 | ____86,348,224 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _8.38 | __9.90 | 1,297,009,024 | _1,359,923,608 |
+-----------+-------+--------+---------------+----------------+


===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals =====
---- Test run number 0  ----
-- NoGraphs memory --
Computed distance sum: 2279877.0
> Total peak memory for graph and analysis: 85,282,816 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 2.324 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.319 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.313 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.314 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.320 seconds



---- Test run number 0  ----
-- +IntIdA memory --
Computed distance sum: 2279877.0
> Total peak memory for graph and analysis: 9,617,764 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 1.900 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.904 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.901 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.977 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 2.039 seconds



---- Test run number 0  ----
-- +Ints memory --
Computed distance sum: 2279877.0
> Total peak memory for graph and analysis: 4,915,805 bytes
-- +Ints runtime --
> Time for graph and analysis: 2.173 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 2.163 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 2.166 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 2.164 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 2.171 seconds




---- Test run number 0  ----
-- igraph memory --
> Peak memory for graph definition: 21,590,880 bytes
Computed distance sum: 2279877.0
> Total peak memory for graph and analysis: 21,590,880 bytes
-- igraph runtime --
> Time for graph definition: 13.842 seconds
> Time for graph and analysis: 14.364 seconds

---- Test run number 1  ----
-- igraph runtime --
> Time for graph definition: 13.836 seconds
> Time for graph and analysis: 14.371 seconds

---- Test run number 2  ----
-- igraph runtime --
> Time for graph definition: 13.866 seconds
> Time for graph and analysis: 14.386 seconds

---- Test run number 3  ----
-- igraph runtime --
> Time for graph definition: 13.829 seconds
> Time for graph and analysis: 14.375 seconds

---- Test run number 4  ----
-- igraph runtime --
> Time for graph definition: 13.847 seconds
> Time for graph and analysis: 14.386 seconds


---- Test run number 0  ----
-- RetworkX memory --
> Peak memory for graph definition: 38,392,976 bytes
Computed distance sum: 2279877.0
> Total peak memory for graph and analysis: 38,394,000 bytes
-- RetworkX runtime --
> Time for graph definition: 1.648 seconds
> Time for graph and analysis: 2.000 seconds

---- Test run number 1  ----
-- RetworkX runtime --
> Time for graph definition: 1.643 seconds
> Time for graph and analysis: 1.990 seconds

---- Test run number 2  ----
-- RetworkX runtime --
> Time for graph definition: 1.642 seconds
> Time for graph and analysis: 1.986 seconds

---- Test run number 3  ----
-- RetworkX runtime --
> Time for graph definition: 1.646 seconds
> Time for graph and analysis: 1.996 seconds

---- Test run number 4  ----
-- RetworkX runtime --
> Time for graph definition: 1.642 seconds
> Time for graph and analysis: 1.983 seconds


---- Test run number 0  ----
-- NetworkX memory --
> Peak memory for graph definition: 1,297,014,184 bytes
Computed distance sum: 2279877.0
> Total peak memory for graph and analysis: 1,424,230,152 bytes
-- NetworkX runtime --
> Time for graph definition: 8.435 seconds
> Time for graph and analysis: 10.861 seconds

---- Test run number 1  ----
-- NetworkX runtime --
> Time for graph definition: 8.360 seconds
> Time for graph and analysis: 10.781 seconds

---- Test run number 2  ----
-- NetworkX runtime --
> Time for graph definition: 8.509 seconds
> Time for graph and analysis: 10.974 seconds

---- Test run number 3  ----
-- NetworkX runtime --
> Time for graph definition: 8.371 seconds
> Time for graph and analysis: 10.775 seconds

---- Test run number 4  ----
-- NetworkX runtime --
> Time for graph definition: 8.361 seconds
> Time for graph and analysis: 10.760 seconds


+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.32 | ____________0 | ____85,282,816 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __1.90 | ____________0 | _____9,617,764 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __2.17 | ____________0 | _____4,915,805 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 13.84 | _14.38 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.64 | __1.99 | ___38,392,976 | ____38,394,000 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _8.37 | _10.78 | 1,297,014,184 | _1,424,230,152 |
+-----------+-------+--------+---------------+----------------+


===== Test case: Dijkstra distances, 3,6 M vertices, 1 goal, 1/3 regarded =====
---- Test run number 0  ----
-- NoGraphs memory --
Computed distance sum: 816670.0
> Total peak memory for graph and analysis: 85,290,496 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 2.308 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.312 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.323 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.305 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.309 seconds



---- Test run number 0  ----
-- +IntIdA memory --
Computed distance sum: 816670.0
> Total peak memory for graph and analysis: 19,482,508 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 1.919 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.920 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.924 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.922 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 1.931 seconds



---- Test run number 0  ----
-- +Ints memory --
Computed distance sum: 816670.0
> Total peak memory for graph and analysis: 10,166,961 bytes
-- +Ints runtime --
> Time for graph and analysis: 2.259 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 2.271 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 2.261 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 2.261 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 2.267 seconds



---- Test run number 0  ----
-- +Shift memory --
Computed distance sum: 816670.0
> Total peak memory for graph and analysis: 4,915,565 bytes
-- +Shift runtime --
> Time for graph and analysis: 2.595 seconds

---- Test run number 1  ----
-- +Shift runtime --
> Time for graph and analysis: 2.600 seconds

---- Test run number 2  ----
-- +Shift runtime --
> Time for graph and analysis: 2.595 seconds

---- Test run number 3  ----
-- +Shift runtime --
> Time for graph and analysis: 2.595 seconds

---- Test run number 4  ----
-- +Shift runtime --
> Time for graph and analysis: 2.585 seconds


---- Test run number 0  ----
-- igraph memory --
> Peak memory for graph definition: 60,035,232 bytes
Computed distance sum: 816670.0
> Total peak memory for graph and analysis: 60,035,232 bytes
-- igraph runtime --
> Time for graph definition: 111.376 seconds
> Time for graph and analysis: 112.027 seconds

---- Test run number 1  ----
-- igraph runtime --
> Time for graph definition: 110.397 seconds
> Time for graph and analysis: 111.014 seconds

---- Test run number 2  ----
-- igraph runtime --
> Time for graph definition: 110.270 seconds
> Time for graph and analysis: 110.906 seconds

---- Test run number 3  ----
-- igraph runtime --
> Time for graph definition: 110.450 seconds
> Time for graph and analysis: 111.084 seconds

---- Test run number 4  ----
-- igraph runtime --
> Time for graph definition: 111.124 seconds
> Time for graph and analysis: 111.743 seconds


---- Test run number 0  ----
-- RetworkX memory --
> Peak memory for graph definition: 115,192,784 bytes
Computed distance sum: 816670.0
> Total peak memory for graph and analysis: 115,193,516 bytes
-- RetworkX runtime --
> Time for graph definition: 4.859 seconds
> Time for graph and analysis: 5.630 seconds

---- Test run number 1  ----
-- RetworkX runtime --
> Time for graph definition: 4.829 seconds
> Time for graph and analysis: 5.587 seconds

---- Test run number 2  ----
-- RetworkX runtime --
> Time for graph definition: 4.811 seconds
> Time for graph and analysis: 5.567 seconds

---- Test run number 3  ----
-- RetworkX runtime --
> Time for graph definition: 4.849 seconds
> Time for graph and analysis: 5.604 seconds

---- Test run number 4  ----
-- RetworkX runtime --
> Time for graph definition: 4.850 seconds
> Time for graph and analysis: 5.601 seconds



+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.31 | ____________0 | ____85,290,496 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __1.92 | ____________0 | ____19,482,508 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __2.26 | ____________0 | ____10,166,961 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    | _0.00 | __2.60 | ____________0 | _____4,915,565 |
+-----------+-------+--------+---------------+----------------+
| igraph    |110.45 | 111.08 | ___60,035,232 | ____60,035,232 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _4.85 | __5.60 | __115,192,784 | ___115,193,516 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+


===== Test case: Dijkstra distances, 1,2 M vertices, 3 goals, executed 3 times =====
---- Test run number 0  ----
-- NoGraphs memory --
Computed distance sums: 2279877.0 2279877.0 2279877.0
> Total peak memory for graph and analysis: 85,282,520 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 6.910 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 6.917 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 6.911 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 6.914 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 6.908 seconds



---- Test run number 0  ----
-- +IntIdA memory --
Computed distance sums: 2279877.0 2279877.0 2279877.0
> Total peak memory for graph and analysis: 9,616,860 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 5.664 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 5.669 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 5.671 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 5.727 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 5.666 seconds



---- Test run number 0  ----
-- +Ints memory --
Computed distance sums: 2279877.0 2279877.0 2279877.0
> Total peak memory for graph and analysis: 4,915,461 bytes
-- +Ints runtime --
> Time for graph and analysis: 7.001 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 6.998 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 6.989 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 6.976 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 6.990 seconds




---- Test run number 0  ----
-- igraph memory --
> Peak memory for graph definition: 21,590,880 bytes
Computed distance sums: 2279877.0 2279877.0 2279877.0
> Total peak memory for graph and analysis: 21,590,880 bytes
-- igraph runtime --
> Time for graph definition: 14.130 seconds
> Time for graph and analysis: 15.751 seconds

---- Test run number 1  ----
-- igraph runtime --
> Time for graph definition: 14.128 seconds
> Time for graph and analysis: 15.725 seconds

---- Test run number 2  ----
-- igraph runtime --
> Time for graph definition: 14.143 seconds
> Time for graph and analysis: 15.729 seconds

---- Test run number 3  ----
-- igraph runtime --
> Time for graph definition: 14.132 seconds
> Time for graph and analysis: 15.694 seconds

---- Test run number 4  ----
-- igraph runtime --
> Time for graph definition: 14.057 seconds
> Time for graph and analysis: 15.634 seconds


---- Test run number 0  ----
-- RetworkX memory --
> Peak memory for graph definition: 38,392,976 bytes
Computed distance sums: 2279877.0 2279877.0 2279877.0
> Total peak memory for graph and analysis: 38,393,872 bytes
-- RetworkX runtime --
> Time for graph definition: 1.761 seconds
> Time for graph and analysis: 2.819 seconds

---- Test run number 1  ----
-- RetworkX runtime --
> Time for graph definition: 1.759 seconds
> Time for graph and analysis: 2.820 seconds

---- Test run number 2  ----
-- RetworkX runtime --
> Time for graph definition: 1.756 seconds
> Time for graph and analysis: 2.823 seconds

---- Test run number 3  ----
-- RetworkX runtime --
> Time for graph definition: 1.750 seconds
> Time for graph and analysis: 2.807 seconds

---- Test run number 4  ----
-- RetworkX runtime --
> Time for graph definition: 1.765 seconds
> Time for graph and analysis: 2.819 seconds



+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __6.91 | ____________0 | ____85,282,520 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __5.67 | ____________0 | _____9,616,860 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __6.99 | ____________0 | _____4,915,461 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 14.13 | _15.72 | ___21,590,880 | ____21,590,880 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _1.76 | __2.82 | ___38,392,976 | ____38,393,872 |
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
> Total peak memory for graph and analysis: 16,173,180 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 0.228 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 0.224 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 0.237 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 0.225 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 0.223 seconds



---- Test run number 0  ----
-- +IntIdA memory --
Computed distance sum: 68061.0
Computed vertex count of path: 23,611
Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
Computed distance sum: 68061.0
> Total peak memory for graph and analysis: 4,269,928 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 0.179 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 0.178 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 0.176 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 0.178 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 0.180 seconds



---- Test run number 0  ----
-- +Ints memory --
Computed distance sum: 68061.0
Computed vertex count of path: 23,611
Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
Computed distance sum: 68061.0
> Total peak memory for graph and analysis: 1,860,614 bytes
-- +Ints runtime --
> Time for graph and analysis: 0.206 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 0.206 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 0.210 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 0.205 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 0.205 seconds




---- Test run number 0  ----
-- igraph memory --
> Peak memory for graph definition: 2,927,552 bytes
Computed distance sum: -1.0
Computed vertex count of path: 23,611
Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
Distance not computed
> Total peak memory for graph and analysis: 2,927,552 bytes
-- igraph runtime --
> Time for graph definition: 0.200 seconds
> Time for graph and analysis: 0.244 seconds

---- Test run number 1  ----
-- igraph runtime --
> Time for graph definition: 0.196 seconds
> Time for graph and analysis: 0.240 seconds

---- Test run number 2  ----
-- igraph runtime --
> Time for graph definition: 0.194 seconds
> Time for graph and analysis: 0.238 seconds

---- Test run number 3  ----
-- igraph runtime --
> Time for graph definition: 0.198 seconds
> Time for graph and analysis: 0.242 seconds

---- Test run number 4  ----
-- igraph runtime --
> Time for graph definition: 0.202 seconds
> Time for graph and analysis: 0.247 seconds


---- Test run number 0  ----
-- RetworkX memory --
> Peak memory for graph definition: 3,193,040 bytes
Computed distance sum: -1.0
Computed vertex count of path: 23,611
Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
Distance not computed
> Total peak memory for graph and analysis: 3,387,925 bytes
-- RetworkX runtime --
> Time for graph definition: 0.147 seconds
> Time for graph and analysis: 44.956 seconds

---- Test run number 1  ----
-- RetworkX runtime --
> Time for graph definition: 0.150 seconds
> Time for graph and analysis: 62.206 seconds

---- Test run number 2  ----
-- RetworkX runtime --
> Time for graph definition: 0.150 seconds
> Time for graph and analysis: 61.256 seconds

---- Test run number 3  ----
-- RetworkX runtime --
> Time for graph definition: 0.151 seconds
> Time for graph and analysis: 67.976 seconds

---- Test run number 4  ----
-- RetworkX runtime --
> Time for graph definition: 0.149 seconds
> Time for graph and analysis: 62.928 seconds


---- Test run number 0  ----
-- NetworkX memory --
> Peak memory for graph definition: 113,316,224 bytes
Computed distance sum: 68061.0
Computed vertex count of path: 23,611
Start and end of found path: (0, 1, 2, 8, 14) ... (99976, 99982, 99988, 99994)
Computed distance sum: 68061.0
> Total peak memory for graph and analysis: 9,584,256,096 bytes
-- NetworkX runtime --
> Time for graph definition: 0.590 seconds
> Time for graph and analysis: 70.096 seconds

---- Test run number 1  ----
-- NetworkX runtime --
> Time for graph definition: 0.593 seconds
> Time for graph and analysis: 65.547 seconds

---- Test run number 2  ----
-- NetworkX runtime --
> Time for graph definition: 0.605 seconds
> Time for graph and analysis: 69.960 seconds

---- Test run number 3  ----
-- NetworkX runtime --
> Time for graph definition: 0.601 seconds
> Time for graph and analysis: 70.660 seconds

---- Test run number 4  ----
-- NetworkX runtime --
> Time for graph definition: 0.646 seconds
> Time for graph and analysis: 97.890 seconds


+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __0.23 | ____________0 | ____16,173,180 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __0.18 | ____________0 | _____4,269,928 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __0.21 | ____________0 | _____1,860,614 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | _0.20 | __0.24 | ____2,927,552 | _____2,927,552 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  | _0.15 | _62.21 | ____3,193,040 | _____3,387,925 |
+-----------+-------+--------+---------------+----------------+
| NetworkX  | _0.60 | _70.10 | __113,316,224 | _9,584,256,096 |
+-----------+-------+--------+---------------+----------------+


===== Test case: Dijkstra path and distance, 1,2 M vertices, 1 goal =====
---- Test run number 0  ----
-- NoGraphs memory --
Computed distance sum: 816674.0
Computed vertex count of path: 283,331
Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
Computed distance sum: 816674.0
> Total peak memory for graph and analysis: 130,549,488 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 2.651 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.660 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.680 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.667 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 2.680 seconds



---- Test run number 0  ----
-- +IntIdA memory --
Computed distance sum: 816674.0
Computed vertex count of path: 283,331
Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
Computed distance sum: 816674.0
> Total peak memory for graph and analysis: 49,352,856 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 2.201 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 2.203 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 2.203 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 2.195 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 2.188 seconds



---- Test run number 0  ----
-- +Ints memory --
Computed distance sum: 816674.0
Computed vertex count of path: 283,331
Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
Computed distance sum: 816674.0
> Total peak memory for graph and analysis: 22,287,184 bytes
-- +Ints runtime --
> Time for graph and analysis: 2.516 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 2.524 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 2.517 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 2.538 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 2.525 seconds




---- Test run number 0  ----
-- igraph memory --
> Peak memory for graph definition: 21,590,880 bytes
Computed distance sum: -1.0
Computed vertex count of path: 283,331
Start and end of found path: (0, 1, 2, 8, 14) ... (1199976, 1199982, 1199988, 1199994, 1200000)
Distance not computed
> Total peak memory for graph and analysis: 31,823,628 bytes
-- igraph runtime --
> Time for graph definition: 14.237 seconds
> Time for graph and analysis: 14.814 seconds

---- Test run number 1  ----
-- igraph runtime --
> Time for graph definition: 14.235 seconds
> Time for graph and analysis: 14.809 seconds

---- Test run number 2  ----
-- igraph runtime --
> Time for graph definition: 14.130 seconds
> Time for graph and analysis: 14.717 seconds

---- Test run number 3  ----
-- igraph runtime --
> Time for graph definition: 14.190 seconds
> Time for graph and analysis: 14.765 seconds

---- Test run number 4  ----
-- igraph runtime --
> Time for graph definition: 14.143 seconds
> Time for graph and analysis: 14.724 seconds




+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __2.67 | ____________0 | ___130,549,488 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __2.20 | ____________0 | ____49,352,856 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit|  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __2.52 | ____________0 | ____22,287,184 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    | 14.19 | _14.77 | ___21,590,880 | ____31,823,628 |
+-----------+-------+--------+---------------+----------------+
| RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+


===== Test case: Depth first search, 1M vertices, exhaustive search =====
---- Test run number 0  ----
-- NoGraphs memory --
Computed #reachable: 999867
> Total peak memory for graph and analysis: 297,206,116 bytes
-- NoGraphs runtime --
> Time for graph and analysis: 7.634 seconds

---- Test run number 1  ----
-- NoGraphs runtime --
> Time for graph and analysis: 7.621 seconds

---- Test run number 2  ----
-- NoGraphs runtime --
> Time for graph and analysis: 7.672 seconds

---- Test run number 3  ----
-- NoGraphs runtime --
> Time for graph and analysis: 7.676 seconds

---- Test run number 4  ----
-- NoGraphs runtime --
> Time for graph and analysis: 7.679 seconds


---- Test run number 0  ----
-- +IntIdL memory --
Computed #reachable: 999867
> Total peak memory for graph and analysis: 243,124,864 bytes
-- +IntIdL runtime --
> Time for graph and analysis: 6.447 seconds

---- Test run number 1  ----
-- +IntIdL runtime --
> Time for graph and analysis: 6.423 seconds

---- Test run number 2  ----
-- +IntIdL runtime --
> Time for graph and analysis: 6.449 seconds

---- Test run number 3  ----
-- +IntIdL runtime --
> Time for graph and analysis: 6.435 seconds

---- Test run number 4  ----
-- +IntIdL runtime --
> Time for graph and analysis: 6.432 seconds


---- Test run number 0  ----
-- +IntIdA memory --
Computed #reachable: 999867
> Total peak memory for graph and analysis: 236,071,719 bytes
-- +IntIdA runtime --
> Time for graph and analysis: 6.417 seconds

---- Test run number 1  ----
-- +IntIdA runtime --
> Time for graph and analysis: 6.413 seconds

---- Test run number 2  ----
-- +IntIdA runtime --
> Time for graph and analysis: 6.437 seconds

---- Test run number 3  ----
-- +IntIdA runtime --
> Time for graph and analysis: 6.416 seconds

---- Test run number 4  ----
-- +IntIdA runtime --
> Time for graph and analysis: 6.444 seconds


---- Test run number 0  ----
-- +IntIdABit memory --
Computed #reachable: 999867
> Total peak memory for graph and analysis: 235,178,722 bytes
-- +IntIdABit runtime --
> Time for graph and analysis: 7.214 seconds

---- Test run number 1  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 7.228 seconds

---- Test run number 2  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 7.228 seconds

---- Test run number 3  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 7.238 seconds

---- Test run number 4  ----
-- +IntIdABit runtime --
> Time for graph and analysis: 7.209 seconds


---- Test run number 0  ----
-- +Ints memory --
Computed #reachable: 999867
> Total peak memory for graph and analysis: 24,798,135 bytes
-- +Ints runtime --
> Time for graph and analysis: 6.557 seconds

---- Test run number 1  ----
-- +Ints runtime --
> Time for graph and analysis: 6.540 seconds

---- Test run number 2  ----
-- +Ints runtime --
> Time for graph and analysis: 6.549 seconds

---- Test run number 3  ----
-- +Ints runtime --
> Time for graph and analysis: 6.561 seconds

---- Test run number 4  ----
-- +Ints runtime --
> Time for graph and analysis: 6.566 seconds


---- Test run number 0  ----
-- +IntsBit memory --
Computed #reachable: 999867
> Total peak memory for graph and analysis: 23,905,082 bytes
-- +IntsBit runtime --
> Time for graph and analysis: 7.487 seconds

---- Test run number 1  ----
-- +IntsBit runtime --
> Time for graph and analysis: 7.495 seconds

---- Test run number 2  ----
-- +IntsBit runtime --
> Time for graph and analysis: 7.465 seconds

---- Test run number 3  ----
-- +IntsBit runtime --
> Time for graph and analysis: 7.488 seconds

---- Test run number 4  ----
-- +IntsBit runtime --
> Time for graph and analysis: 7.483 seconds






+-----------+-------+--------+--------------------------------+
| lib+gear  | runtime (sec.) |   peak memory (bytes)          |
+-----------+-------+--------+---------------+----------------+
|           | graph |  total |     graph     |     total      |
+===========+=======+========+===============+================+
| NoGraphs  | _0.00 | __7.67 | ____________0 | ___297,206,116 |
+-----------+-------+--------+---------------+----------------+
| +IntIdL   | _0.00 | __6.43 | ____________0 | ___243,124,864 |
+-----------+-------+--------+---------------+----------------+
| +IntIdA   | _0.00 | __6.42 | ____________0 | ___236,071,719 |
+-----------+-------+--------+---------------+----------------+
| +IntIdABit| _0.00 | __7.23 | ____________0 | ___235,178,722 |
+-----------+-------+--------+---------------+----------------+
| +Ints     | _0.00 | __6.56 | ____________0 | ____24,798,135 |
+-----------+-------+--------+---------------+----------------+
| +IntsBit  | _0.00 | __7.49 | ____________0 | ____23,905,082 |
+-----------+-------+--------+---------------+----------------+
| +Shift    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| igraph    |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| RetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+
| NetworkX  |  n.a. |   n.a. |          n.a. |           n.a. |
+-----------+-------+--------+---------------+----------------+



Process finished with exit code 0
