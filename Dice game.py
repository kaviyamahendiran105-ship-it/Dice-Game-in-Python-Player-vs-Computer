import random

print("Dice Game - Player vs Computer")

player_score = 0
computer_score = 0
rounds = 5

for round_num in range(1, rounds + 1):
    input("Round " + str(round_num) + " - Press Enter to roll dice...")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("Player rolled  :", player_roll)
    print("Computer rolled:", computer_roll)

    if player_roll > computer_roll:
        print("Player wins this round")
        player_score += 1
    elif computer_roll > player_roll:
        print("Computer wins this round")
        computer_score += 1
    else:
        print("Tie round")

    print("Score -> Player:", player_score, "| Computer:", computer_score)

print("Final Result")

if player_score > computer_score:
    print("Player Wins the Game")
elif computer_score > player_score:
    print("Computer Wins the Game")
else:
    print("Game Tie")
