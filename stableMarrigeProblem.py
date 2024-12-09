def allocate_items(preferences):
    """
    Allocates items to players based on their preferences using an adaptation of the Gale-Shapley algorithm.
    Logs each step of the process.

    Args:
        preferences (dict): A dictionary where keys are player names and values are lists of items in preference order.

    Returns:
        dict: A dictionary with player names as keys and their allocated item as values.
        
    """
    # Create a dictionary to store the allocation result
    allocation = {player: None for player in preferences.keys()}

    # Create a list of all items
    items = set(item for pref_list in preferences.values() for item in pref_list)

    # Reverse mapping to track which items are "proposed to"
    proposed_to = {item: None for item in items}  # item -> player

    # Create a queue of players who still need an item
    free_players = list(preferences.keys())

    # Keep track of the next item each player will propose to
    next_proposal = {player: 0 for player in preferences.keys()}

    step = 1  # Step counter for debugging

    while free_players:
        print(f"\n--- Step {step} ---")
        player = free_players.pop(0)  # Get a free player
        player_prefs = preferences[player]

        # Get the next item on the player's preference list
        if next_proposal[player] < len(player_prefs):
            item = player_prefs[next_proposal[player]]
            next_proposal[player] += 1  # Increment the proposal index for this player

            print(f"{player} proposes to {item}")

            if proposed_to[item] is None:  # Item is free
                allocation[player] = item
                proposed_to[item] = player
                print(f"{item} is free and now belongs to {player}")
            else:  # Item is already proposed to someone else
                current_holder = proposed_to[item]
                current_holder_prefs = preferences[current_holder]

                # Compare preferences
                if current_holder_prefs.index(item) > player_prefs.index(item):  # New player is preferred
                    allocation[player] = item
                    allocation[current_holder] = None
                    proposed_to[item] = player
                    print(f"{item} switches from {current_holder} to {player}")
                    free_players.append(current_holder)  # Current holder becomes free
                else:
                    free_players.append(player)  # Player stays free
                    print(f"{item} rejects {player}, stays with {current_holder}")
        else:
            print(f"{player} has no more items to propose to")

        step += 1  # Increment step counter

    print("\n--- Final Allocation ---")
    for player, item in allocation.items():
        print(f"{player} gets {item}")

    return allocation


preferences = {
    "Dark Urge": ["Duelist's Peragative", "Rhapsody + DJ Scimitar", "Shar Spear", "Hellfire Greataxe"],
    "Karlach": ["Hellfire Greataxe", "Shar Spear", "Duelist's Peragative", "Duelist's Peragative"],
    "Astarion": ["Duelist's Peragative", "Rhapsody + DJ Scimitar", "Shar Spear", "Hellfire Greataxe"],
    "Shadowheart": ["Shar Spear", "Duelist's Peragative", "Rhapsody + DJ Scimitar", "Hellfire Greataxe"]
}

allocation_result = allocate_items(preferences)
