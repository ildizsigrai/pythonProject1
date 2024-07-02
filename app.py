# input function
name = input("What is your name? ")
print("hello " + name)

birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print("Age: ", age)

# type conversions // CALCULATOR
first = float(input("first:"))
second = float(input("second: "))
sum = first + second
print("sum", str(sum))

# STRINGS
learn = "Python basics."

print(learn.capitalize())
print(learn.upper())
print(learn.replace('.', '!'))
print('Python' in learn) #true

# IF STATEMENTS
temperature = 8

if temperature > 20:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 10:
    print("It is a nice day")
elif temperature < 10:
    print("It's a cold day")
print("done")

# practice -- unit conversion
weight = float(input("Weight: "))
unit = input("(k)g or (l)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

# WHILE LOOP
i = 1
while i <= 10:
    print(i * '*')
    i = i + 1
print("done")

# LISTS
letters = ["X", "Y", "Z"]
letters[0] = "A"
print(letters[0:3])