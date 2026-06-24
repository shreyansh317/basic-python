# tictactoe.py
import math
import random

# Board is a list of 9 elements: 'X', 'O', or ' ' (space)
def new_board():
    return [' '] * 9

def print_board(b):
    print()
    for r in range(3):
        row = " | ".join(b[3*r:3*r+3])
        print(" " + row)
        if r < 2:
            print("---+---+---")
    print()

def available_moves(b):
    return [i for i, v in enumerate(b) if v == ' ']

def winner(b):
    wins = [
        (0,1,2),(3,4,5),(6,7,8), # rows
        (0,3,6),(1,4,7),(2,5,8), # cols
        (0,4,8),(2,4,6)          # diags
    ]
    for a,b2,c in wins:
        if b[a] != ' ' and b[a] == b[b2] == b[c]:
            return b[a]
    if ' ' not in b:
        return 'Tie'
    return None

# Minimax for unbeatable AI (player is 'O' by default)
def minimax(board, depth, is_maximizing, ai_player, human_player):
    result = winner(board)
    if result == ai_player:
        return 10 - depth
    elif result == human_player:
        return depth - 10
    elif result == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in available_moves(board):
            board[i] = ai_player
            score = minimax(board, depth+1, False, ai_player, human_player)
            board[i] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in available_moves(board):
            board[i] = human_player
            score = minimax(board, depth+1, True, ai_player, human_player)
            board[i] = ' '
            best_score = min(best_score, score)
        return best_score

def best_move(board, ai_player, human_player):
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = ai_player
        score = minimax(board, 0, False, ai_player, human_player)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def human_turn(board, mark):
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos in range(9) and board[pos] == ' ':
                board[pos] = mark
                break
            else:
                print("Invalid position or already taken. Try again.")
        except ValueError:
            print("Please enter a number 1-9.")

def computer_turn(board, ai_player, human_player, difficulty):
    if difficulty == 'easy':
        move = random.choice(available_moves(board))
    else:
        move = best_move(board, ai_player, human_player)
    board[move] = ai_player
    print(f"Computer placed {ai_player} in position {move+1}.")

def main():
    print("Tic-Tac-Toe")
    mode = input("Choose mode: (1) Two-player  (2) Play vs Computer: ")
    board = new_board()

    if mode.strip() == '1':
        current = 'X'
        while True:
            print_board(board)
            print(f"Player {current}'s turn.")
            human_turn(board, current)
            r = winner(board)
            if r:
                print_board(board)
                if r == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {r} wins!")
                break
            current = 'O' if current == 'X' else 'X'
    else:
        human_player = ''
        while human_player not in ('X','O'):
            human_player = input("Do you want to be X or O? (X goes first): ").upper()
        ai_player = 'O' if human_player == 'X' else 'X'
        difficulty = ''
        while difficulty not in ('easy','hard'):
            difficulty = input("Difficulty: easy or hard (unbeatable): ").lower()

        current = 'X'
        while True:
            print_board(board)
            if current == human_player:
                print("Your move.")
                human_turn(board, human_player)
            else:
                print("Computer's move.")
                computer_turn(board, ai_player, human_player, difficulty)
            r = winner(board)