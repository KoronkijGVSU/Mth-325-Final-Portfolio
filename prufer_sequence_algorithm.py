import heapq


def generate_prufer_sequence(tree):
    """
    Generate the Prüfer sequence from a given tree.

    Parameters:
    tree: A dictionary representing the tree as an adjacency list, where the keys are vertices and
          the values are lists of neighboring vertices.

    Returns:
    prufer_sequence: A list containing the Prüfer sequence for the input tree.
    """

    # Initialize the degree of each vertex by counting the number of neighbors in the tree
    degree = {vertex: len(neighbors) for vertex, neighbors in tree.items()}

    # Initialize a priority queue to always pick the smallest leaf
    leaf_queue = []

    # Add all leaves (vertices with degree 1) to the priority queue (min-heap)
    for vertex, deg in degree.items():
        if deg == 1:
            heapq.heappush(leaf_queue, vertex)

    # List to store the Prüfer sequence
    prufer_sequence = []

    # Perform the algorithm until we are left with two vertices
    while len(prufer_sequence) < len(tree) - 2:
        # Remove the smallest leaf from the heap
        leaf = heapq.heappop(leaf_queue)

        # Find the leaf's only neighbor
        for neighbor in tree[leaf]:
            if degree[neighbor] > 0:  # Ensure the neighbor hasn't been removed already
                prufer_sequence.append(neighbor)  # Append the neighbor to the Prüfer sequence

                # Remove the edge by removing the leaf from the neighbor's list
                tree[neighbor].remove(leaf)
                degree[neighbor] -= 1  # Decrease the degree of the neighbor

                # If the neighbor has become a leaf, add it to the heap
                if degree[neighbor] == 1:
                    heapq.heappush(leaf_queue, neighbor)

                break  # Once the edge is processed, no need to continue checking other neighbors

        # Mark the leaf as removed
        degree[leaf] = 0

    return prufer_sequence  # Return the generated Prüfer sequence


tree = {
    1: [2, 3],  # Vertex 1 is connected to vertices 2 and 3
    2: [1, 4],}  # Vertex 2 is connected to vertices
