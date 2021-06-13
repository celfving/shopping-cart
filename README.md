# shopping-cart

## Setup
This README.md file has been adapted from Professor Rossetti's procedure for this project.

Create a new repository called "shopping-cart" using the GitHub online interface. Add a "README.md" file and a Python-flavored ".gitignore" file. 

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like Documents.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Documents/GitHub/rock-paper-scissors-exercise
```

Use your text editor or the command-line to create a file in that repo called "shopping_cart.py", and then place the following contents inside:

```
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
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

print(products)
```

## Environment Setup

Create a ".env" file and a "requirements.txt" file. The ".env" file should contain: 'TAX_RATE=".0875"'. The "requirements.txt" file should contain 'python-dotenv'. Create and activate a new Anaconda virtual environment. Use a "requirements.txt" file approach to installing your packages. 

```
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt # (after specifying desired packages inside)
```

Within the active virtual environment, demonstrate your ability to run the Python script from the command-line:

```py
python shopping_cart.py
```

If you see the provided "products" data structure, you're ready to move on to project development.

## Data Setup

The provided code includes a variable called products which facilitates management of the products inventory from within the application's source code. 

## Capturing User Inputs 

Steps:

1. Accept a user input value, store it in a variable, and print it. HINT: use the input() function.
2. One at a time, iteratively accept a user input value, store it in a variable, and print it. HINT: use an infinite while loop. NOTE: you may have to press "control-c" to quit your script if you get stuck.
3. One at a time, iteratively accept a user input value, store it in a variable, and print it. But stop the loop if the user inputs the word "DONE". HINT: use an if statement in conjunction with the break keyword.
4. Repeat the previous step, but instead of printing each user input, store them all in a single list. Then print the list after the user is "DONE".

## Look Up the Products

Steps:

1. For a single valid product identifier, look up the matching product and print its name and price. HINT: try using a custom function in conjunction with a list comprehension.
2. For each valid product identifier in the example list, look up the matching product and print its name and price.
3. For each valid product identifier in the example list, look up the matching product and print its name and price, and add its price to a running-total of all prices, then print the running-total after iterating through the entire list. 

## Printing the Receipt 

Steps:

1. For each receipt component listed in the project requirements (e.g. store name, product prices, taxes, total price, farewell message, etc.), revise your program to print that component.

## Finished Product

The final product should be able to do the following: 

1. Capture product identifiers
2. Handle invalid inputs and fail gracefully on invalid product lookups
3. Instruct the user about and handle the "DONE" signal
4. Display the store's info
5. Display the checkout date and time
6. Display the names and prices of all scanned products
7. Display subtotal, tax, and total amounts

## Example Output 

```
(shopping-env)  --->> python shopping_cart.py
Please input a product identifier: 1
Please input a product identifier: 2
Please input a product identifier: 3
Please input a product identifier: 2
Please input a product identifier: 1
Please input a product identifier: DONE
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2020-02-07 03:54 PM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... All-Seasons Salt ($4.99)
#>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
#>  ... All-Seasons Salt ($4.99)
#>  ... Chocolate Sandwich Cookies ($3.50)
#> ---------------------------------
#> SUBTOTAL: $19.47
#> TAX: $1.70
#> TOTAL: $21.17
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------
```
