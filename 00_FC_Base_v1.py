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


# Main routine goes here
get_int = num_check("How many do you need? ","Please enter an integer (whole number) that is more than 0\n", int)
get_cost = num_check("How much does it cost? $","Please enter an integer (whole number) that is more than 0\n", float)

print("You need: ", get_int)
print("It costs: ", get_cost)