#Adventure game by LEGHASRE
#Define a function to start the quiz, which receives the username value to begin the quiz.
def player():
    #Greet the player and ask if they are ready to start.
    name = input("Enter your name: ")  # Input name
    print(f"𝓗𝓮𝓵𝓵𝓸,{name}")#{} are used to insert the value of the variable name directly into the string.So, {name} gets replaced by whatever value is stored in the name variable at that moment
    print("ωᥱℓᥴ𐐫꧑ᥱ to begin the adventure ! 🌈")  # Greeting message
    return name 

def play_game_1(name):
    #Play game 1 of the quiz
    print("\nYour adventure begins here,", name)  
    print("You are a brave traveler who has entered the *Enchanted Forest*, a place filled with mystical creatures and hidden secrets.")
    print("Legends say that deep within the forest lies a *hidden treasure*, but only those who prove their intelligence can claim it!")
    print("To move forward, you must pass the trial of Luna, the Guardian of the Forest! Answer wisely to proceed, but fear not to be fear! Even if you fail, you may still find your way out of the forest.")

    # Briefing about the adventure
    print("\n🌲 Suddenly, a glowing mist swirls around you... From the shadows, a great tiger emerges! 🌲")
    print(f"Talking Animal🐯: 'Greetings, {name}! I am *Luna, the Guardian of the Forest*. No one passes through without proving their wisdom!'")# "f" lets us insert variables into the string.
    print("Luna🐯: 'Are you prepared for my challenge? Only the cleverest may reach the treasure!'")

    start = input("Yes or No:? ").lower()
    if start != "yes":
        print("꧁ᬊBye see u soonᬊ᭄꧂")
        sys.exit()  # Properly exit the program

    # Question 1
    Q1 = "\n First Challenge: Which vegetable is known to make people cry when they cut it?"
    print(Q1)
    A1 = input("Answer: ").lower()
    if A1 == "onion":
        print("Luna🐯: Correct! The onion’s🧅 spell of tears has no effect on you. Impressive! 💯 ✅")
    else:
        print("Luna🐯: Wrong! The answer is onion 🧅. The enchanted mist grows thicker around you... ❌")
        print("Luna🐯:Oh no you made a mistake!But it's okay u have two chances left.")

    # Question 2
    Q2 = "\n Second Challenge: Is a tomato 🍅 a fruit or vegetable?"
    print(Q2)
    A2 = input("Answer: ").lower()
    if A2 == "fruit":
       print("Luna🐯: Correct! You see through the illusion of the tomato. You truly have the mind of a great explorer! 💯 ✅")
    else:
        print("Luna🐯: Wrong again! A tomato 🍅 is a fruit. Beware, traveler—the vines of the forest grow restless... ❌")

    # Question 3
    Q3 = "\n Final Challenge: What breakfast food is often served with maple syrup and butter?" 
    print(Q3)
    A3 = input("Answer: ").lower()
    if A3 == "pancake":
        print("Luna🐯: Spot on! Pancakes 🥞 are a feast worthy of heroes. You are truly one step closer to greatness! 💯 ✅ ")
    else:
        print("Luna🐯: 'Oh no! The answer is pancake 🥞. The forest watches your every move... ❌'")
        print("Luna🐯: 'Oh u lost the challenge but its okay you still wil be rewarded 😊.")
    
    print("\n✨ Luna steps back, and the mist clears. A golden path appears before you... ✨")
    print(f"Luna🐯: You have completed my trial, {name}. The *hidden treasure of the Enchanted Forest* is now within your reach!")

def end_game(name):
    #Display the end game message.
    input(f"꧁ᬊFarewell, {name}ᬊ᭄꧂! The forest whispers you {name}, for you have conquered its challenge. Until next time! 👋😊 ")

def main():
    name = player()
    play_game_1(name)
    end_game(name)

if __name__ == "__main__":
    main()
