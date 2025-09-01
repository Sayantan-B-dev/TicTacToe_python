matrix = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

def display(m):
    for row in m:
        print("["+",".join(row)+"]")
    print()

def input_value():
    """Ask first player to choose X or O"""
    inp = ''
    while inp not in ['x', 'o']:
        inp = input("Select your symbol (X or O): ").lower()
        if inp not in ['x', 'o']:
            print("[[ Please select either X or O ]]")
    return inp

def select_position():
    """Ask player to choose position (1-9) and return (row, col)"""
    matrix_pos = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2]
    }
    pos = ''
    while pos not in range(1,10):
        pos = input("Choose a position (1-9): ")
        try:
            pos = int(pos)
        except ValueError:
            print("[[ Please enter a number between 1-9 ]]")
            continue
        if pos not in range(1,10):
            print("[[ Invalid choice. Try again (1-9) ]]")
    return matrix_pos[pos]

def new_matrix(inp, row, col):
    """Place symbol if position is free. Return True/False"""
    if matrix[row][col] == ' ':
        matrix[row][col] = inp
        return True
    else:
        print("[[ That position is already taken! ]]")
        return False

def check_winner():
    """Check if there is a winner"""
    for i in range(3):
        # Rows
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != ' ':
            return matrix[i][0]
        # Columns
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != ' ':
            return matrix[0][i]
    # Diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ':
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != ' ':
        return matrix[0][2]
    return None

def is_draw():
    """Check if the game is a draw"""
    for row in matrix:
        if ' ' in row:
            return False
    return True

def reset_board():
    """Reset the board for new game"""
    global matrix
    matrix = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

def game():
    """Main game loop"""
    reset_board()

    # Player chooses X or O
    player1 = input_value()
    player2 = 'o' if player1 == 'x' else 'x'
    current_player = player1

    print(f"Player 1 is [{player1.upper()}], Player 2 is [{player2.upper()}]")

    while True:
        print(f"Player {current_player.upper()}'s turn")
        display(matrix)

        row, col = select_position()

        if not new_matrix(current_player, row, col):
            continue  # invalid move, retry

        winner = check_winner()
        if winner:
            display(matrix)
            print(f"[[ Player {winner.upper()} wins! ]]")
            break

        if is_draw():
            display(matrix)
            print("[[ It's a draw! ]]")
            break

        # Switch turn
        current_player = player2 if current_player == player1 else player1

    # Ask if want to play again
    again = input("Do you want to play again? (y/n): ").lower()
    if again == 'y':
        game()
    else:
        print("Thanks for playing!")

# Start the game
game()