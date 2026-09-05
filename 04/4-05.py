# 4-5. Summing a Million: Make a list of numbers from one to one million, and then use min() and max() to make sure the list starts at one and ends at one million. Also, use the sum() function to see how quiclkly Python can add a million numbers.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

one_million = [i for i in range(1, 1000_001)]

print(min(one_million))
print(max(one_million))
print()

print(sum(one_million))
