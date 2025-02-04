import random

# Function to get available moves on the board (empty spaces)
def get_available_moves(board):
    return [i for i, x in enumerate([cell for row in board for cell in row]) if x == " "]

# Function to make the computer's move
def computer_move(board):
    available_moves = get_available_moves(board)  
    if available_moves:  
        move = random.choice(available_moves)
        # Convert the flat move index back to 2D coordinates and mark the board
        row, col = divmod(move, 3)
        board[row][col] = "O"  
    else:
        print("No available moves. Game Over!")  # Handle the case when no moves are available

# Function to print the current state of the board
def print_board(board):
    for row in board:
        print(" | ".join(row))  
        print("-" * 9) 

# Function to check if a player has won
def check_winner(board, player):
    # Check for a winner in rows, columns, and diagonals
    return any(
        all(cell == player for cell in line) 
        for line in board + list(zip(*board)) + [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    )

# Function to prompt the player to make a move
def player_move(board):
    while (move := input("Enter your move (1-9): ")) not in map(str, range(1, 10)) or board[(row := (int(move)-1)//3)][(col := (int(move)-1)%3)] != " ":
        # Check if input is valid (1-9) and the chosen position is empty
        print("Invalid move. Try again.")  
    board[row][col] = "X" 

# Main function to run the game
def main():
    board = [[" "] * 3 for _ in range(3)]
    print("Welcome to Lerato's Tic-Tac-Toe!")  
    for turn in range(9): 
        print_board(board) 
        # Alternate between player and computer moves based on turn number
        (player_move if turn % 2 == 0 else computer_move)(board)
        # Check if the current player has won
        if check_winner(board, "XO"[turn % 2]):
            print_board(board) 
            print(f"{'You' if turn % 2 == 0 else 'Computer'} win!") 
            return  
    print("It's a draw!") 

if __name__ == "__main__":
    main()  

