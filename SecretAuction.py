print("Welcome to the secret auction program")


check = True
dictionary = {}

#highest = 0
#name_highest = ""
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    highest_name = ""
    for name in dictionary:
        bid = dictionary[name]
        if bid > highest_bid:
            highest_bid = bid
            highest_name = name
    # print(f"The winner is {highest_name} with a bid of ${highest_bid}")
    return highest_name, highest_bid

while check:
    name = input("what is your name ")
    bid = int(input("what is your bid "))
    response = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    dictionary[name] = bid

    # if bid > highest:
    #     highest = bid
    #     name_highest = name
    if response == 'no':
        check = False
    print("\n" * 20)

    if check == False:

        highest_name, highest_bid = find_highest_bidder(dictionary)
        print(f"The winner is {highest_name} with a bid of ${highest_bid}")






#print(f"The winner is {name_highest} with a bid of ${highest}")