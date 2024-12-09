def find_eulerian_circuit(graph):
    """
    Finds an Eulerian circuit in a graph, if it exists.
    An Eulerian circuit is a cycle that visits every edge exactly once and returns to the starting node.

    Parameters:
    graph: A dictionary representing the graph as an adjacency list.
           Each key is a node, and the corresponding value is a list of neighbors (edges).

    Returns:
    A list representing the Eulerian circuit, if it exists.
    Raises a ValueError if the graph doesn't have an Eulerian circuit.
    """

    # Verify that the graph has an Eulerian circuit
    # For a graph to have an Eulerian circuit, all vertices must have an even degree
    for node in graph:
        if len(graph[node]) % 2 != 0:
            # If any node has an odd degree, raise an error
            raise ValueError("Graph doesn't have an Eulerian circuit: vertex {} has odd degree.".format(node))

    # Initialize a stack to help with the traversal and a list to store the Eulerian circuit
    stack = []
    circuit = []

    # Start from any node that has an edge (use the first node in the graph)
    start_node = next(iter(graph))  # `next(iter(graph))` gets the first node from the graph
    stack.append(start_node)  # Push the start node onto the stack

    # Traverse the graph using the stack, following edges to find the Eulerian circuit
    while stack:
        current = stack[-1]  # The current node is the one at the top of the stack

        # If the current node still has unused edges
        if graph[current]:
            # Pop the next node from the adjacency list of the current node
            next_node = graph[current].pop()
            # Remove the edge from the next node's adjacency list as well (undirected graph)
            graph[next_node].remove(current)
            # Push the next node onto the stack to continue the traversal
            stack.append(next_node)
        else:
            # If no unused edges, add the current node to the circuit (backtracking)
            circuit.append(stack.pop())  # Remove from the stack and add to the circuit

    # Reverse the circuit to get the correct order (since we backtracked)
    return circuit[::-1]


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Try to find the Eulerian circuit in the graph
try:
    eulerian_circuit = find_eulerian_circuit(graph)
    print("Eulerian Circuit:", eulerian_circuit)
except ValueError as e:
    print(e)
