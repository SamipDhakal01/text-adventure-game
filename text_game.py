import sys
import random
# This adds a code that when executed exits the program and ends it.

def user_input(prompt):
    user_choice = input(prompt)
    cleaned_choice = user_choice.strip()
    if cleaned_choice == "q" or cleaned_choice == "quit":
        print('Thank you for playing; GoodBye!')
        sys.exit()
    return cleaned_choice

# I have made the levels bellow, and now I just need to call them, for it to exit.

def level_1(inventory):
    print("Welcome to level 1")
    print()
    print("There are 2 doors one on your left and one on your right")
    print()
    while True:
        part_1 = user_input("Which one do you choose? ").lower()
        if part_1 == "left":
            print("You walk inside and see a sword and a door past it.")
            print()
            break
        elif part_1 == "right":
            print("There was a bridge, and when you tried to walk you fell and died.")
            print()
            print("Please restart; To restart press run!")
            return "died", inventory
        else:
            print("Sorry that's not valid!")
            print()
    while True:
        sword = user_input("Would you like to take the sword? ").lower()
        if sword == "yes":
            inventory.append('Sword')
            print("The sword is in your inventory!")
            print()
            break
        elif sword == "no":
            break
        else:
            print("Sorry that's not a valid input!")
    print("You walk through the door!")
    print("Inside you see a monster")
    print()

    if "Sword" in inventory:
        print("You pull out your sword to fight and defeat the monster.")
        print()
        print("You completed level 1")
        print()
        return "passed", inventory
    else:
        print("The monster kills you because you didn't pick up the sword.")
        return "died", inventory
def level_2(inventory, doors):
    print("Welcome to Level 2")
    print()
    print("You walk through a portal where it takes you to a room with multiple doors!")
    while True:
        part_2 = user_input(f"There are multiple doors in front of you which one do you choose {doors}?: ").lower()
        if part_2 == "red":
            if "red" in doors:
                print("You walk through and there was a tiger, which you defeated")
                print("You walk back out and choose a different door!")
                print()
                doors.remove("red")
            else:
                print("You already chose red and defeated the tiger please choose a different door!")
                print()
        elif part_2 == "green":
            print("You chose the correct door, Welcome to the next level!")
            return "passed", inventory
        elif part_2 == "blue":
            print("You open the door and a trap of arrows kills you!")
            print("Please restart; To restart please press run!")
            return "died", inventory
        elif part_2 == "yellow":
            if "yellow" in doors:
                print("You try to open the door but it wont budge.")
                print("You walk back to the center of the room!")
                print()
                doors.remove("yellow")
            else:
                print("The door still wont budge choose a different door!")
                print()

def level_3(inventory):
        print()
        print()
        print("Welcome to level 3!")
        print()

        while True:
            print("When you enter level 3 you see 2 weapons, and a door. (Bow and arrows + Spear)")
            weapon_two = user_input("Would you like to take the weapons?: ").lower()
            if weapon_two == "yes":
                print("You take the weapons and continue to the next room.")
                print()
                inventory.append("Bow and arrows")
                inventory.append("Spear")
                break
            elif weapon_two == "no":
                print("You move on without the weapons!")
                break
            else:
                print("Sorry that's not valid!")
        print()
        print("Once you walk through the door, you see 2 bridges.")
        print('The left bridge looks rusty and old, while the right one looks new.')
        while True:
            part_3 = user_input("Which bridge do you choose?: ").lower()
            if part_3 == "left":
                print("You walk halfway and the bridge starts shaking violently.")
                while True:
                    part_3_5 = user_input('The bridge is still shaking do you wish to go back or continue?(Continue or Back): ').lower()
                    if part_3_5 == "continue":
                        print("You continue and barely make it to the other side.")
                        print()
                        print("When you make it to the other side you see a door.")
                        print("You walk through the door, and see a portal.")
                        print()
                        print("You walk through the portal.")
                        print()
                        print()
                        print()
                        print("You completed level 3")
                        return "passed", inventory

                    elif part_3_5 == "back":
                        break

                    else:
                        print("Sorry that's not valid!")
                        continue


            elif part_3 == "right":
                print("You walk through the bridge without any problems.")
                print()
                print("On the other side you see a door.")
                print("You walk through the door, and see a portal.")
                print()
                print("You walk through the portal.")
                print()
                print()
                print()
                print("You completed level 3")
                return "passed", inventory
            else:
                print("Sorry that's not valid!")
                continue
