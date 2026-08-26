# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

countries = ['Pakistan', 'Japan', 'Russia']
print(countries)

print(len(countries))

countries.append('Iran')
print(countries)

countries.insert(1, 'India')
print(countries)

countries.remove('Russia')
print(countries)

popped_country = countries.pop(0)
print(countries)

countries.sort()
print(countries)

countries.reverse()
print(countries)
