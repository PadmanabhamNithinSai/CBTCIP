import random
import time

def print_title():
    print("=" * 60)
    print("🎮 ROCK PAPER SCISSORS GAME 🎮".center(60))
    print("=" * 60)
    print("Winning Rules:")
    print("➡ Rock vs Paper 📝 → Paper wins")
    print("➡ Rock vs Scissors ✂️ → Rock wins")
    print("➡ Paper vs Scissors ✂️ → Scissors wins")
    print("=" * 60)

def get_user_choice():
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    while True:
        try:
            user_input = int(input("Choose Rock (1), Paper (2), or Scissors (3): ").strip())
            if user_input in choices:
                return choices[user_input]
            else:
                print("❌ Invalid input. Please type 1 for Rock, 2 for Paper, or 3 for Scissors.")
        except ValueError:
            print("❌ Invalid input. Please enter a number (1, 2, or 3).")

def get_winner(player, computer):
    player = player.lower()
    computer = computer.lower()
    if player == computer:
        return "draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

def smart_computer_choice(player_choice):
    options = ["rock", "paper", "scissors"]
    options.remove(player_choice)
    return random.choice(options)

def play_round():
    player = get_user_choice()
    if random.random() < 0.2: 
        computer = player
    else:
        computer = smart_computer_choice(player)

    print(f"\nYou chose: {player.capitalize()}")
    time.sleep(0.5)
    print(f"Computer chose: {computer.capitalize()}")
    time.sleep(0.5)

    winner = get_winner(player, computer)
    if winner == "draw":
        print("🤝 It's a draw!")
    elif winner == "player":
        print("🎉 You win this round!")
    else:
        print("💻 Computer wins this round!")
    return winner

def ask_to_play_again():
    while True:
        response = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        print("❌ Invalid input. Please type 'yes' or 'no'.")

def main():
    print_title()
    rounds = 0
    player_score = 0
    computer_score = 0

    while True:
        rounds += 1
        print(f"\n--- ROUND {rounds} ---")
        result = play_round()

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"📊 Score → You: {player_score} | Computer: {computer_score}")

        if not ask_to_play_again():
            break

    print("\n" + "=" * 60)
    print("🏁 GAME OVER".center(60))
    print("=" * 60)
    print(f"Final Score → You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("🏆 Congratulations! You won the game!")
    elif player_score < computer_score:
        print("😞 You lost the game. Better luck next time!")
    else:
        print("🤝 It's a tie!")

if __name__ == "__main__":
    main()
