# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#   * Add a new pizza to the original list.
#   * Add a different pizza to the list friend_pizza.
#   * Prove that you have two separate lists. Print the message 'My friend's favourite pizzas are;', and then use a `for` loop to print the second list. Make sure each new pizza is stored in the appropriate list.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pizzas = ["Chicken Tikka", "Chicken Fajita", "Pepperoni"]

friends_pizzas = pizzas[:]

pizzas.append("BBQ Chicken")

friends_pizzas.append("Chicken Lovers")

print("My favourite pizzas are:")
for i in pizzas:
    print(i)

print("My friend's favourite pizzas are:")
for i in friends_pizzas:
    print(i)
