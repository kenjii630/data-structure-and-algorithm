# take a graph as input and find the subset of the edges of that graph
# Construct the minimum spanning tree by using adjacency matrix.
# faster with sparse graphs (graphs with a low number of edges)
# Can also run on the disconnected graphs
# It follows the greedy approach that finds an optimum solution at every stage instead of focusing on a global optimum.

# we start from edges with the lowest weight and keep adding the edges until the goal is reached.

# Time complexity
    #   O(E log V)

# Data structure
    # disjoint set union
                            # Use Union concept#
# Uses "Union find" data structure to check whether any additional edge cause a cycle.
# The logic is to put all connected vertices into the set(union find concept)
# If the two vertices from a new edge do not belong to the same set, then it's safe to add that edge into the MST.

                            # The steps to implement Kruskal's algorithm are listed as follows:
# 1. Sort all the edges base on weight from low to high
# 2. Take the edge with the lowest weight and add it to the spanning tree.
# ( Spanning tree is subset of graph which all the vertices covered with the minimum possible number of edge ).
    # if adding the edge created a cycle, then reject this edge.
# 3. Keep adding edges until we reach all vertices, Repeat from step 2 until it includes n - 1 edges are added.

# sort edges form lowest to the highest
# if edge doesn't create cycle add to E
# continue until |v| = |E| + 1

                                        # The comparison #

# Dijkstra's - Here the goal is to reach from start to end.
# You are concerned about only this 2 points, and optimize your path accordingly.

# Kruskal's - Here you can start from any point and have to visit all other points in the graph.
# So, you may not always choose the shortest path for any two points.
# Instead, the focus is to choose the path that will lead you to a shorter path for all the other points.

# Prime's algorithm is another popular minimum spanning tree algorithm
# that uses a different logic to find the MST of a graph.
# Instead of starting from an edge, Prime's algorithm starts from a vertex
# and keeps adding lowest-weight edges which aren't in the tree, until all vertices have been covered.


# Pseudo code

# KRUSKAL(G):
# A = ∅
# For each vertex v ∈ G.V:
# MAKE-SET(v)
# For each edge (u, v) ∈ G.E ordered by increasing order by weight(u, v):
#   if FIND-SET(u) ≠ FIND-SET(v):
# A = A ∪ {(u, v)}
# UNION(u, v)
# return A

# A = ∅
# foreach v ∈ V:
# make-disjoint-set(v)
# sort E by weight increasingly
# foreach (v1, v2) ∈ E:
# if find(v1) opposite find(v2):
# A = A U {(v1,  v2)}
# Union(v1, v2)
# return A
