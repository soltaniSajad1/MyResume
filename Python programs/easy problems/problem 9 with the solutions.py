# make a table of users data number

userInputNumber = int(input("Please enter a number : "))
print('your entered ' + str(userInputNumber))

for i in range(1, 11):
    print(str(i) + " x " + str(userInputNumber) + " = " + str(i * userInputNumber))


# make a 2 table of users data numer

userNumber = int(input("enter your nummber again : "))
print('you entered ' + str(userNumber))

for i in range(1, 11):
    print(str(i) + " x " + str(userNumber) + " = " + str(i * userNumber))

print("\n \n \n")
for j in range(50, 60):
    print(str(j) + " / " + str(userNumber) + " = " + str(j / userNumber))