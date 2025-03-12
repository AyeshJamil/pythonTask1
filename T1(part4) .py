def standardize_genres(inventory):
    """
    Standardizes the genres for each book in the inventory by converting to lowercase and trimming spaces.

    :param inventory: Dictionary with ISBN as keys and book details as values
    :return: None (modifies inventory in place)
    """
    for book in inventory.values():
        if "genres" in book and isinstance(book["genres"], set):
            book["genres"] = {genre.strip().lower() for genre in book["genres"]}

# Example inventory dictionary
inventory = {
    "978-0-312-27323-1": {"title": "Moth Smoke", "author": "Mohsin Hamid", "genres": {" Fiction ", "Drama"}},
    "978-0-312-55187-2": {"title": "Burnt Shadows", "author": "Kamila Shamsie", "genres": {" Historical", "Drama "}},
    "978-0-156-03402-9": {"title": "The Reluctant Fundamentalist", "author": "Mohsin Hamid", "genres": {"Thriller", "Political"}}
}

# Standardize genres
standardize_genres(inventory)

# Print updated inventory
print(inventory)