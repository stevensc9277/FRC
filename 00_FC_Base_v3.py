import pandas

# Checks that input is either a float or an integer that is more than zero. Takes in custom error messages
def num_check(question, error, type):
    
    while True:
        try:
            response = type(input(question))

            if response <= 0:
                print(error)
                print()
            else:
                return response

        except ValueError:
            print(error)

def not_blank(question, error):


    while True:
        response =  input(question)
    
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

        return response

# yes / no checker
def yes_no(question):

    to_check = ["yes", "no"]

    while True:
        response =  input(question).lower()
    
        for var_item in to_check:
            if response == var_item:
                return response

            elif response == var_item[0]:
                return var_item 
        
        print("Please enter either yes or no...\n")

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Gets expenses, returns lists which has the data frame and sub total
def get_expenses(var_fixed):
    # set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")

        if item_name.lower() == "xxx":
            break
        
        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)

        else:
            quantity = 1
        
        price = num_check("How much ? $", "The price must be a number more than zero", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

        
    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# Prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("*** {} Costs ***".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""

# *** Main routine starts here ***

# Get product name
product_name = not_blank("Product name: ", "The product name")

print()
print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0


# Ask user for profit goal

# Calculate recommended price

# Write data to file

# Printing area

print()
print("*** Fund Raising - {} ***".format(product_name))
print()
expense_print("Variable", variable_frame, variable_sub)

# show fixed costs if there are any
if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)
