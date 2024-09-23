import random

choice = input('What do you choose? Type "R" for Rock, "P" for Paper or "S" for Scissors: ').upper()

computer = random.randint(0,2)

if choice == "R":
    print("Your choice = ROCK")
    if computer == 0:
        print("Computer's choice = ROCK. It's a Draw! - Try Again.")
    if computer == 1:
        print("Computer's choice = PAPER. You Lose!")
    if computer == 2:
        print("Computer's choice = SCISSORS. You Win!")
elif choice == "P":
    print("Your choice = PAPER")
    if computer == 0:
        print("Computer's choice = ROCK. You Win!")
    if computer == 1:
        print("Computer's choice = PAPER. It's a Draw! - Try Again.")
    if computer == 2:
        print("Computer's choice = SCISSORS. You Lose!")
elif choice == "S":
    print("Your choice = SCISSORS")
    if computer == 0:
        print("Computer's choice = ROCK. You Lose!")
    if computer == 1:
        print("Computer's choice = PAPER. You Win!")
    if computer == 2:
        print("Computer's choice = SCISSORS. It's a Draw! - Try Again.")
else:
    print("Please choose a valid option!")
