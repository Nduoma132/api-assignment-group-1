from main import books

#ALL FUNCTIONS
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_all_books():
    return books

def get_book_by_title(book_title):
    new_books = []
    for book in books:
        if book_title.lower() == book["title"].lower():
            new_books.append(book)
    return new_books

def get_book_by_author(author_name):
    new_books = []
    for book in books:
        if author_name.lower() == book["author"].lower():
            new_books.append(book)
    return new_books


def add_new_book_to_list(title, author):
    for existing_book in books:
        if existing_book["title"].lower() == title.lower() and existing_book["author"].lower() == author.lower():
            return "Error: This book already exists."

    books.append({"title": title, "author": author})
    return f"Success: {title} has been added"

def update_book_by_title(current_title, new_title, new_author):
    for book in books:
        if book["title"].lower() == current_title.lower():
            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}

def get_book_by_prime():
    new_books = []
    for book in books:
        # split_val = book["title"][-1]
        split_title = book["title"].split()
        if len(split_title) >= 2 and split_title[1].isdigit():
            split_val = int(split_title[1])
            if is_prime(split_val):
                new_books.append(book)
    return new_books

def delete_book_by_title(book_title):
    for book in books:
        if book_title.lower() == book["title"].lower():
            books.remove(book)
    return f"Success: {book['title']} has been removed"

def find_empty_authors(book_title):
    for book in books:
        if book_title.lower() == book["title"].lower() and book["author"] == "":
            return f"{book['title']} has an empty author"
    return "This book has an author"

def search_by_keyword(the_keyword):
    search_results = []
    for book in books:
        if the_keyword.lower() in book["title"].lower() or (book["author"] == "" and the_keyword.lower() in book["title"].lower()):
            search_results.append({"title": book["title"], "author": book["author"]})
    if search_results:
        return search_results
    else:
        return "No matches in the database"
