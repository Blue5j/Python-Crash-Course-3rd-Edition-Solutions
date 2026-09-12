locations = ["Japan", "China", "Russia", "Germany", "Turkey"]

print(locations)
print()

print("Alphabetically Sorted:")
print(sorted(locations))
print()

print("Original List:")
print(locations)
print()

print("Reverse Alphabetically Sorted:")
print(sorted(locations, reverse=True))
print()

print("Original List:")
print(locations)
print()

locations.reverse()
print("Reversed List:")
print(locations)
print()

locations.reverse()
print("Original List:")
print(locations)
print()

locations.sort()
print("Alphabetically Sorted:")
print(locations)
print()

locations.sort(reverse=True)
print("Reverse Alphabetically Sorted:")
print(locations)
