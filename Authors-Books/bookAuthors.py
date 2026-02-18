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

while choice != 6:

# >>>>>>>>>>>>>>>>>>
# OPTION 1 - ADD
# >>>>>>>>>>>>>>>>>>
    if choice == 1:
        author = input("Author: ").strip()
        title = input("Title: ").strip()
        year = int(input("Year: ").strip())
        sale = int(input("Sales: ").strip())

        if title in titles:
            print("That book is already in the database.")
        else:
            authors.append(author)
            titles.append(title)
            years.append(year)
            sales.append(sale)
            print("Book added successfully.")

# >>>>>>>>>>>>>>>>>>>>
# OPTION 2 - DELETE
# >>>>>>>>>>>>>>>>>>>>
    elif choice == 2:
        title = input("Enter title to delete: ").strip()

        if title not in titles:
            print("Book not found.")
        else:
            index = titles.index(title)
            del authors[index]
            del titles[index]
            del years[index]
            del sales[index]
            print("Book deleted successfully.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# OPTION 3 - UPDATE SALES
# >>>>>>>>>>>>>>>>>>>>>>>>>>
    elif choice == 3:
        title = input("Enter title to update: ").strip()

        if title not in titles:
            print("Book not found.")
        else:
            index = titles.index(title)
            print(f"{titles[index]} ({years[index]}) by {authors[index]} has sales of {sales[index]:,}.")
            new_sales = int(input("New Sales >>> ").strip())
            sales[index] = new_sales
            print("Record updated.")
            print(f"{titles[index]} ({years[index]}) by {authors[index]} now has sales of {sales[index]:,}.")