# functions go here

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


def profit_goal(total_costs):
    increase = int(input("Profit goal? ", "%"))
    target = total_costs * (increase/100)
    return "${}".format(target)

# Loop for quick testing
all_costs = 200
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))

    print()
