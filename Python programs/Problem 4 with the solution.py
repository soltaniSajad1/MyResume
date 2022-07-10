# take an age from the user and check if user is grown enough to participate in the voting
# if NOT, It will calculate the reamin age until the user can make a participation in the voting


userAgeInput = int(input("How old are you? "))
remain_aged = 0

if userAgeInput < 18:
    remain_aged = 18 - userAgeInput
    print("Sorry! You can not participate in the voting, you will be able to participate after ", remain_aged, " years!")
elif userAgeInput >= 18:
    print("You are allowed to participate in the voting.")


# take marks from the user and check if user is able to admission in College 

userMarksInput = int(input("what is your mark? "))
remain_marks = 0
if userMarksInput >= 60:
    print("you can admit in the college")
elif userMarksInput < 60:
    remain_marks = 60 - userMarksInput
    print("sory! you can not admit in the college. you need more ", remain_marks, " marks for admission.")
