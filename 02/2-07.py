# 2-7. Stripping Names: Use a variable to represent a person's name, and include some whitespaces characters at the beginning and end of the name. Make sure you use each character combination "/t" and "/n" at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name = "\tAbdullah\n"
print(name)
name = name.rstrip()
name = name.lstrip()
name = name.strip()
print(name)
