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
print()

guests.insert(0, "Dawood")
guests.insert(1, "Faiq")
guests.append("Hanzala")

print(f"Hello, {guests[0]}! You are invited to dinner at my house!")
print(f"Hello, {guests[1]}! You are invited to dinner at my house!")
print(f"Hello, {guests[2]}! You are invited to dinner at my house!")
print(f"Hello, {guests[3]}! You are invited to dinner at my house!")
print(f"Hello, {guests[4]}! You are invited to dinner at my house!")
print(f"Hello, {guests[5]}! You are invited to dinner at my house!")

print(
    "\nSorry everyone, my new dinner table can't arrive on time so we can only have two guests now. :("
)
print()

popped1 = guests.pop(0)
popped2 = guests.pop(0)
popped3 = guests.pop(0)
popped4 = guests.pop(0)

popped_guests = [popped1, popped2, popped3, popped4]
for popped_guest in popped_guests:
    print(f"We're sorry you couldn't attend the dinner, {popped_guest}.")

print()

print(f"You're still invited to dinner, {guests[0]}!")
print(f"You're still invited to dinner, {guests[1]}!")

del guests[0]
del guests[0]

print()
print(guests)
