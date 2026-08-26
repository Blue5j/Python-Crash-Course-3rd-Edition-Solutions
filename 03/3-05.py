# 3-5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitatations. You'll have to think of someone else to invite.
#   * Start with the program from Exercise 3-4. Add a `print()` call at the end of the program stating the name of the guest who can't make it.
#   * Modify your list, replacing the name of the guest who can't make it with the name of the new person you're inviting.
#   * Print a second set of invitation messages, one for each person who is still in your list.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

guests = ['Shaheer', 'Ayan', 'Ghous']

print(f"Hello, {guests[0]}! You are invited to dinner at my house!")
print(f"Hello, {guests[1]}! You are invited to dinner at my house!")
print(f"Hello, {guests[2]}! You are invited to dinner at my house!")

print(f"\nSorry everyone, {guests[2]} couldn't make it to the dinner.")

del guests[2]
guests.append('Yahya')
print()

print(f"Hello, {guests[0]}! You are invited to dinner at my house!")
print(f"Hello, {guests[1]}! You are invited to dinner at my house!")
print(f"Hello, {guests[2]}! You are invited to dinner at my house!")
