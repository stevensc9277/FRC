# import libraries


# *** Functions go here ***

# checks that input is either a float or an integer that is more than zero. Takes in custom error messages
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


# Checks that user has entered yes / no to a question
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


# *** Main routine goes here ***
get_int = num_check("How many do you need? ","Please enter an integer (whole number) that is more than 0\n", int)
get_cost = num_check("How much does it cost? $","Please enter an integer (whole number) that is more than 0\n", float)

print("You need: ", get_int)
print("It costs: $", get_cost)