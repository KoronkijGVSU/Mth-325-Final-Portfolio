from collections import deque

def bfs_capacity(residual_graph, source, sink, parent):
    """
    Perform BFS to find an augmenting path in the residual graph.

    Args:
        residual_graph: The residual capacity graph.
        source: The source node.
        sink: The sink node.
        parent: List to store the path.

    Returns:
        bool: True if an augmenting path is found, False otherwise.
    """
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for next_node, capacity in enumerate(residual_graph[current_node]):
            if not visited[next_node] and capacity > 0:  # Positive capacity indicates a possible path
                queue.append(next_node)
                visited[next_node] = True
                parent[next_node] = current_node
                if next_node == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    """
    Implements the Ford-Fulkerson algorithm to find the maximum flow in a network.

    Args:
        graph (list of list): The adjacency matrix representing the capacities of the graph.
        source (int): The source node.
        sink (int): The sink node.

    Returns:
        int: The maximum flow from source to sink.
    """
    # Create a residual graph and initialize it with the capacities of the original graph
    residual_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)  # To store the path
    max_flow = 0

    step = 1

    # Augment the flow while there is an augmenting path
    while bfs_capacity(residual_graph, source, sink, parent):
        print(f"\n--- Augmenting Path Step {step} ---")

        # Trace back the path from sink to source to find the minimum capacity (path flow)
        path_flow = float('Inf')
        current_node = sink
        path = []  # To store the current augmenting path
        while current_node != source:
            path.insert(0, (parent[current_node], current_node))
            path_flow = min(path_flow, residual_graph[parent[current_node]][current_node])
            current_node = parent[current_node]

        # Print the augmenting path and its flow
        print(f"Augmenting Path: {path}")
        print(f"Path Flow: {path_flow}")

        # Update the residual graph capacities along the path
        current_node = sink
        while current_node != source:
            prev_node = parent[current_node]
            residual_graph[prev_node][current_node] -= path_flow
            residual_graph[current_node][prev_node] += path_flow
            current_node = parent[current_node]

        # Add path flow to the overall flow
        max_flow += path_flow
        print(f"Updated Max Flow: {max_flow}")

        # Print the updated residual graph
        print("Residual Graph:")
        for row in residual_graph:
            print(row)

        step += 1

    print("\n--- Final Result ---")
    print(f"Maximum Flow: {max_flow}")

    return max_flow


graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink = 5

ford_fulkerson(graph, source, sink)
