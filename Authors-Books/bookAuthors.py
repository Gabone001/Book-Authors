# bookAuthors.py
# gabriel mihail
# create a Python file using Git, code to read from the file into four lists


# >>>>>>>>>>>>>>>>>>>>>>>>>
# LOAD DATA INTO LISTS
# >>>>>>>>>>>>>>>>>>>>>>>>>

authors = []
titles = []
years = []
sales = []

with open("books.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        authors.append(parts[0].strip())
        titles.append(parts[1].strip())
        years.append(int(parts[2].strip()))
        sales.append(int(parts[3].strip()))


# >>>>>>>>>
# MENU
# >>>>>>>>>

MENU = """
1. Add a new book
2. Delete a book
3. Update the sales figure of a book
4. Find books by an author
5. Find the oldest book(s)
6. Quit
Enter choice >>> """

choice = int(input(MENU))