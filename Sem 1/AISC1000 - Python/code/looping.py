age = 1

while(age < 10):
    print(age)
    age+=1

# Cal comm rate in loop
keep_going = 'y'
while(keep_going == 'y'):
    sales       = int(input("I/P sales: "))
    comm_rate   = float(input("I/P commision rate: "))
    print(f'Commision rate: ', (sales*comm_rate))
    keep_going = input("Keep going? (Y/N): ")


# Cal sum until a non numeric is inputed
num   = input("I/P numerics: ")
sum   = 0
while(num.isnumeric()):
    sum += int(num)
    num   = input("I/P numerics: ")
print(sum)