import random

# Function to get available moves on the board (empty spaces)
def get_available_moves(board):
    return [i for i, x in enumerate([cell for row in board for cell in row]) if x == " "]  # Flatten and find empty spaces

# Function to make the computer's move
def computer_move(board):
    available_moves = get_available_moves(board)  # Get a list of available moves
    if available_moves:  # Check if there are available moves
        move = random.choice(available_moves)  # Select a random move from available moves
        # Convert the flat move index back to 2D coordinates and mark the board
        row, col = divmod(move, 3)
        board[row][col] = "O"  # Mark the chosen spot with "O" (computer's symbol)
    else:
        print("No available moves. Game Over!")  # Handle the case when no moves are available

# Function to print the current state of the board
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Join the cells in a row with " | " for better readability
        print("-" * 9)  # Print a separator line after each row
