# 4-13. Buffet: A buffet-style restaurant offers only 5 basic foods. Think of five simple foods, and store them in a tuple.
#   * Use a for loop to print each food the restaurant offers.
#   * Try to modify one of the items, and make sure Python rejects the change.
#   * The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

foods = ("rice", "meat", "bread", "chicken", "pizza")

for food in foods:
    print(food)

# foods[0] = "burger"

foods = ("rice", "eggs", "burger", "chicken", "pizza")

for food in foods:
    print(food)
