## Function == a reuseable code, place () after the function name

# def happy_song():
#     print("Happy birthday to you!")
#     print("You are old")
#     print("Happy birthday to you")
#     print()

# happy_song()
# happy_song()
# happy_song()

def happy_song(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old")
    print("Happy birthday to you")
    print()

happy_song("Bob", 20)
happy_song("Steve", 30)
happy_song("Joe", 40)


print("-------------------------------------------------")

def invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount} is due : {due_date}")

invoice("Broco", 42.50, "01/01")
invoice("Joey", 100.05, "01/02")


print("-------------------------------------------------")

def add(x,y):
    z = x+y
    return z

def subtract(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z

print(add(1,2))
print("Add number =" ,add(1,2))
print("Subtract number =" ,subtract(1,2))
print("Multiply number =" ,multiply(1,2))
print("Divide number =" ,divide(1,2))


print("-------------------------------------------------")

def create_name(first, last):
    first = first.capitalize()  #first = first
    last = last.capitalize()    #last = last
    full_name = first +" "+ last
    return full_name

a1 = create_name("bob", "code")
a2 = create_name("christ", "bennot")

print(a1)
print(a2)
