# 🍦 Self Love Ice Cream - Simple Ordering Program

## Overview

This is a simple Python console-based program that simulates an ice cream ordering system. It allows users to view available flavors, place multiple orders, and receive a total bill at the end.

## What the Code Does

### 1. Displays a Welcome Message and Menu

The program starts by printing a welcome message along with a list of available ice cream flavors and their prices:

* Vanilla Ice-cream – BDT 20
* Chocolate Ice-cream – BDT 20
* Mango Ice-cream – BDT 30
* Strawberry Ice-cream – BDT 30

---

### 2. Initializes Variables

* `orders`: A list used to store all customer orders.
* `total_bill`: A variable used to calculate the final total price.

---

### 3. Takes User Input

The user is asked:

* How many different flavors they want to order.
* For each order:

  * The flavor number (from the menu)
  * The quantity

---

### 4. Processes Each Order

For every item ordered:

* The program matches the selected flavor number with its name and price.
* Calculates the total price for that item (`price × quantity`).
* Stores the order details (flavor, quantity, total price) in the `orders` list.
* Displays a summary of the current item ordered.

---

### 5. Displays Order Summary

After all inputs are taken:

* The program loops through all stored orders.
* Prints each item with its quantity and total price.
* Adds each item's cost to the final bill.

---

### 6. Shows Final Bill

Finally, the program:

* Confirms the order.
* Displays the total amount the user needs to pay.

---

## Example Output (VS Code Terminal)

```
Welcome to Self Love ice cream
Check out lovable flavours:
1. Vanilla Ice-cream - BDT 20
2. Chocolate Ice-cream - BDT 20
3. Mango Ice-cream - BDT 30
4. Strawberry Ice-cream - BDT 30
Enter the number of flavor you want to order: 2
Enter the no. 1: 4
Enter the quantity: 3
Ordered: 
Flavor: Strawberry
Quantity: 3
Enter the no. 2: 1
Enter the quantity: 2
Ordered: 
Flavor: Vanilla
Quantity: 2
Your order: 
1. Strawberry x 3 = 90
----------------------------------------
2. Vanilla x 2 = 40
----------------------------------------
Order confirmed.
Total Bill: 130
```

---

## Notes

* The program uses basic Python concepts such as loops, conditionals, lists, and dictionaries.
* It runs entirely in the terminal and requires user interaction.
* There is a small issue in the code where the Mango flavor is mistakenly labeled as "Chocolate" during processing.

---

## How to Run

1. Make sure Python is installed.
2. Run the script in a terminal:

   ```bash
   python filename.py
   ```
3. Follow the on-screen instructions to place your order.

---

Enjoy your virtual ice cream ordering experience! 🍨
