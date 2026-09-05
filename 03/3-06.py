# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#   * Start with your program from Exercise 3-4 or Exercise 3-5. Add a `print()` call to the end of your program informing people that you found a bigger dinner table.
#   * Use `insert()` to add one new guest to the beginning of your list.
#   * Use `insert()` to add one new guest to the middle of your list.
#   * Use `append()` to add one new guest to the end of your list.
#   * Print a new set of invitation messages, one for each person in your list.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

guests = ["Shaheer", "Ayan", "Ghous"]

print(f"Hello, {guests[0]}! You are invited to dinner at my house!")
print(f"Hello, {guests[1]}! You are invited to dinner at my house!")
print(f"Hello, {guests[2]}! You are invited to dinner at my house!")

print(f"\nSorry everyone, {guests[2]} couldn't make it to the dinner.")

del guests[2]
guests.append("Yahya")
print()

print(f"Hello, {guests[0]}! You are invited to dinner at my house!")
print(f"Hello, {guests[1]}! You are invited to dinner at my house!")
print(f"Hello, {guests[2]}! You are invited to dinner at my house!")

print(
    "\nHello everyone, I just found a bigger dinner table! We can now invite more friends!"
)

guests.insert(0, "Dawood")
guests.insert(1, "Faiq")
guests.append("Hanzala")

print(f"Hello, {guests[0]}! You are invited to dinner at my house!")
print(f"Hello, {guests[1]}! You are invited to dinner at my house!")
print(f"Hello, {guests[2]}! You are invited to dinner at my house!")
print(f"Hello, {guests[3]}! You are invited to dinner at my house!")
print(f"Hello, {guests[4]}! You are invited to dinner at my house!")
print(f"Hello, {guests[5]}! You are invited to dinner at my house!")
