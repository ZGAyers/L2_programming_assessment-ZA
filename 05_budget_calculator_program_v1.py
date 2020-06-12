# V1 of Budget Calculator Final Program


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
kg_weight = []
afford_list = []
weight_aff = []


# Ask user what their budget is for the item
budget = num_check("Budget: ")

# print out the users budget in correct format
print("Your budget is ${:.2f}".format(budget))

# loop of getting information from user
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
    # if the weight is in g:
    if get_weight > 0.999:
        printout.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))
        kg_weight.append(get_weight / 1000)

    # if weight is in kg already:
    else:
        printout.append("${:.2f} {}, {}kg".format(get_cost, get_product.title(), get_weight))
        kg_weight.append(get_weight)

    # if the user can afford the product
    if budget == get_cost:
        afford_list.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))
        weight_aff.append(get_weight)

    elif budget > get_cost:
        afford_list.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))
        weight_aff.append(get_weight)

    # get the suggested item
    tp_weight = ("${:.2f} {}, {}g".format(get_cost, get_product.title(), max(weight_aff)))


# print out list of items
for item in printout:
    print(item)

# print out items they can afford
print()
if afford_list != []:
    print("Affordable product/s within a ${:.2f} budget: ".format(budget))
    for item in afford_list:
        print(item)

    # print out the suggested item
    print()
    print("Suggested Item:")
    print(tp_weight)
else:
    print("--------------------------------------")
    print("You can't afford any of these products")
    print("--------------------------------------")
