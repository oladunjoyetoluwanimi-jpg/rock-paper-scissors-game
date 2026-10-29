import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    while True:
        # 1. We just take the input here as a string
        playerchoice = input(f"\n{name},Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name},You must enter 1, 2, or 3.")
            continue

        player = int(playerchoice)

        # random.choice("123") picks a string (like "1"), so this is fine
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        # 3. We must use str() on playerchoice because it is an integer
        print(f"\n{name},You chose: {str(RPS(player)).replace('RPS.','').title()}.")

        print(
              f"Python chose: {str(RPS(computer)).replace('RPS.', '').title()}.\n"
              )

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "😃You win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}😃You win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}😃You win"
            elif player == computer:
                player_wins += 1
                return f"{name}🙏🏼It's a tie!"
            else:
                player_wins += 1
                return f"{name}🐍You lose! \n sorry,{name}.."

        game_result =  decide_winner(player, computer)
        print(game_result)

        
        game_count += 1
        print(f"\n Game Count: {game_count}")
        print(f"\n {name}'s wins: {player_wins}")
        print(f"\n Python wins: {python_wins}")

        print(f"\nPlay again {name}")
        
        while True:    

            playagain = input("\nPlay again? \nY for yes or \nQ to quit\n\n").strip().lower()

            if playagain == "y":
                continue
            else:
                print("\n🙂‍↔️🙂‍↔️🙃")
                print("\nThank you for playing!\n")
                sys.exit(f"Bye!👋🏼👋🏼👋🏼👋🏼 ,{name}")

    return play_rps


rock_paper_scissors= rps()

if __name__=="__main__":
    import argparse

parser = argparse.ArgumentParser(
    description="provides a personal game experience."
)

parser.add_argument(
    "-n", "--name", metavar="name", 
    required=True, help="The name of the person playing the game."
)


args =parser.parse_args()
rock_paper_scissors= rps(args.name)
rock_paper_scissors()

