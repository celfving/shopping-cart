# shopping_cart.py
# Guided screencast helped significantly with set up code

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)

# INPUT

# got timestamp code from https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/ 
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
# got hint for tax rate from after class office hours 
TAX_RATE = float(os.getenv("TAX_RATE",default = ".1"))
import time 
from datetime import datetime

subtotal_price = 0
selected_ids = []

while True: 
    selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ") #> "9" (string)
    # print(selected_id)
    # print(type(selected_id))
    if selected_id == "DONE": 
        break
    else: 
        selected_ids.append(selected_id)

# OUTPUT

# print(selected_ids)

timeStr = time.ctime()

print("--------------------")
print("11TH STREET GROCERY")
print("--------------------")
print("Web: www.11thstreetgrocery.com")
print("Phone: 1.555.123.4567")
print("Checkout Time:", timeStr)
print("--------------------")

print("Shopping Cart Items: ")
for selected_id in selected_ids: 
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #> (list)
    # print(matching_products)
    # print(type(matching_products))
    matching_product = matching_products[0] #> (dictionary)
    # print(matching_product)
    # print(type(matching_product))
    subtotal_price = subtotal_price + matching_product["price"]
    print("+ " + matching_product["name"] + " " + "(" + to_usd(float(str(matching_product["price"]))) + ") ")
print("--------------------")

print("Subtotal: " + to_usd(float(str(subtotal_price)))) 
sales_tax = (subtotal_price * TAX_RATE)
print("NYC Sales Tax (8.75%): ", to_usd(float(sales_tax)))
total_price = to_usd(subtotal_price + sales_tax)
print("Total: ", total_price) 
print("--------------------")

print("Thank you for your business! Please come again!")
print("--------------------")