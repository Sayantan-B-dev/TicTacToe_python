matrix = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

def display(m):
    for row in m:
        print("["+",".join(row)+"]")
    print()

def input_value():
    inp=''
    while inp not in ['x','o']:
        inp=input("select between x and o. : ").lower()
        if inp not in ['x','o']:
            print("[[!!!select correct option. ]]")
    return inp

def select_position():
    matrix_pos={1:[0,0],2:[0,1],3:[0,2],
               4:[1,0],5:[1,1],6:[1,2],
               7:[2,0],8:[2,1],9:[2,2]}
    pos=''
    while pos not in range(1,10):
        pos=input("select column between (1 to 9). : ")
        print("--------------------------")
        try:
            pos=int(pos)
        except ValueError as e:
            
            print("!!Input should be number")
        if pos not in range(1,10):
                print("!!!select correct column. ")
                print("--------------------------")
        
    return matrix_pos[pos]


def new_matrix(inp, row, col):
    if matrix[row][col] == ' ':
        matrix[row][col] = inp
    else:
        print("[[That position is already taken!]]")
    return matrix


def check_winner():
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != ' ':
            return matrix[i][0]
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != ' ':
            return matrix[0][i]
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ':
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != ' ':
        return matrix[0][2]
    return None

def is_draw():
    for row in matrix:
        if ' ' in row:
            return False
    return True

def game():
    current_player = 'x'
    while True:
        print(f"Player {current_player.upper()}'s turn")
        display(matrix)

        [row,col] = select_position()

        if not new_matrix(current_player, row, col):
            continue

        winner = check_winner()
        if winner:
            display(matrix)
            print(f"[[ Player {winner.upper()} wins! ]]")
            break

        if is_draw():
            display(matrix)
            print("[[ It's a draw! ]]")
            break

        current_player = 'o' if current_player == 'x' else 'x'

game()