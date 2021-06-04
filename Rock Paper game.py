import time
print("Made by kavin")
print("*"*50)

# "Account Setup")
v=input("Enter your user name:   ")
h=input("Enter the password:     ")
c=input("Confirm your password:  ")
time.sleep(0.5)
print("Loading..")
print("Account Created")
print("_"*50)
print('\033[1m')
print("Welcome to the Game:")
print("Rock Paper Scissor",end="\n ")
print('\033[0m')
print("_" * 50)
time.sleep(1)
print("Loading.")
time.sleep(1)
print("Loading..")
time.sleep(1)
print("Loading...")

print("_"*2,end='')
time.sleep(1)
print("_"*48)

life=5
score=0
comp_life=5
import random
while True:
    print("_"*50)
    print("\nCHOICES\nrock \npaper\nscissors\nquit")
    user_action = input("Enter a choice: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action=='quit':
        break
    elif user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    elif user_action=='quit':
        break
print("#"*50)
print("Thank You")
print("You are not a child to play this game... Go and study you ****")


