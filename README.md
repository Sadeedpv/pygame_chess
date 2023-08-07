This is a chess game made with pygame.

To run the game, open a terminal window and navigate to the directory where the code is saved. Then type the following command:

```
python main.py
```

The game will start and you can play it by clicking on the squares on the chessboard.

Here are some explanations of the code:

* The `pygame` library is used to create the graphics and handle the user input.
* The `chessboard` is a 2D list that represents the chessboard. Each element of the list is a string that represents the piece that is on that square.
* The `draw_board()` function draws the chessboard on the screen.
* The `handleClick()` function handles the logic for when the user clicks on a square on the chessboard.
* The `get_moves()` function returns a list of all the possible moves for a given piece.

## How to play

The game of chess is played between two players, White and Black. Each player starts with 16 pieces:

* 8 pawns
* 2 rooks
* 2 knights
* 2 bishops
* 1 queen
* 1 king

The pieces are arranged on the board as shown in the following diagram:

```
     a b c d e f g h
8   ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
7  ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
6   . . . . . . . .
5   . . . . . . . .
4   . . . . . . . .
3   . . . . . . . .
2  ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
1   ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
```

The objective of the game is to take your opponent's king. To move a piece, click on the piece you want to move and then click on the square you want to move it to(It will show all the possible moves).

I hope this helps!