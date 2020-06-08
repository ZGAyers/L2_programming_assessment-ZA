# Component 03 - converts from grams into kilograms


# Not Blank function goes here
def not_blank(question, error_msg, ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)

        # If response is blank, question is repeated (loop starts over)
        if response == "":
            print(error)
            continue

        # if response is not blank, program continues
        else:
            return response


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


# main routine

# set up lists
printout = []
converted_weight = []

stop = ""
while stop != "exit":
    product = []
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'exit' to quit")
    product.append(get_product)

    # if user enters exit code break loop
    if get_product == "exit":
        break

    # get cost from user
    get_cost = num_check("Cost: $")

    # get weight of item from user
    get_weight = num_check("Weight(g): ")

    # append the information the user entered into a single line of code
    printout.append("${:.2f} {}, {:.2f}g".format(get_cost, get_product.title(), get_weight))

    if get_weight > 1:
        print("hi")


for item in printout:
    print(item)
