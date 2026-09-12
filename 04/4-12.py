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
