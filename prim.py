# Prime's will be faster in dense graphs (lots of edges).
# Get the full potential for Prime's alg, by use a Fibonacci heap.
# Using it you will have a runtime of O(E + V logV)
# only work on undirected graphs
# can handle negative edge weights
# better used when graph with many more edges than vertices.

# It's resembles Dijkstra

# it's efficiently implemented using "d-ary heap" and also can use Fibonacci heap
    # add the minimum weight edge for the chosen vertex which requires searching on the array of weights.
    # Prim’s algorithm can be made to run in linear time using d-ary heap(generalization of binary heap).

# It doesn't pre-sort all edges.Instead, it uses a "Priority Queue" to maintain a running sorted next-possible vertices.
    # Priority queue are useful for algorithms that need to process a number of items and where you repeatedly need to
        # identify which one is now the biggest or smallest
# Start from one vertex
# loop through all unvisited neighbours and enqueue a pair of values for each neighbour
# The vertex and the weight of edge connecting current vertex to the neighbour.
# Each time it select the top of the priority queue (the one with the least weight value)
# Add the edge into the final MST if the enqueued neighbour hasn't been already visited.

# 1. Create two sets U and V
# 2. Put the start value in U from which we have to make the spanning tree.
# 3. while U is not equal to V, find the lowest cost to reach the edges and put that over U.
# 4. Repeat step 3 for other edges until n-1 (where n is the number of vertices) an MST is achieved.

# https://techdifferences.com/difference-between-prims-and-kruskals-algorithm.html#Definition
