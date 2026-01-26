## If Statement
# a = int(input("Enter the number= "))
a = 5

if a >= 100:
    print("A")
elif a > 10:
    print("B")
elif a <= 0:
    print("C")
else:
    print("D")


b = "K"

if b =="Y":
    print("Yes")
else:
    print("No")


c = False

if c:
    print("Correct")
else:
    print("Not Correct")

"-------------------------------------------------"
print("-------------------------------------------------")

## for Loop
for x1 in range(1,11):
    print(x1)

for x2 in reversed(range(1,11)):
    print(x2)

for x3 in range(1,11,2):
    print(x3)

card = "1234-5678-9012-3456"
for x4 in card:
    print(x4)

for x5 in range(1,21):
    if x5==13:
        continue
    else:
        print(x5)

for x6 in range(1,21):
    if x6==13:
        break
    else:
        print(x6)


"-------------------------------------------------"
print("-------------------------------------------------")

## while Loop == condition remains True

name = input("Enter your name = ")

# if name == "":
#     print("You did not enter your name!!")
# else:
#     print(f"Your Name is {name}")

while name == "":
    print("You did not enter your name!!")
    name = input("Enter your name = ") # retype for infinite loop

print(f"Your Name is {name}")



num = int(input("Enter a number between 1-10 = "))

while num <1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10 = "))

print(f"Your number is {num}")



age = -2

while age <0:
    print("Enter your age again!")
    age = int(input("Enter your age ="))

print(f"You are {age} years old")



food = input("Enter a food you like (or q) = ")

# while food == "q":
#     print("Bye!")
#     food = input("Enter a food you like = ")

# print(f"You like {food}")    

while not food =="q":
    print(f"You like {food}")
    food = input("Enter a food you like (or q) = ")

print("Bye!")

