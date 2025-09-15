# Ask user for their names, then remove spaces left and right and finally make the 1st letter of each word capital
name = input("What's your name? ").strip().title()

# Say hello to the user but using FORMATTED STRINGS
print(f"hello, {name}")
