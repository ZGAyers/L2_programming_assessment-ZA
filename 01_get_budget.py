# Component 01 - Get users budget


# Number Checking Function goes here
def num_check(question):

    error = "Please enter a number that is more than zero"
    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:

                print(error)
            else:
                return response
        except ValueError:

            print(error)

# Ask user what their budget is for the item
budget = num_check("Budget: ")

# print out the users budget in correct format
print("Your budget is ${:.2f}".format(budget))