def level_4(inventory):
    print()
    print()
    print("Welcome to Level 4! ")
    print("In front of you, there is a locked vault.")
    print("Beside the vault are three levers. There is also text, match the levers in the correct order to open the vault")
    print("Type a combination of (1,2,3) in different orders to try and open the vault. You only get 3 tries!!")
    attempts = 0
    correct_answer = 213
    while attempts < 3:
        try:
            combination = int(user_input("Enter the code!: "))
            if combination == correct_answer:
                print("Good Job you got it correct! ")
                print()
                print("The vault door opens and you walk inside. ")
                print("Inside the vault there is a door with a place to put a spear. ")
                if "Spear" in inventory:
                    print()
                    print("You put the spear in the place which opens the door!")
                    print()
                    print("You walk inside! ")
                    print()
                    print("You completed level 4! ")
                    inventory.remove("Spear")
                    return "passed", inventory
                else:
                    print()
                    print()
                    print("Sorry you did not have the spear in your inventory! ")
                    print("You were stuck and died of hunger! ")
                    return "died", inventory
            else:
                print("Sorry that's not the right code! ")
                attempts += 1
        except ValueError:
            print("Sorry that's not a valid code!! ")
    print("You ran out of guesses! ")
    return "died", inventory
number = random.randint(0, 100)

