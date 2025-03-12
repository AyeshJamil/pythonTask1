def search_by_author(inventory,author_name):
    """
    Search for books written by a specific author in the inventory.
    
    :param inventory: Dictionary with ISBN as keys and book details as values
    :param author_name: The author's name to search for
    :return: List of tuples containing (ISBN, title) of matching books 
    """
    return [(isbn, details["title"]) for isbn, details in inventory.items() if details.get ("author") == author_name]

# Example inventory dictionary
inventory = {
    "978-0-312-27323-1": {"title": "Moth Smoke", "author": "Mohsin Hamid"},
    "978-0-312-55187-2": {"title": "Burnt Shadows", "author": "Kamila Shamsie" },
    "978-0-156-03402-9": {"title":"The Reluctant Fundamentalist","author": "Mohsin Hamid"}
}

# Example usage
author_to_search = "Mohsin Hamid"
matching_books = search_by_author(inventory, author_to_search)
print(matching_books)
