# V2 of Budget Calculator Final Program

# -Functions-


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


# -Main Routine-

# set up lists
printout = []
afford_list = []
per_kg = []
suggest = []
string_list = []

# set up certain variables for later code
kg_weight = ""
get_weight = ""
get_cost = ""
get_product = ""

# Bold printout text option and reset option
bold = "\033[1m"
reset = "\033[0;0m"

# introduce the user to the program / what the program is used for
print(bold, "Budget Calculator", reset)
print("This program is used to compare prices of products in store")
print("The program will then remove the items you can't afford and "
      "suggest one of the products based on its cost per kilo.")
print()

# Ask user what their budget is for the product
budget = num_check("What is your budget: $")
print()

# explains to user the look and how to exit it
print("Please enter a product, its cost and its weight.")
print("If you have finished entering products type", bold, "'exit'", reset,
      "to get a printout of the products")
print()
# loop of getting information from user
stop = ""
while stop != "exit":
    print()
    # get product name from user
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'exit' to quit").lower()

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

        # calculate the kg weight
        kg_weight = get_weight / 1000

    # if weight is in kg already:
    else:
        printout.append("${:.2f} {}, {}kg".format(get_cost, get_product.title(), get_weight))

        # append the weight that is already in kg
        kg_weight = get_weight

    # if the user can afford the product
    if budget >= get_cost:
        # get the per kg for item
        per_kg = (get_cost / kg_weight)
        # what the users can afford
        if get_weight > 0.999:
            afford_list.append("${:.2f} {}, {}g, ${:.2f} per kg".format(get_cost, get_product.title(), get_weight, per_kg))
        else:
            afford_list.append("${:.2f} {}, {}kg, ${:.2f} per kg".format(get_cost, get_product.title(), get_weight, per_kg))

        # string_list for list of what the user can afford and the per_kg
        string_list.append([get_cost, get_product.title(), get_weight, per_kg])

        print(per_kg)  # remove this later


# -Printout-
# Output section of program (prints out the information the user needs)
print()
print(bold, "Items: ", reset)
for item in printout:
    print(item)

# print out items the user can afford on their budget
print()
if afford_list != []:

    # sort the list and append the item that has the smallest cost per kg
    string_list.sort(key=lambda x: x[3])
    suggest.append(string_list[0])

    # items user can afford
    print(bold, "Affordable product/s within a ${:.2f} budget: ".format(budget), reset)
    for item in afford_list:
        print(item)

    # print out the suggested item that the user should buy
    print()
    print(bold, "Suggested Item:", reset)
    for item in suggest:
        print("${:.2f} {}, {}kg, ${:.2f} per kg".format(item[0], item[1], item[2], item[3]))

# if the user cannot afford any products, print:
else:
    print("--------------------------------------")
    print("You can't afford any of these products")
    print("--------------------------------------")
