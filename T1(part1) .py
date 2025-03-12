# Creating an empty dictionary
books = {}

# Adding books with details (ISBN as key, tuple as value)
books["978-0-312-27323-1"] = ("Moth Smoke", "Mohsin Hamid", 15.99, {"Fiction", "Drama"})
books["978-0-312-55187-2"] = ("Burnt Shadows", "Kamila Shamsie", 14.50, {"Historical", "Drama"})
books["978-0-156-03402-9"] = ("The Reluctant Fundamentalist", "Mohsin Hamid", 12.99, {"Thriller", "Political"})

# Printing the dictionary
for isbn, details in books.items():
    print(f"ISBN: {isbn}, Title: {details[0]}, Author: {details[1]}, Price: ${details[2]:.2f}, Genres: {', '.join(details[3])}")