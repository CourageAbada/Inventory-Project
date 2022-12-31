        Shoe Inventory Management System
This project is a python script that allows users to manage a shoe inventory. The script includes functions to read in shoe data from a text file, add new shoe data, view all the shoe data, restock shoes, search for a specific shoe by code, and view the value of each item in the inventory.

        Prerequisites
Before running the script, make sure that you have the following libraries installed:
email
tabulate
You will also need a text file named inventory.txt in the same directory as the script, with the following format:

        Running the script
To run the script, simply execute the following command in your terminal:
python shoe_inventory.py

        Using the script
The script will present you with a menu of options:

1)Read Shoes Data
2)Add Shoes
3)View All
4)Restock Shoes
5)Search Shoe
6)Value per Item
7)Quit
Select an option by entering the corresponding number and pressing enter.

        Read Shoes Data
This option will read in the shoe data from the inventory.txt file and store it in memory. This option should be run first before any other options.

        Add Shoes
This option will allow you to add a new shoe to the inventory by prompting you for the country of manufacture, code, product name, cost, and quantity.

        View All
This option will display all the shoe data in the inventory.

        Restock Shoes
This option will allow you to restock a shoe with the lowest quantity in the inventory. You will be prompted to enter a new quantity to add to the current quantity of the shoe.

        Search Shoe
This option will allow you to search for a specific shoe by code. If the shoe is found, its data will be displayed.

        Value per Item
This option will display the value of each shoe in the inventory, calculated as the product of the cost and quantity of each shoe.

        Quit
This option will exit the script.

