print("================================")
print("          THE LAST CLUE")
print("     MYSTERY DETECTIVE GAME")
print("================================")

name = input("\nEnter detective name: ")

print("\nWelcome Detective", name)

print("\n1. Start Investigation")
print("2. Instructions")
print("3. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    def room1():
    print("\n================================")
    print("       ROOM 1: CRIME SCENE")
    print("================================")

    print("\nA mysterious crime has occurred.")
    print("You find a locked drawer.")

    print("\nRiddle:")
    print("I have keys but no locks.")
    print("I have space but no room.")
    print("What am I?")

    answer = input("\nYour answer: ")

    if answer.lower() == "keyboard":
        print("\nCorrect! You found your first clue.")
    else:
        print("\nIncorrect! Try again next time.")

elif choice == "2":
    print("\nSolve puzzles and collect clues.")

elif choice == "3":
    print("\nGoodbye Detective!")

else:
    print("\nInvalid choice!")
