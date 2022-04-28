# Find the shortest path from a vertex to all others vertices
# Can work with graph which edges can have negative weights.

# Time complexity is O(VE)
# times the for loop in the Bellman Ford Algorithm gets executed (V-1)


# bellman ford returns Boolean value whether there is a negative weight cycle that is reachable from the source.

                                #Comparision#
# While Dijkstra looks only to the immediate neighbors of a vertex,
# Bellman goes through each edge in every iteration.

#function bellmanFord(G, S)
    #for each vertex V in G
    #distance[V] <- infinite
      #previous[V] <- NULL
  #distance[S] <- 0

  #for each vertex V in G
    #for each edge (U,V) in G
      #tempDistance <- distance[U] + edge_weight(U, V)
      #if tempDistance < distance[V]
        #distance[V] <- tempDistance
        #previous[V] <- U

  #for each edge (U,V) in G
    #If distance[U] + edge_weight(U, V) < distance[V}
      #Error: Negative Cycle Exists

  #return distance[], previous[]

# Python3 program for Bellman-Ford's single source
# the shortest path algorithm.

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(dist)


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
g.BellmanFord(3)

# Initially, Contributed by Neelam Yadav
# Later On, Edited by Himanshu Garg
