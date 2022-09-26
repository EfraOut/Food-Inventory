import sqlite3

connection = sqlite3.connect("food.db")
cursor = connection.cursor()


def main():
    """
    The function that executes everything.
    """

    # Create the database but only if it doesn't exist.
    cursor.execute("CREATE TABLE if not exists food(product TEXT, quantity INT)")

    # Main loop.
    choice = -1
    while choice != 6:
        display_menu()
        choice = int(input("Your choice> "))
        match choice:
            case 1:
                display_table()
            case 2:
                add_item()
            case 3:
                remove_item()
            case 4:
                update_quantity()
            case 5:
                create_shopping_list()
            case 6:
                print("Thank you for using the system!")


def display_menu():
    """
    Displays the program's menu on the terminal.
    """
    print("1. Display table")
    print("2. Add item")
    print("3. Remove item")
    print("4. Update quantity")
    print("5. Create shopping list")
    print("6. Exit")
    print()


def display_table():
    """
    Displays the SQL database on the terminal.
    """
    cursor.execute("SELECT * FROM food")
    print("{:>10}  {:>10}".format("Product", "Quantity"))
    for record in cursor.fetchall():
        print(f"{record[0]:>10}  {record[1]:>10}    ${record[2]:>10}")


def add_item():
    """
    Adds an item to the database. User will be prompt for
    product's name and the quantity.
    """
    pass


def remove_item():
    """
    Removes an item from the database. User will enter a string of
    what they desire to remove. If multiple matches are found, they will
    be displayed on the screen, and then user will specify which one is
    desired.
    After the selection is done, the item will be deleted.
    """
    pass


def update_quantity():
    """
    Changes the quantity of an already existing item on the database.
    """
    pass


def create_shopping_list():
    """
    Creates a .xlsx with the items on the database where quantity=0.
    """
    pass


main()
connection.close()