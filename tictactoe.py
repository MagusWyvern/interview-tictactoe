import random # For coin flipping

print(f"""
  _____ _        _____            _____           
 |_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___  
   | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ 
   | | | | (__    | | (_| | (__    | | (_) |  __/ 
   |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___| 

""")
print("Welcome to Tic Tac Toe!\nA simple game made by Adi Ahmad Danish (@MagusWyvern)\nThis game requires two players to play, so make sure to grab a friend!\n")
print("Standard rules for Tic Tac Toe apply:\n1. The game is played on a 3x3 grid.\n2. Players take turns marking a square.\n3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over.\n5. If no player has 3 marks in a row, the game is a draw.\n")

player1 = input("Player 1, please enter your name (Player 1): ") or "Player 1"
player2 = input("Player 2, please enter your name (Player 2): ") or "Player 2"

print(f"Welcome, {player1} and {player2}! Let's get started!\n")

# Ask for player 1's marker
player1_marker = input(f"{player1}, please choose your marker (X or O): ")
while player1_marker != 'X' and player1_marker != 'O':
    player1_marker = input(f"Invalid marker! Please choose either X or O: ")

# Assign player 2's marker
player2_marker = 'X' if player1_marker == 'O' else 'O'

print(f"\n{player1} will be using {player1_marker} and {player2} will be using {player2_marker}.\n")

# Flip a 'coin' to determine who will move first

coin_flip = random.randint(0, 1)
current_player = player1 if coin_flip == 0 else player2

print(f"Coin flipping.. {current_player} will go first!\n")

# Initialize the board
board_state = [None, None, None, None, None, None, None, None, None]

print("Here is the board:")
print(f"""
===================
|  1  |  2  |  3  |
===================
|  4  |  5  |  6  |
===================
|  7  |  8  |  9  |
===================
""")

def check_game_over(board_state):
  """Checks if the game is over (win or draw).

  Args:
      board_state: A list representing the current board state.

  Returns:
      True if the game is over, False otherwise.
  """

  # Define winning conditions
  winning_conditions = [
      (0, 1, 2), (3, 4, 5), (6, 7, 8),
      (0, 3, 6), (1, 4, 7), (2, 5, 8),
      (0, 4, 8), (2, 4, 6)
  ]

  # Check for win
  for row in winning_conditions:
    if board_state[row[0]] == board_state[row[1]] == board_state[row[2]] and board_state[row[0]] is not None:
      return True

  # Check for draw
  if None not in board_state:
    return True

  return False

def print_board(board_state):
    """Prints the board with the updated state.

    Args:
        board_state: A list representing the current board state.
    """

    # Define a row separator for better formatting
    row_separator = "==================="

    # Loop through each row and print cells with proper formatting
    for i in range(0, 9, 3):
        print(row_separator)
        print(f"|  {' ' if board_state[i] is None else board_state[i]}  |  {' ' if board_state[i+1] is None else board_state[i+1]}  |  {' ' if board_state[i+2] is None else board_state[i+2]}  |")

    print(row_separator)

# Main game loop
while True:
    print(f"{current_player}'s turn!")
    move = int(input("Enter the number of the square you want to mark [1-9]: ")) - 1

    while move < 0 or move > 8 or board_state[move] is not None:
        move = int(input("Invalid move! Please enter a valid number: ")) - 1

    board_state[move] = player1_marker if current_player == player1 else player2_marker
    print_board(board_state)
    
    if check_game_over(board_state):
        break
    current_player = player1 if current_player == player2 else player2

# Check the game result
if None not in board_state:
    print("It's a draw!")
else:
    # The previous player is the winner
    winner = player2 if current_player == player2 else player1
    print(f"{winner} wins! Congratulations!")

print("Thanks for playing Tic Tac Toe! Goodbye!")
input("Press Enter to exit..")
