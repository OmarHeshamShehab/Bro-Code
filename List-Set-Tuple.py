#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

utensils = {"fork", "spoon", "Knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)
dinner_table = dishes.union(utensils)
for i in utensils:
    print(i)
print(dishes.difference(utensils))

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))

capitals = {'Egypt': 'Cairo',
            'Russia': 'Moscow',
            'USA': 'Washington DC',
            'India': 'New Delhi'}
print(capitals['Egypt'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Germany': 'Berlin'})
for key, value in capitals.items():
    print(key, value)

def add(*args):
    sum_value = 0
    # we converted to list as we can change list but can't change tuple
    lista = list(args)
    lista[0] = -15
    for i in lista:
        sum_value += i
    print(sum_value)


add(1, 2, 3, 10)

def hello(**kwargs):
    print("Hello ", end="")
    for key, value in kwargs.items():
        print(value, end="")


hello(Title="Mr. ", Name="Omar Hesham", age=" you are 30 years old")

name = "omar"
age = 25
country = "Egypt"
height = 1.79

print("my name is %s ,and I am %d , my height is %.2f and i live in %s " % (name, age, height, country))

print("my name is {:s} and i am {:d} , my height is {:.2f} and i live in {:s} "
      .format(name, age, height, country))

print(f'my name is {name} and i am {age} , my height is {height} and I live in {country} ')


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! foolish!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
