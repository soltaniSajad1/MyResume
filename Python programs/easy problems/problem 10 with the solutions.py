# get 6 subject number from the user and calculate the average and total of the numbers and print it.


from numpy import average


user = []

while len(user) != 6:
    userInput = int(input("enter a number : "))
    user.append(userInput)

print("your list is ", user)
print("the total number of the list is ", sum(user))
print("the average number of the list is ", average(user))

# get 6 subject number from the user and calculate percentage the numbers and print it.
res = (len([ele for ele in user if ele > 0])) / len(user) * 100

print('answer is ' + str(res))