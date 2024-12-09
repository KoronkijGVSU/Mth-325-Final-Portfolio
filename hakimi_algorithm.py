def hakimi_havel(degree_sequence):
    """
    Implementation the Hakimi-Havel algorithm to check if a given degree sequence
    can form a simple undirected graph.

    Parameters:
    degree_sequence: A list of non-negative integers representing the degree sequence.

    Returns:
    True if the sequence is graphical (can form a simple graph), False otherwise.
    """

    # Remove all zeros from the sequence (since nodes with degree 0 are already handled)
    degree_sequence = [deg for deg in degree_sequence if deg > 0]

    # Sort the degree sequence in non-increasing order
    degree_sequence.sort(reverse=True)

    # Continue the process until the sequence is empty or found invalid
    while degree_sequence:
        # If the largest degree is greater than the length of the sequence, it's invalid
        largest_degree = degree_sequence.pop(0)  # Take the largest degree

        # If largest degree is greater than the length of the remaining sequence, return False
        if largest_degree > len(degree_sequence):
            return False

        # Subtract 1 from the next 'largest_degree' elements
        for i in range(largest_degree):
            degree_sequence[i] -= 1
            # If any degree goes negative, the sequence is invalid
            if degree_sequence[i] < 0:
                return False

        # Remove all zeros and sort again
        degree_sequence = [deg for deg in degree_sequence if deg > 0]
        degree_sequence.sort(reverse=True)

    # If we successfully reduced the sequence to all zeros, it's graphical
    return True


degree_seq_1 = [3, 3, 3, 3, 3, 3]
degree_seq_2 = [3, 3, 3, 3, 2, 2]

print(f"Degree sequence {degree_seq_1} is graphical: {hakimi_havel(degree_seq_1)}")
print(f"Degree sequence {degree_seq_2} is graphical: {hakimi_havel(degree_seq_2)}")
