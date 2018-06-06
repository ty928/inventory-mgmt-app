import csv
import os

def menu(username="@ty928", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename="products.csv"):
    filepath =os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []
    #TODO: open the file and populate the products list with product dictionaries

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            # print(row["name"], row["price"])
            products.append(dict(row))
    return products


def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name","aisle","department","price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)


def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    #print(products)
    write_products_to_file(filename, products)

def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    number_of_products = len(products)
    my_menu = menu(username="@ty928", products_count=number_of_products)
    user_input = input(my_menu) #TODO instead of printing, capture user input

    #operation = operation.title()
    if user_input == "list":
        list_products(products)
    elif user_input == "show":
        show_products(products)
    elif user_input == "create":
        create_products(products)
    elif user_input == "destroy":
        destroy_products(products)
    elif user_input == "update":
        update_products(products)

    # else user_input == "reset":
    #     reset_products_file()


def list_products(products):
    print("Listing " + str(len(products)) + " products")
    for p in products:
        print("#" + p["id"] +":" + p["name"])


def show_products(products):
    product_id = input("OK. Please sepecify the product's identifier: ")
    matching_products = [product for product in products if int(product["id"]) == int(product_id)]
    matching_product = matching_products[0]
    print(matching_product)

def create_products(products):
    new_id = int(products[-1]["id"])+1
    new_name = input("PLEASE input the product's 'name': ")
    new_aisle = input("PLEASE input the product's 'aisle': ")
    new_department = input("PLEASE input the product's 'department': ")
    new_price = input("PLEASE input the product's 'price': ")

    new_product = {
        "id": new_id,
        "name": new_name,
        "aisle": new_aisle,
        "department": new_department,
        "price": new_price
    }
    products.append(new_product)
    print("Create a new product: ")
    print("-------------------------------")
    print(new_product)
    write_products_to_file(products=products)

def destroy_products(products):
    product_id = input("OK. Please sepecify the product's identifier: ")
    matching_products = [product for product in products if int(product["id"]) == int(product_id)]
    matching_product = matching_products[0]
    del products[products.index(matching_product)]
    print("destroy a product:")
    print("-------------------------------")
    print(matching_product)
    write_products_to_file(products=products)

def update_products(products):
    product_id = input("OK. Please sepecify the product's identifier: ")
    matching_products = [product for product in products if int(product["id"]) == int(product_id)]
    matching_product = matching_products[0]

    new_name = input("What is the product new 'name': ")
    new_aisle = input("What is the product new 'aisle': ")
    new_department = input("What is the product new 'department': ")
    new_price = input("What is the product new 'price': ")

    matching_product["name"] = new_name
    matching_product["aisle"] = new_aisle
    matching_product["department"] = new_department
    matching_product["price"] = new_price

    print("Updated a product: ")
    print("-------------------------------")
    print(matching_product)

    write_products_to_file(products=products)

    #for product in products if product["id"] == product_id:




    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    #TODO: handle selected operation

    # Finally, save products to file so they persist after script is done...



# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
