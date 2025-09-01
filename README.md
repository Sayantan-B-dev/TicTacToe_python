## 1. The Board

```python
matrix = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
```

* A 3×3 grid stored as a list of lists.
* Each cell starts as `' '` (empty).

---

## 2. Player Choice

```python
def input_value():
    inp = ''
    while inp not in ['x', 'o']:
        inp = input("Select your symbol (X or O): ").lower()
        if inp not in ['x', 'o']:
            print("[[ Please select either X or O ]]")
    return inp
```

* First player chooses whether they want **X** or **O**.
* Keeps asking until valid choice.
* Returns `"x"` or `"o"`.

---

## 3. Selecting a Position

```python
def select_position():
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
```

* `matrix_pos` maps numbers 1–9 to board coordinates:

  ```
  1 | 2 | 3
  4 | 5 | 6
  7 | 8 | 9
  ```
* Input is validated:

  * Must be an integer.
  * Must be in `1–9`.
* Returns `[row, col]` for board placement.

---

## 4. Updating the Board

```python
def new_matrix(inp, row, col):
    if matrix[row][col] == ' ':
        matrix[row][col] = inp
        return True
    else:
        print("[[ That position is already taken! ]]")
        return False
```

* Checks if selected cell is empty (`' '`).
* If yes → put `'x'` or `'o'` there, return `True`.
* If taken → show warning, return `False`.

This fixes the bug from the older code ✅.

---

## 5. Checking for Winner

```python
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
```

* Checks **rows, columns, diagonals**.
* If 3 same marks found → returns `'x'` or `'o'`.
* Otherwise → returns `None`.

---

## 6. Checking Draw

```python
def is_draw():
    for row in matrix:
        if ' ' in row:
            return False
    return True
```

* If no spaces left → board is full → draw.
* Else → game continues.

---

## 7. Resetting the Board

```python
def reset_board():
    global matrix
    matrix = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]
```

* Creates a **fresh empty board** for replay.

---

## 8. Main Game Logic

```python
def game():
    reset_board()

    player1 = input_value()
    player2 = 'o' if player1 == 'x' else 'x'
    current_player = player1

    print(f"Player 1 is [{player1.upper()}], Player 2 is [{player2.upper()}]")

    while True:
        print(f"Player {current_player.upper()}'s turn")
        display(matrix)

        row, col = select_position()

        if not new_matrix(current_player, row, col):
            continue  # retry if invalid move

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

    again = input("Do you want to play again? (y/n): ").lower()
    if again == 'y':
        game()
    else:
        print("Thanks for playing!")
```

### How it works:

1. Board is reset.
2. Player 1 chooses X or O. Player 2 gets the other.
3. While game is running:

   * Show current board.
   * Current player selects position.
   * Place mark if free (`new_matrix`).
   * Check for **winner** → stop if found.
   * Check for **draw** → stop if board is full.
   * Switch turn to other player.
4. After game ends → ask if players want to restart.
