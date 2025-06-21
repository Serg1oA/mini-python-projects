import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

def get_computer_choice():
    rand1to3 = random.randint(1, 3)
    if rand1to3 == 1:
        return ROCK
    elif rand1to3 == 2:
        return PAPER
    elif rand1to3 == 3:
        return SCISSORS

def get_user_choice():
    user_choice = ""
    while user_choice != ROCK and user_choice != PAPER and user_choice != SCISSORS:
        user_choice = input("Choose between rock, paper and scissors: ")
    return user_choice

def result_check(user, computer):
    VICTORY = "YOU WON, CONGRATS!"
    DEFEAT = "YOU LOST, TRY AGAIN!"
    if user == ROCK and computer == SCISSORS:
        print(VICTORY)
    elif user == SCISSORS and computer == PAPER:
        print(VICTORY)
    elif user == PAPER and computer == ROCK:
        print(VICTORY)
    else:
        print(DEFEAT)

def main():
    result_check(get_user_choice(), get_computer_choice())

main()