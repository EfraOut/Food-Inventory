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
    print() # Blank space before the table.
    cursor.execute("SELECT * FROM food")
    print("{:>10}  {:>10}".format("Product", "Quantity"))
    for record in cursor.fetchall():
        print(f"{record[0]:>10}  {record[1]:>10}")
    print() # Blank space after the table.


def add_item():
    """
    Adds an item to the database. User will be prompt for
    product's name and the quantity.
    Parameters: None
    Return: None
    """

    # Prompting for the product, and making sure it's correct data.
    product = input("Enter name of the product: ")
    while not product.isalpha():
        print("Please enter a valid product.")
        product = input("Enter name of the product: ")
    assert product.isalpha(), "The product is not a string"

    # Prompting for the quantity, and making sure it's correct data.
    quantity = input("Enter amount you currently have: ")
    while int(quantity) < 1:
        print("Please enter a valid quantity.",
              "Remember that you are adding something you already have.")
        quantity = input("Enter amount you currently have: ")
    quantity = int(quantity) # We transform now because we know it's a number.
    assert type(quantity) == int, "There was a problem converting to int"
    assert quantity > 0, "An incorrect value almost slipped through!"

    # Adding correct data into the database.
    values = (product, quantity)
    cursor.execute("INSERT INTO food VALUES(?, ?)", values)
    connection.commit()


def remove_item():
    """
    Removes an item from the database. User will enter a string of
    what they desire to remove. If multiple matches are found, they will
    be displayed on the screen, and then user will specify which one is
    desired.
    After the selection is done, the item will be deleted.
    """

    # Prompting and checking for the item to be deleted.
    item = input("Enter the product you wish you delete: ")
    while not item.isalpha():
        print("Please enter a string")
        item = input("Enter the product you wish you delete: ")
    
    # The function check_substring() goes here. The value returned
    # is what the cursor would execute.

    # Selecting the desired item from the database.
    value = (item,)
    cursor.execute("SELECT product FROM FOOD WHERE product=?", value)
    products = cursor.fetchall()

    # Checking if the cursor returned a value.
    # If not, we return the function.
    if products == []:
        print("Couldn't find", item, "in the database.")
        return

    # Displaying all the returned values.
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]}")
    print()

    # User selection and checking that it is correct.
    choice = input("Select the desired product: ")
    while int(choice) < 0:
        print("Please enter a valid option.")
        choice = input("Select the desired product: ")
    choice = int(choice)
    assert choice > 0, "This is not a valid option."

    # Selecting the product and deleting it.
    value = products[choice - 1]
    cursor.execute("DELETE FROM food WHERE product=?", value)
    connection.commit()


def update_quantity():
    """
    Changes the quantity of an already existing item on the database.
    """
    
    # Prompting and checking for the item.
    item = input("Enter the product you wish you delete: ")
    while not item.isalpha():
        print("Please enter a string")
        item = input("Enter the product you wish you delete: ")
    
    # Prompting and verifying the quantity is valid.
    quantity = input("New quantity: ")
    while int(quantity) < 0:
        print("Please enter a positive integer.")
        quantity = input("New quantity: ")
    quantity = int(quantity)
    assert quantity >= 0, "An invalid number almost slipped through!"

    # Updating the quantity on the given item.
    values = (quantity, item)
    cursor.execute("UPDATE food SET quantity=? WHERE product=?", values)
    connection.commit()


def create_shopping_list():
    """
    Creates a .xlsx with the items on the database where quantity=0.
    """
    pass


main()
connection.close()
