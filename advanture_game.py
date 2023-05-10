# import the modules
import random
import time
# make variables
villains = ["Witch", "Dragon", "Pirate", "Gangaster", "Elf","Werewolf","Vampire"]
villain = random.choice(villains)
items = []
the_way = ""

# function to print then wait

def print_pause(massage):
    print(massage)
    time.sleep(0)
    
# the introduction

def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + villain +
                " is somewhere around here, and has been terrifying"
                " the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")

# if the player choice to go to house

def house():

    if "new sword" not in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a " + villain + ".")
        print_pause("Eep! This is the " + villain + "'s house!")
        print_pause("The " + villain + " attacks you!")
        print_pause("You feel a bit under-prepared for this, what "
                    "with only having a tiny dagger.")
        attack_unprepared = input("Would you like to (1) fight or (2) run"
                                  " away")
        if attack_unprepared == "1":
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the "+ villain + '.')
            print_pause("Game over,You have been defeated!")
            play_again()
        elif attack_unprepared == "2":
            print_pause("You run back into the field. Luckily,"
                        " you don't seem to have been followed.")
            the_way = input("Enter 1 to knock on the door of the house\n"
                            "Enter 2 to peer into the cave")
        else:
            house()
    elif "new sword" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a " + villain + ".")
        print_pause("Eep! This is the " + villain + "'s house!")
        print_pause("The" + villain + "attacks you!")
        attack_prepared = input("Would you like to (1) fight or (2) run away?")
        if attack_prepared == "1":
            print_pause("As the " + villain + " moves to attack, you unsheath"
                        " your new sword")
            print_pause("The " + villain + " slayer sword brightly in your"
                        " hand as you brace yourself for the attack.")
            print_pause("But the " + villain + " takes one look at your shiny"
                        " new toy and runs away!")
            print_pause("congratulation, You won!.You got rid of the"
                         + villain + ". You are victorious!")
            play_again()
        elif attack_prepared == "2":
            print_pause("You run back into the field. Luckily,"
                        " you don't seem to have been followed.")
            the_game()
        else:
            house()
            
# if the player choice to go to the cave

def cave():
    if "new sword" not in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the legendary " + villain + " slayer sword.")
        print_pause("You discard your silly old dagger and take"
                    " the sword with you.")
        items.append("new sword")

    elif "new sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the"
                    " good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        
# Ask the player if he want to play again

def play_again():
        again = input("would you like to play again? (Y/N)").lower()
        if again == "y":
            items.clear()
            villain = random.choice(villains)
            print_pause("Excellent! Restarting the game ...")
            main()
        elif again == "n":
            print_pause("Thanks for playing! See you next time.")
            import sys
            sys.exit()
        else:
            play_again()
            
# play the game

def the_game():
        the_way = input("Enter 1 to knock on the door of the house\n"
                        "Enter 2 to peer into the cave:")

        if the_way == "1":
            house()
            the_game()
        elif the_way == "2":
            cave()
            the_game()
        else:
            the_game()


def main():
    intro()
    the_game()

# calling the main function that run the game
main()
