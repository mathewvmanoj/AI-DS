age = float(input("I/P your age:"))
while age <= 0 or age > 200:
    print("Invalid")
    age = float(input("I/P your age:"))
print("Valid age = ", age)