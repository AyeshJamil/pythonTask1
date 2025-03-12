# Function to update book price
def update_price(inventory, isbn, new_price):
    """
    Update the price of a book if the ISBN exists in the inventory.
    
    :param inventory: Dictionary with ISBN as keys and book details as values
    :param isbn: The ISBN of the book to update
    :param new_price: The new price to set
    :return: True if the update was successful, False if ISBN not found
    """
    if isbn in inventory:
        details = inventory[isbn]  # Get the existing book details
        updated_details = (details[0], details[1], new_price, details[3])  # Create a new tuple with updated price
        inventory[isbn] = updated_details  # Replace the old tuple with the new one
        return True
    return False  # ISBN not found

# Example inventory dictionary
books = {
    "978-0-312-27323-1": ("Moth Smoke", "Mohsin Hamid", 15.99, {"Fiction", "Drama"}),
    "978-0-312-55187-2": ("Burnt Shadows", "Kamila Shamsie", 14.50, {"Historical", "Drama"}),
    "978-0-156-03402-9": ("The Reluctant Fundamentalist", "Mohsin Hamid", 12.99, {"Thriller", "Political"})
}

# Example usage
isbn_to_update = "978-0-312-27323-1"
new_price = 18.99

if update_price(books, isbn_to_update, new_price):
    print(f"Price updated successfully for ISBN {isbn_to_update}.")
else:
    print(f"ISBN {isbn_to_update} not found.")

# Print updated inventory
for isbn, details in books.items():
    print(f"ISBN: {isbn}, Title: {details[0]}, Author: {details[1]}, Price: ${details[2]:.2f}, Genres: {', '.join(details[3])}")