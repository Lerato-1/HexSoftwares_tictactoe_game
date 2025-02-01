import random

# Function to get available moves on the board (empty spaces)
def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]  # Return the indices of all empty spaces

# Function to make the computer's move
def computer_move(board):
    available_moves = get_available_moves(board)  # Get a list of available moves
    if available_moves:  # Check if there are available moves
        move = random.choice(available_moves)  # Select a random move from available moves
        board[move] = "O"  # Mark the chosen spot with "O" (computer's symbol)
    else:
        print("No available moves. Game Over!")  # Handle the case when no moves are available
