import random

options = ("Rock", "Paper", "Scissors")
best_of_three_pc = 0
best_of_three_player = 0

while True:

    if best_of_three_player >= 3:
        print("Player won the game!")
        break

    if best_of_three_pc >= 3:
        print("PC won the game!")
        break

    player_pick = input("Player pick: ")
    print("")

    pc_pick = random.choice(options)

    if player_pick == pc_pick:
        print("It's draw! Pick another one")
        print("")
        continue

    elif player_pick == "Rock" and pc_pick == "Scissors":
        print("Player won this round!")
        print("")
        best_of_three_player += 1
    elif player_pick == "Paper" and pc_pick == "Rock":
        print("Player won this round!")
        print("")
        best_of_three_player += 1
    elif player_pick == "Scissors" and pc_pick == "Paper":
        print("Player won this round!")
        print("")
        best_of_three_player += 1
    else:
        print("PC won this round!")
        print("")
        best_of_three_pc += 1
