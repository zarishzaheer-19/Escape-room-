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
    print("\nYour investigation begins!")

elif choice == "2":
    print("\nSolve puzzles and collect clues.")

elif choice == "3":
    print("\nGoodbye Detective!")

else:
    print("\nInvalid choice!")
