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
