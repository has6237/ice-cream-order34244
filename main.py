print("Welcome to Self Love ice cream")
print("Check out lovable flavours:")
print("1. Vanilla Ice-cream - BDT 20")
print("2. Chocolate Ice-cream - BDT 20")
print("3. Mango Ice-cream - BDT 30")
print("4. Strawberry Ice-cream - BDT 30")

orders = []
total_bill = 0


num_of_flavour = int(input("Enter the number of flavor you want to order: "))


for i in range(num_of_flavour):
    flavor_no = int(input(f"Enter the no. {i+1}: "))
    quantity = int(input("Enter the quantity: "))
    if flavor_no == 1:
        flavor = "Vanilla"
        price = 20
    elif flavor_no == 2:
        flavor = "Chocolate"
        price = 20
    elif flavor_no == 3:
        flavor = "Chocolate"
        price = 30
    elif flavor_no == 4:
        flavor = "Strawberry"
        price = 30
    else:
        print("Invalid input")

    print("Ordered: ")
    print(f"Flavor: {flavor}")
    print(f"Quantity: {quantity}")

    total_price = price * quantity
    orders.append({
        "flavor": flavor,
        "quantity": quantity,
        "total_price": total_price
    })


print("Your order: ")
for i, order in enumerate(orders):
    print(f"{i+1}. {order['flavor']} x {order['quantity']} = {order['total_price']}")
    print("----------------------------------------")
    total_bill += order["total_price"]


print("Order confirmed.")
print(f"Total Bill: {total_bill}")

    

