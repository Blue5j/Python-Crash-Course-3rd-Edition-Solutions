# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
