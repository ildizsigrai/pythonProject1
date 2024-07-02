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