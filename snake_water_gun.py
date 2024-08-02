import random

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        return "You win!"
    else:
        return "You lose!"

def main(): 
    print("Welcome to Snake, Water, Gun!")
    user_choice = input("Enter your choice (snake, water, gun): ").lower()

    if user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice! Please choose either snake, water, or gun.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