def level_5(inventory, endings, number, player_name):
    print()
    print()
    print("Welcome to the FINAL LEVEL!! (5) ")
    print()
    print("Hope you finish the game, good luck!!")
    print()
    print()
    print("Once you are inside the room, the door closes behind you and it locks you in. ")
    while True:
        inventory_check = user_input("Press I or i to check your inventory before the finale!: ")
        if inventory_check == "I" or inventory_check == "i":
            print(f'This is your inventory, {inventory} !')
            break
        else:
            print("Sorry that's not valid! ")

    print()
    print()
    print("You start looking around the room.")
    print("You see a door to your right and start walking up to it.")
    print("...")
    print("You hear footsteps...")
    print()
    print("[ERROR: ENTITY CANT BE DESCRIBED!!]")
    print()
    print("You start backing up from the door. ")
    print()
    print("The door opens and you see...")
    print("A person like figure made out of light stands in front of you. ")
    print()
    print()
    print()
    print("ERROR: ""Hello, human welcome to the final level!")
    print("ERROR: I am the creator of this game; hope you have enjoyed it so far. ")
    print()
    print("There are multiple endings to this game!")
    print(f"These are the available endings, {endings}")
    print()
    while True:
        endings_choice = (user_input("What ending do you desire to seek? "))
        if endings_choice == "1" or endings_choice == "2" or endings_choice == "3":
            break
        else:
            print("Sorry that's not valid! ")

    while endings_choice == "1":
        print("Welcome to ending 1, hope you chose the right one! ")
        print()
        print("I am thinking of a random number (0-100) you have to guess it! GOOD LUCK!!")
        attempts_finale = 0
        while attempts_finale < 10:
            try:
                guess = int(user_input("What is your guess?: "))
                if guess == number:
                    print("You guessed correct! ")
                    print()
                    print("Final level completed! ")
                    print('You have completed all the levels!')
                    print()
                    print(f"Thank you for playing, {player_name} ")
                    print()
                    print("YOU DID ITTTTTTTTTTTT")
                    return "passed", inventory
                elif guess < 0 or guess > 100:
                    print("Sorry guess numbers from 0-100")
                elif guess <= number:
                    print('Sorry to low! ')
                    print(f"TOTAL ATTEMPTS: {attempts_finale}")
                    attempts_finale += 1
                elif guess >= number:
                    print("Sorry to high! ")
                    attempts_finale += 1
                    print(f"TOTAL ATTEMPTS: {attempts_finale}")

            except ValueError:
                print("Sorry that's not valid! ")
        print("You ran out of guesses! The mystery number slips away forever.")
        return "died", inventory
    while endings_choice == "2":
        print("Welcome to ending choice 2! ")
        print("You have been teleported to a room with a 3 headed hydra snake. ")
        print()
        print()
        choice = user_input("Do you wish to fight with your bow or sword! ").lower()
        if choice == "bow":
            print("You start shooting arrows at the hydra. ")
            print()
            print()
            print("You keep shooting arrows. ")
            print()
            print()
            print('You have 10 arrows left and only one head is down.')
            print("You have one arrow left and only one head down. ")
            print("You start fighting with your sword.")
            print()
            print('You are tired because you have been evading the hydra for an hour now.')
            print('YOU DIED')
            print()
            print("SO CLOSE TRY AGAIN; PS, the random number is RANDOM")
            return 'died', inventory
        elif choice == "sword":
            print("You pull out your sword out to fight. ")
            print("The hydra cuts your left wrist...")
            print("Luckily your right handed :) ")
            print()
            print("You keep fighting, do you wish to use your bow as well? ")
            choice_2 = user_input("DO YOU WISH TO USE YOUR BOW AS WELL? (Yes, No): ").lower()
            if choice_2 == 'yes':
                print('You start swapping your weapons to fight.')
                print("In the end you die :(")
                print()
                print()
                print('JOKINGGGGG YOU BEAT THE HYDRAAAAAAA ')
                print(" YOU BEAT THE FINAL LEVEL")
                print(f"THANKS FOR PLAYING, {player_name} ")
                return "passed", inventory
            elif choice_2 == "no":
                print("You choose not to swap your wepons out.")
                print()
                print()
                print("You keep going but the hydra grabs you and eats you.")
                print()
                print("You DIE")
                return 'died', inventory
            else:
                print("Sorry that's not valid! ")
        else:
            print("Sorry that's not valid! ")
    while endings_choice == "3":
        print()
        print("You chose the right ending?  ")
        print()
        print()
        print()
        print()
        while True:
            print("You have 2 doors in front of you. (left, right) ")
            part_5 = user_input("Which one do you choose? ").lower()
            if part_5 == "left":
                print("You walk inside and you see ERROR again.")
                print()
                print("ERROR: CONGRATS ON PASSING THE FINAL LEVEL")
                print("ERROR: YOU HAVE BEATEN THE GAME")
                print(f"ERROR: Thanks for playing, {player_name}. ")
                return "passed", inventory
            elif part_5 == "right":
                print("There was a bridge again, and when you tried to walk past it?")
                print("Guess what happened? ")
                right = user_input("DID YOU DIE OR LIVE?: ").lower()
                if right == "die":
                    print("Wrong, you actually lived!!! ")
                    print("You walk inside and you see ERROR again.")
                    print()
                    print("ERROR: CONGRATS ON PASSING THE FINAL LEVEL")
                    print("ERROR: YOU HAVE BEATEN THE GAME")
                    print(f"ERROR: Thanks for playing, {player_name}. ")
                    return "passed", inventory
                elif right == "live":
                    print("RIGHT YOU LIVEDDDDD.")
                    print("Theres a door AGAINNNN. ")
                    print("You walk inside and you see ERROR again.")
                    print()
                    print("ERROR: CONGRATS ON PASSING THE FINAL LEVEL")
                    print("ERROR: YOU HAVE BEATEN THE GAME")
                    print(f"ERROR: Thanks for playing, {player_name}. ")
                    return "passed", inventory

            else:
                print("Sorry that's not valid!")
                print()
print("Welcome to the fictional adventure game!!")
print("In this game your decisions decide your fate.")
print()
print("Enter q to quit!")
player_name = user_input("WHAT IS YOUR PLAYERS NAME?: ")
levels = [1, 2, 3, 4, 5]
endings = [1, 2, 3]
inventory = []
doors = ["red", "green", "blue", "yellow"]
print("These are the levels", levels)

# THE CODES BELOW RUN THE LEVELS #
result, inventory = level_1(inventory)
if result == "died":
    sys.exit()
result, inventory = level_2(inventory, doors)
if result == "died":
    sys.exit()
result, inventory = level_3(inventory)
if result == "died":
    sys.exit()
result, inventory = level_4(inventory)
if result == "died":
    sys.exit()
result, inventory = level_5(inventory, endings, number, player_name)
if result == "died":
    sys.exit()
