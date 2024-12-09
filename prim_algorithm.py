import heapq


def prim_algorithm(graph, start_node):
    """
    Implementation of Prim's algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

    Parameters:
    graph: A dictionary where the keys are nodes, and the values are dictionaries of neighboring nodes and edge weights.
           Example: {'A': {'B': 3, 'D': 1}, 'B': {'A': 3, 'D': 3, 'C': 1}, ...}
    start_node: The node from which to start building the MST.

    Returns:
    mst: A list of edges that form the minimum spanning tree. Each edge is represented as a tuple (node1, node2, weight).
    total_weight: The total weight of all edges in the MST.
    """

    # Priority queue to select the edge with the smallest weight
    pq = []  # Formatting is: (weight, start_node, end_node)

    # Set of nodes that have been added to the MST
    visited = set()

    # List to store the edges of the Minimum Spanning Tree (MST)
    mst = []

    # Total weight of all edges in the MST
    total_weight = 0

    # Initialize the priority queue with the starting node's edges
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(pq, (weight, start_node, neighbor))  # Add edges to the priority queue

    visited.add(start_node)  # Mark the start node as visited

    while pq:
        # Get the edge with the smallest weight
        weight, node1, node2 = heapq.heappop(pq)

        # If node2 has already been visited, we skip it to avoid cycles
        if node2 in visited:
            continue

        # Add this edge to the MST
        mst.append((node1, node2, weight))
        total_weight += weight  # Add the edge's weight to the total weight

        # Mark the new node as visited
        visited.add(node2)

        # For the newly added node, add all its edges to the priority queue if the other node isn't visited yet
        for neighbor, edge_weight in graph[node2].items():
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, node2, neighbor))

    return mst, total_weight


graph = {
    'A': {'B': 3, 'D': 1},
    'B': {'A': 3, 'D': 3, 'C': 1},
    'C': {'B': 1, 'D': 1, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 1, 'E': 6},
    'E': {'C': 5, 'D': 6}
}

mst, total_weight = prim_algorithm(graph, 'A')

# Output the resulting Minimum Spanning Tree and its total weight
print("Edges in the Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)

print(f"Total weight of the MST: {total_weight}")
