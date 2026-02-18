# bookAuthors.py
# gabriel mihail
# create a Python file using Git, code to read from the file into four lists


# -----------------------------
# LOAD DATA INTO LISTS
# -----------------------------

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
    print(authors)
