# Overview

This is a Food Inventory program. It's very easy to use! Just run the program and use the console menu that will help you in every step. All the information is stored on a database using SQL.

Ideally any user who uses this program will have an accurate inventory of their current food. Once an item is updated to 0, another database can be created through the menu that includes all of those items, which is just perfect for a shopping list!

[Software Demo Video](https://youtu.be/hW5cGhynaSs)

# Relational Database

The SQL table currently has two columns:
* Product: Keeps the name of the item to store
* Quantity: Shows the available quantity of the product.

# Development Environment

This program is made with Python, using the squlite3 library. The console menu is made in Python, and the SQL commands are used through the already mentioned library.

# Useful Websites

* [SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
* [Python Style Guide](https://peps.python.org/pep-0008/)

# Future Work

* On add_item(), verify if an item is already on the database. If it is there. prompt if the user would like to update the value instead.
* On remove_item(), have a check_substring() function that would return all the existing values on the database where the substring exists. Then, that list would be displayed to the user, and from there they make the selection.
* On add_item() there is a bug where users can't enter a digit as part of the product, e.g "1LB rice". Solving this would either mean allowing digits to be entered, or adding another column for the measurement.
* Implement the create_shopping_list() function.
