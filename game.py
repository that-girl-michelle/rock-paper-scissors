import random

userChoice = input("Choose rock, paper or scissors: ")
while userChoice != "rock" and userChoice != "paper" and userChoice != "scissors":
    print("No monkey business!\n")
    userChoice = input("Choose rock, paper or scissors: ")

computerActions = ["rock", "paper", "scissors"]
computerChoice = random.choice(computerActions)

print(f"Computer chose {computerChoice}. You chose {userChoice}.\n")

if computerChoice == userChoice:
    print(f"Both of you chose {userChoice}. It's a draw!")

elif userChoice == "rock":
    if computerChoice == "paper":
        print("Paper wrapped rock. You lost, you fool!")
    else:
        print("Rock destroyed scissors. You won, good job!")

elif userChoice == "paper":
    if computerChoice == "rock":
        print("Paper wrapped rock. You won, congratulations!")
    else:
        print("Scissors cut paper. You lost, be ashamed!")

elif computerChoice == "rock": #user chose scissors
    print("Rock destroyed scissors. You lost, idiot!")
else: #user chose scissors, computer chose paper
    print("Scissors cut paper. You won, have some rum! (unless you are underage)")