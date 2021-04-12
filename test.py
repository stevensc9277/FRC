def int_check(question, low, high):
    error = ""
    
    while True:
        try:
            response = int(input(question))

            if response < low:
                print(error)
                print()
            elif response > high:
                print(error)
                print()
            else:
                return response
        except ValueError:
            print(error)


number = int_check("Enter a number: ", 1, 10)