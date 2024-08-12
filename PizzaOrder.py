print("Welcome to the Python Pizza Delivieries!")
size = input("What size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepporoni? Y or N\n")
extra_cheese = input("Do you want extra chese? Y or N\n")

bill = int(0)
if size == "S":
    bill += 15
    print("Your Small pizza will cost $15")
    if add_pepperoni == "Y":
        bill += 2
        print("Your Pepporoni order has been added with a $2 charge.")
    if extra_cheese == "Y":
        bill += 1
        print("Your extra cheese order has been added with a $1 charge.")
elif size == "M":
    bill += 20
    print("Your Medium pizza will cost $20")
    if add_pepperoni == "Y":
        bill += 2
        print("Your Pepporoni order has been added with a $2 charge.")
    if extra_cheese == "Y":
        bill += 1
        print("Your extra cheese order has been added with a $1 charge.")
elif size == "L":
    bill += 25
    print("Your Large pizza will cost $25")
    if add_pepperoni == "Y":
        bill += 2
        print("Your Pepporoni order has been added with a $2 charge.")
    if extra_cheese == "Y":
        bill += 1
        print("Your extra cheese order has been added with a $1 charge.")
else:
    print("That is not a valid size.")

print(f"Your current bill is ${bill}.")