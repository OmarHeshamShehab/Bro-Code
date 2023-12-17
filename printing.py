first_name = "omar"
print(type(first_name))

name, age, attractive = "omar", 30, True
print(name)
print(age)
print(attractive)

omar = batoul = sayed = 30
import tkinter.messagebox

name = "omar"

print(len(name))
print(name.find("r"))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("r", "R"))
print(name * 3)

full_name = "omar hesham"
first_name = full_name[:5]
print(first_name)
last_name = full_name[5:]
print(last_name)
reversed_name = full_name[::-1]
print(reversed_name)

website1 = "https://www.google.com/"
website2 = "https://www.yahoo.com/"
slicing = slice(12, -5)
print(website1[slicing])
print(website2[slicing])


# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# —---------------------
#   EXAMPLE 1
# —---------------------
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ sign up")
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(5)

rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = input("enter desired symbol: ")
#
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

while True:
    name = input("enter your name")
    if name != "":
        break

Phone_Number = "012-345-6789"

for x in Phone_Number:
    if x == "-":
        continue
    print(x, end="")

for i in range(1, 10):
    if i == 4:
        pass
    else:
        print(i)
