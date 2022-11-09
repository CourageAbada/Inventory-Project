from email import header
from tabulate import tabulate
# The class Shoes is defined with the following attributes: country, code, product, cost, and quantity
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
#A fuction that will return the cost
    def get_cost(self):
        return self.cost
#A fuction that will return the quantity    
    def get_quantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity += quantity
#A fuction that will return the the string in this order
    def __str__(self):
        return f"Country: {self.country} | Code: {self.code} | Product: {self.product} | Cost: {self.cost} | Quantity: {self.quantity}"
#A list that contains the shoe data
shoe_objects = []
#A fuction that will allow the user to read the shoe data that is in inventory 
def read_shoes_data():
    with open('inventory.txt','r') as inventory:
        inventory_sort = inventory.readlines()

        for lines in inventory_sort[1:]:
            lines_split = lines.split(",")            
            temp_shoes = Shoes(lines_split[0], lines_split[1], lines_split[2], float(lines_split[3]), int(lines_split[4].strip('\n')))
            shoe_objects.append(temp_shoes)

read_shoes_data()
#A function that will allow the user to add new data in the inventory list
def capture_shoes():
    country_ob = input("Enter the country:\n")
    code_ob = input('Please enter the Shoe code:\n')
    product_ob = input('Please enter the Product:\n')
    cost_ob = int(input('Please enter the cost of the Shoe:\n'))
    quantity_ob = int(input('Please enter the shoe quantity:\n'))
    new_shoe_info = Shoes(country_ob, code_ob, product_ob, cost_ob, quantity_ob)
    shoe_objects.append(new_shoe_info)
#A fuction that will viewer to view all the stock
def view_all():
    with open('inventory.txt','r') as inventory:
        invList = inventory.readlines()
        newList = [[item] for item in invList]
        print(tabulate(newList, headers='firstrow'))
        print("\n")
#A fumction that will allow the user to restock
def re_stock():
    minValue = int(shoe_objects[0].quantity)
    shoe_pos = 0

    for number, x in enumerate(shoe_objects):
        print(number, x)
        if int(x.quantity) < minValue:
            minValue = int(x.quantity)
            shoe_pos = number
    print(minValue)
    print(shoe_pos)
    
    value_change = input('Would you like to change the Quantity of the Shoe:\n').lower()
    if value_change == 'yes':
        new_value = int(input('Please enter the new quantity:\n'))
        update_value = minValue+new_value
        shoe_objects[shoe_pos].quantity = update_value
        pass

        for number, x in enumerate(shoe_objects):
            print(number, x)
#Fumction that Allows the user to search for a shoe using the code
def search_shoe():
    shoe_code = input('Please enter the shoe code:\n')
    for i in shoe_objects:
        if i.code == shoe_code:
            print(i)
#Fuction that will allow the user to view the value of each Item
def value_per_item():
    for i in shoe_objects:
        value_per_item = i.cost*i.quantity
        print(f'The {i.product} Value is:R{value_per_item}')
#Fuction that will show the user which item is on sale
def highest_qty():
    maxValue = int(shoe_objects[0].quantity)
    shoe_position = 0

    for number2, x in enumerate(shoe_objects):
        if int(x.quantity) > maxValue:
            maxValue = int(x.quantity)
            shoe_position = number2
    print(f'This {shoe_objects[shoe_position].product} is for SALE!!!')




# This is a while loop that will keep on running until the user enters the correct input.
while True:
    user_menu = input('''RD- Read Shoe Data:\nCS- Capture Shoes:\nVA- View all data  in Inventory:\nRS- Restock the Inentory:
SS- Search for a Shoe:\nVPI- Check Value Of Each Item:\nS- Check which item is one sale:\nE- Exite\n''').lower()
    if user_menu == 'rd':
        read_shoes_data()
    elif user_menu == 'cs':
        capture_shoes()
    elif user_menu == 'va':
        view_all()
    elif user_menu == 'rs':
        re_stock()
    elif user_menu == 'ss':
        search_shoe()
    elif user_menu == 'vpi':
        value_per_item()
    elif user_menu == 's':
        highest_qty()
    elif user_menu == 'e':
        print('BYE BYEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        break
    else:
        print('You have not entered the correct input please try AGAIN!!!')
        