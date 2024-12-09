# Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices in a weighted graph
def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm to compute the shortest paths between all pairs of vertices in a graph.

    Parameters:
    graph: A 2D list (adjacency matrix) where graph[i][j] represents the weight of the edge from vertex i to vertex j.
           Use 'INF' (infinity) to represent no path between two vertices.

    Returns:
    dist: A 2D list (distance matrix) where dist[i][j] gives the shortest path from vertex i to vertex j.
    If a negative-weight cycle is detected, returns None and prints a message.
    """

    # Number of vertices in the graph
    n = len(graph)

    # Initialize the distance matrix as a copy of the graph matrix to preserve the original graph
    dist = [row[:] for row in graph]

    # Triple nested loop to consider each vertex as an intermediate point
    for k in range(n):  # Loop over all possible intermediate vertices
        for i in range(n):  # Loop over all source vertices
            for j in range(n):  # Loop over all destination vertices
                # Update the shortest distance if a shorter path is found through vertex k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative-weight cycles by examining the diagonal elements of the distance matrix
    for i in range(n):
        if dist[i][i] < 0:  # If any diagonal element is negative, a negative cycle exists
            print("Graph contains a negative-weight cycle")
            return None

    return dist  # Return the distance matrix with the shortest paths


# Example usage
# Define 'INF' as the weight representing no path between vertices
INF = float('inf')

# Define a graph with 4 vertices and some weighted edges (infinite weight for non-edges)
graph = [
    [0, 3, INF, 5],  # Distances from vertex 0 to others
    [2, 0, INF, 4],  # Distances from vertex 1 to others
    [INF, 1, 0, INF],  # Distances from vertex 2 to others
    [INF, INF, 2, 0]  # Distances from vertex 3 to others
]

# Call the Floyd-Warshall function and store the shortest path distances
distances = floyd_warshall(graph)

# Print the shortest path matrix if no negative-weight cycle is found
if distances:
    print("Shortest distances between every pair of vertices:")
    for row in distances:
        print(row)  # Print each row of the distance matrix, representing distances from a vertex to all others
