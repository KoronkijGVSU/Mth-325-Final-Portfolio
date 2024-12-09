class UnionFind:
    """
    A class to represent the Union-Find data structure.
    It supports the union and find operations with path compression and union by rank.
    """

    def __init__(self, nodes):
        # Initialize the parent and rank dictionaries
        self.parent = {node: node for node in nodes}  # Initially, each node is its own parent
        self.rank = {node: 0 for node in nodes}  # Initially, each node has rank 0

    def find(self, node):
        """
        Find the root of the set containing the node.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        """
        Unite the sets containing node1 and node2.
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by rank: attach the smaller tree under the larger tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1  # Increase rank if they were the same height


def kruskal_algorithm(graph):
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree of a weighted, undirected graph.

    Parameters:
    graph: A dictionary where the keys are nodes, and the values are dictionaries of neighboring nodes and edge weights.
           Example: {'A': {'B': 3, 'D': 1}, 'B': {'A': 3, 'D': 3, 'C': 1}, ...}

    Returns:
    mst: A list of edges that form the minimum spanning tree. Each edge is represented as a tuple (node1, node2, weight).
    total_weight: The total weight of all edges in the MST.
    """

    # Create a list of all edges in the graph, where each edge is represented as a tuple (weight, node1, node2)
    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            if (neighbor, node, weight) not in edges:  # Avoid duplicating edges since the graph is undirected
                edges.append((weight, node, neighbor))

    # Sort all edges in non-decreasing order of their weight
    edges.sort()

    # Initialize the Union-Find data structure
    nodes = list(graph.keys())  # Get all the nodes in the graph
    uf = UnionFind(nodes)

    # List to store the edges in the Minimum Spanning Tree
    mst = []

    # Total weight of the MST
    total_weight = 0

    # Process each edge in the sorted list
    for weight, node1, node2 in edges:
        # Check if the current edge forms a cycle
        if uf.find(node1) != uf.find(node2):
            # If no cycle is formed, add this edge to the MST
            mst.append((node1, node2, weight))
            total_weight += weight

            # Union the sets containing node1 and node2
            uf.union(node1, node2)

    return mst, total_weight


graph = {
    'A': {'B': 3, 'D': 1},
    'B': {'A': 3, 'D': 3, 'C': 1},
    'C': {'B': 1, 'D': 1, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 1, 'E': 6},
    'E': {'C': 5, 'D': 6}
}

mst, total_weight = kruskal_algorithm(graph)

print("Edges in the Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)

print(f"Total weight of the MST: {total_weight}")
