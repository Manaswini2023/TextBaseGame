import time

# Global variable to store the player's score
player_score = 0

def introduction():
    print("Welcome to the Quest for the Legendary Treasure!")
    print("You find yourself in the mystical land of Eldoria, known for its magic and mysteries.")
    print("Your goal is to embark on a perilous journey to find the legendary treasure hidden deep within the Eldorian Forest.")
    print("Be cautious, as your decisions will shape your destiny!\n")

def make_choice(choices):
    print("Options:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("\nInvalid choice. Please enter a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

def eldorian_forest():
    global player_score
    print("\nYou enter the Eldorian Forest, a place shrouded in mystery.")
    time.sleep(2)
    print("As you venture deeper, you encounter a magical creature blocking your path.")

    choices = ["Attempt to communicate with the creature.", "Find a detour around the creature."]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou attempt to communicate with the creature using a friendly tone.")
        time.sleep(2)
        print("The creature responds positively and reveals a shortcut through the forest.")
        time.sleep(2)
        print("You continue your journey with the creature's guidance.")
        player_score += 10
    else:
        print("\nYou decide to find a detour around the creature.")
        time.sleep(2)
        print("While navigating the detour, you discover a hidden cave.")

        # Puzzle - Magical Stones
        print("You find a clearing with three magical stones. Each stone has a symbol engraved on it.")
        print("Choose the correct stone to proceed:")

        # Correct stone: Stone with symbol 2
        correct_stone = 2
        choices = [1, 2, 3]
        choice = make_choice(choices)

        if choice == correct_stone:
            print("\nThe magical stones glow with energy, and a path opens before you.")
            player_score += 15
        else:
            print("\nThe magical stones react negatively, and you face a magical barrier. Try again.")
            eldorian_forest()  # Restart the forest scenario

    # Additional decision point
    choices = ["Help a lost traveler.", "Ignore the traveler and continue."]
    print("\nWhile on your journey, you encounter a lost traveler.")
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou decide to help the lost traveler. They are grateful and share valuable information.")
        player_score += 15
    else:
        print("\nYou ignore the traveler and continue your journey.")

def treasure_chamber():
    global player_score
    print("\nAfter overcoming various challenges, you arrive at the entrance of the treasure chamber.")
    time.sleep(2)
    print("However, the chamber is guarded by a mystical guardian.")

    # Challenge - Confronting the Guardian
    print("\nYou must confront the guardian in a battle to reach the treasure.")
    print("Prepare yourself for the challenge!")

    # Player's combat skill (random value for simplicity)
    player_combat_skill = 15
    guardian_combat_skill = 20  # Guardian's combat skill (random value for simplicity)

    if player_combat_skill >= guardian_combat_skill:
        print("You successfully defeat the guardian in a fierce battle.")
        player_score += 25
    else:
        print("The guardian is powerful, and despite your efforts, you are unable to defeat it. Game over.")
        game_over()

    # Display different endings based on the player's score
    print("\nYour quest concludes.")
    if player_score >= 60:
        print("Congratulations! You've achieved the highest score and become a legendary adventurer!")
    elif player_score >= 30:
        print("You've successfully completed the quest and found the legendary treasure.")
    else:
        print("Though your journey was challenging, you couldn't find the legendary treasure. Better luck next time!")

def game_over():
    print("\nGame over. Your quest ends here. Better luck next time!")
    exit()

def main():
    introduction()
    eldorian_forest()
    treasure_chamber()

if __name__ == "__main__":
    main()
