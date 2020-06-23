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
kg_weight = ""
get_weight = ""
get_cost = ""
get_product = ""
afford_list = []
per_kg = []
suggest = []
string_list = []

# Bold print out text option
bold = "\033[1m"
reset = "\033[0;0m"

# introduce the user to the program
print(bold, "Budget Calculator", reset)
print("This program is used to compare prices of products in store")
print("The program will then remove the items you can't afford and "
      "suggest one of the products based on its cost and weight.")
print()

# Ask user what their budget is for the item
budget = num_check("What is your budget: $")
print()

# loop of getting information from user
print("Please enter a product, its cost and its weight.")
print("If you have finished entering products type", bold, "'exit'", reset,
      "to get a printout of the products")
print()

stop = ""
while stop != "exit":
    product = []
    print()
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'exit' to quit").lower()
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

        kg_weight = get_weight / 1000

    # if weight is in kg already:
    else:
        printout.append("${:.2f} {}, {}kg".format(get_cost, get_product.title(), get_weight))

        kg_weight = get_weight

    # if the user can afford the product
    if budget >= get_cost:
        per_kg.append(get_cost / kg_weight)
        afford_list.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight))

        string_list.append("${:.2f} {}, {}g".format(get_cost, get_product.title(), get_weight,))
        string_list.append(per_kg)

        # get the per kg for item
        print(per_kg)

if string_list[1] == min(per_kg):
    for item in string_list:
        if item not in per_kg:
            suggest.append(item)
    print("this works")

# print out list of items
print()
print(bold, "Items: ", reset)
for item in printout:
    print(item)

# print out items they can afford
print()
if afford_list != []:
    print(bold, "Affordable product/s within a ${:.2f} budget: ".format(budget), reset)
    for item in afford_list:
        print(item)

    # print out the suggested item
    print()
    print(bold, "Suggested Item:", reset)
    for item in suggest:
        print(item)

else:
    print("--------------------------------------")
    print("You can't afford any of these products")
    print("--------------------------------------")
