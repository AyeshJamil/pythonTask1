def display_inventory(inventory):
    """
    Displays the book inventory in a clean, readable table format.

    :param inventory: Dictionary with ISBN as keys and book details stored in tuples
    """
    if not inventory:
        print("The inventory is empty.")
        return

    print(f"{'ISBN':<20} {'Title':<30} {'Author':<25} {'Price':<10} {'Genres'}")
    print("=" * 100)

    for isbn, (title, author, genres, price) in inventory.items():
        genre_list = ", ".join(genres)  # Convert genre set to comma-separated string
        print(f"{isbn:<20} {title:<30} {author:<25} ${price:<9.2f} {genre_list}")

# Example inventory dictionary (using tuples for book details)
inventory = {
    "978-0-312-27323-1": ("Moth Smoke", "Mohsin Hamid", {"Fiction", "Drama"}, 15.99),
    "978-0-312-55187-2": ("Burnt Shadows", "Kamila Shamsie", {"Historical", "Drama"}, 14.50),
    "978-0-156-03402-9": ("The Reluctant Fundamentalist", "Mohsin Hamid", {"Thriller" , "Political"}, 12.99),
}

# Display the inventory
display_inventory(inventory)