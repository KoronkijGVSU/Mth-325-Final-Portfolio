def color_graph_with_steps(graph, max_colors=4):
    """
    Colors a graph using at most max_colors while printing each step.

    Args:
        graph (dict): Adjacency list representing the graph.
                      Keys are nodes, and values are lists of adjacent nodes.
        max_colors (int): Maximum number of colors allowed.

    Returns:
        dict: A dictionary mapping each node to its assigned color.
    """
    # Initialize color assignments
    coloring = {node: None for node in graph}

    def is_safe(node, color):
        """Check if it's safe to assign `color` to `node`."""
        for neighbor in graph[node]:
            if coloring[neighbor] == color:
                return False
        return True

    def assign_color(node):
        """Attempt to assign a color to a node and log the process."""
        for color in range(1, max_colors + 1):
            print(f"  Trying color {color} for node {node}...")
            if is_safe(node, color):
                print(f"  Color {color} is safe for node {node}.")
                return color
            else:
                print(f" Color {color} is not safe for use in node {node}.")
        return None  # No valid color found

    # Assign colors to all nodes
    for node in graph:
        print(f"Processing node {node}...")
        color = assign_color(node)
        if color is None:
            raise ValueError(f"Graph cannot be colored with {max_colors} colors.")
        coloring[node] = color
        print(f"Assigned color {color} to node {node}. Current coloring: {coloring}\n")

    return coloring


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

print("Attempting to color the graph with 4 colors...\n")
try:
    coloring = color_graph_with_steps(graph, max_colors=4)
    print("\nSuccessfully colored the graph with 4 colors:")
    print(coloring)
except ValueError:
    print("\nFailed to color the graph with 4 colors. Trying with 5 colors...\n")
    coloring = color_graph_with_steps(graph, max_colors=5)
    print("\nSuccessfully colored the graph with 5 colors:")
    print(coloring)
