from random import randint
import os
import time

# Functions
def loading_dots(duration, interval):
    start_time = time.time()
    print("Loading Number Race")
    while time.time() - start_time < duration:
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(interval)

def main_menu():
    menu_status = True
    opt_status = True

    while menu_status:
        os.system('clear')
        print(":::::::::::::::::")
        print("::: MAIN MENU :::")
        print(":::::::::::::::::")
        print("[1]. Play")
        print("[2]. Help")
        print("[3]. About us")
        print("[4]. Exit")

        while opt_status:
            opt = int(input(".::: Press any option: "))
            if opt < 1 or opt > 4:
                print("::: Invalid option, try again :::")
            else:
                opt_status = False

        if opt == 1:
            num_players = int(input("Enter the number of players (between 2 and 4): "))
            board_level = int(input("Select the board level to play:\n1. Basic Level\n2. Intermediate Level\n3. Advanced Level\n4. Expert Level\nEnter the corresponding number: "))
            play_numeric_race(num_players, board_level)
            opt_status = True

        elif opt == 2:
            show_help()
            opt_status = True

        elif opt == 3:
            about_us()
            opt_status = True

        elif opt == 4:
            exit_game()
            break

def show_help():
    print("Here are some ways we can help:")
    print("- You can read the game rules.")
    print("- You can learn about the different levels of the game.")
    input("Press Enter to go back to the main menu.")

def about_us():
    print("About us:")
    print("Maria is the creator of this game.")
    input("Press Enter to go back to the main menu.")

def exit_game():
    print("Exiting the game...")

def roll_dice():
    return randint(1, 6), randint(1, 6)

def print_board(players, goal):
    print("\nBoard State:")
    for player, position in players.items():
        print(f"Player {player}: {' ' * (position - 1)}{player}")
    print(f"Goal: {' ' * (goal - 1)}X")

def play_numeric_race(num_players, board_level):
    board = {
        1: 20,
        2: 30,
        3: 50,
        4: 100
    }

    if num_players < 2 or num_players > 4:
        print("Invalid number of players.")
        return

    if board_level < 1 or board_level > 4:
        print("Invalid board level.")
        return

    goal = board[board_level]
    players = {i: 1 for i in range(1, num_players + 1)}
    consecutive_pairs = {i: 0 for i in range(1, num_players + 1)}

    while True:
        for player in players:
            input(f"\nPlayer {player}'s turn. Press Enter to roll the dice.")
            die1, die2 = roll_dice()
            print(f"Player {player} rolled {die1} and {die2}.")

            if die1 == die2:
                consecutive_pairs[player] += 1
                if consecutive_pairs[player] == 3:
                    print(f"Player {player} got 3 consecutive pairs! They win the game!")
                    return
            else:
                consecutive_pairs[player] = 0

            new_position = players[player] + die1 + die2
            if new_position >= goal:
                print(f"Player {player} reached the goal! They win the game!")
                return
            players[player] = new_position

        print_board(players, goal)

# Main
os.system('clear')
loading_dots(5, 0.5)
main_menu()
