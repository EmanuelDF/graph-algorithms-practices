## Graph algorithms practices

Graphs have become a powerful means of modelling and capturing data in real-world scenarios such as social media
networks, web pages and links, and locations and routes in GPS.

Graph algorithm visualizer: https://graph-algorithms.io

### Breadth First Search (BFS)
Breadth First Search traverses the graph by first checking the current node and then expanding it by adding its
successors to the next level. The process is repeated for all nodes in the  current level before moving to the next
level. If the solution is found the search stops.
```
Space Complexity: O(n)
Worse Case Time Complexity: O(n)
```

### Depth First Search (DFS)
Depth First Search traverses the graph by first checking the current node and then moving to one of its successors to
repeat the process. If the current node has no successor to check, we move back to its predecessor and the process
continues (by moving to another successor). If the solution is found the search stops.
```
Space Complexity: O(n)
Worse Case Time Complexity: O(n) Depth First Search is complete on
a finite set of nodes. I works better on shallow trees.
```

### Floyd Warshall Algorithm (FWA)
The Floyd Warshall algorithm is a great algorithm for finding the shortest distance between all vertices in a graph.
It is a very concise algorithm and has O(V^3) time complexity (where V is number of vertices).
```
Space Complexity: O(V^2)
Worse Case Time Complexity: O(V^3)
```

References:
- https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph
- https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph
- https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16
- https://www.geeksforgeeks.org/minimum-cost-connect-cities
