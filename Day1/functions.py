#Basic Function

def greet_user(name):
    print(f"Welcome, {name}!")

greet_user("Arjun")

print("------------------")
#Return Values

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)
print("------------------")

#Default Arguments

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

#Calling without second argument
describe_pet("Buddy")

#Calling with second argument,
describe_pet("Whiskers", "cat")

print("------------------")
#Using *args

def sum_all(*args):
    return sum(args)

total = sum_all(1, 2, 3, 4, 5)
print("Total Sum:", total)
print("------------------")
#Using **kwargs

def build_profile(first_name, last_name, **kwargs):
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }
    profile.update(kwargs)
    print(profile)

build_profile("Arjun", "M S", location="Kerala", job="Developer")

print("------------------")
#Scope Challenge

count = 0   # Global variable

def update_count():
    global count   # Allows modifying global variable
    count += 1
    print("Updated Count:", count)

update_count()
# Explanation:
# Without 'global', Python treats 'count' as local inside function.
# Using 'global' allows modifying the global variable.