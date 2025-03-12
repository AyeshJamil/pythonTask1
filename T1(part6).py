def list_all_books(inventory):
    """
    Compiles and returns a sorted list of all book titles in the inventory.

    :param inventory: Dictionary with ISBN as keys and book details stored in tuples
    :return: Alphabetically sorted list of book titles
    """
    return sorted([details[0] for details in inventory.values()])

# Example inventory dictionary (with tuples for book details)
inventory = {
    "978-0-312-27323-1": ("Moth Smoke", "Mohsin Hamid", {"Fiction", "Drama"}, 15.99),
    "978-0-312-55187-2": ("Burnt Shadows", "Kamila Shamsie", {"Historical", "Drama"}, 14.50),
    "978-0-156-03402-9": ("The Reluctant Fundamentalist", "Mohsin Hamid", {"Thriller", "Political"}, 12.99),
}

# Get sorted book titles
sorted_titles = list_all_books(inventory)

# Print the sorted list of titles
print(sorted_titles)