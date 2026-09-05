# 4-14. Code Review: Choose three of the programs you've written in this chapter and modify each one to comply with PEP 8.
# -----------------------------------------------------------------------------------------------------------------------

# 4-12:
pizzas = ["Chicken Tikka", "Chicken Fajita", "Pepperoni"]

friends_pizzas = pizzas[:]

pizzas.append("BBQ Chicken")
friends_pizzas.append("Chicken Lovers")

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for friend_pizza in friends_pizzas:
    print(friend_pizza)

# 4-11:
pizzas = ["Chicken Tikka", "Chicken Fajita", "Pepperoni"]

friends_pizzas = pizzas[:]

pizzas.append("BBQ Chicken")
friends_pizzas.append("Chicken Lovers")

print("My favourite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favourite pizzas are:")
for pizza in friends_pizzas:
    print(f"- {pizza}")

# 4-10:
languages = ["python", "javascript", "c++", "ruby", "react"]

print(f"The first three items in the list are: {languages[:3]}")
print()

print(f"Three items from the middle of the list are: {languages[1:4]}")
print()

print(f"The last three items in the list are: {languages[-3:]}")
print()
