# nested if 

print("Rock , Paper , Scissors ")
player_1 = input("player_1 , make your move : ")
player_2 = input("player_2 , make your move : ")

if player_1 == player_2 :
    print("Tie")
elif player_1 == "Rock" :
    if player_2 == "Paper" :
        print("player_2 wins!")
    elif player_2 == "Scissors" :
        print("player_1 wins!")
    else :
        print("something went wrong.")
elif player_1 == "Paper" :
    if player_2 == "Rock" :
        print("player_1 wins!")
    elif player_2 == "Scissors" :
        print("player_2 wins!")
    else :
        print("something went wrong.")
elif player_1 == "Scissors" :
    if player_2 == "Rock" :
        print("player_2 wins!")
    elif player_2 == "Paper" :
        print("player_1 wins!")
    else :
        print("something went wrong.")
else :
    print("something went wrong.")
