# if condition

userScore = float(input("Please enter your score: "))

if userScore == 20 :
    print("You're the best student.")
elif 15 <= userScore < 20 :
    print("You're a good student.")
elif 10 <= userScore < 15 :
    print("You should try better.")
elif 0 <= userScore < 10 :
    print("You don't pass.")
else :
    print("You enter an invalid number.")