import pygame
# Import a function from functions.py inside utils folder for me
from utils.functions import get_moves
pygame.init()

# Create the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# TITLE OF CANVAS
pygame.display.set_caption("Chess game")
exit = False

# Chessboard properties
board_size = 8
square_size = min(screen_width, screen_height) // (board_size + 1)

bgColor = (64, 62, 57)
selected_color = (255, 90, 48)
color1 = (238,238,210)
color2 = (118,150,86)

# Chessboard pieces
pieces = {
    "black_pawn": pygame.image.load("images/black_pawn.png"),
    "black_rook": pygame.image.load("images/black_rook.png"),
    "black_knight": pygame.image.load("images/black_knight.png"),
    "black_bishop": pygame.image.load("images/black_bishop.png"),
    "black_queen": pygame.image.load("images/black_queen.png"),
    "black_king": pygame.image.load("images/black_king.png"),
    "white_pawn": pygame.image.load("images/white_pawn.png"),
    "white_rook": pygame.image.load("images/white_rook.png"),
    "white_knight": pygame.image.load("images/white_knight.png"),
    "white_bishop": pygame.image.load("images/white_bishop.png"),
    "white_queen": pygame.image.load("images/white_queen.png"),
    "white_king": pygame.image.load("images/white_king.png")
}

captured_pieces = []

# Create the chessboard representation as a 2D list
chessBoard = [[None for _ in range(board_size)] for _ in range(board_size)]

# Draw the chessboard

# Draw the black pieces
chessBoard[0][0] = "black_rook"
chessBoard[0][1] = "black_knight"
chessBoard[0][2] = "black_bishop"
chessBoard[0][3] = "black_king"
chessBoard[0][4] = "black_queen"
chessBoard[0][5] = "black_bishop"
chessBoard[0][6] = "black_knight"
chessBoard[0][7] = "black_rook"
chessBoard[1][0] = "black_pawn"
chessBoard[1][1] = "black_pawn"
chessBoard[1][2] = "black_pawn"
chessBoard[1][3] = "black_pawn"
chessBoard[1][4] = "black_pawn"
chessBoard[1][5] = "black_pawn"
chessBoard[1][6] = "black_pawn"
chessBoard[1][7] = "black_pawn"

# Draw the white pieces
chessBoard[7][0] = "white_rook"
chessBoard[7][1] = "white_knight"
chessBoard[7][2] = "white_bishop"
chessBoard[7][3] = "white_king"
chessBoard[7][4] = "white_queen"
chessBoard[7][5] = "white_bishop"
chessBoard[7][6] = "white_knight"
chessBoard[7][7] = "white_rook"
chessBoard[6][0] = "white_pawn"
chessBoard[6][1] = "white_pawn"
chessBoard[6][2] = "white_pawn"
chessBoard[6][3] = "white_pawn"
chessBoard[6][4] = "white_pawn"
chessBoard[6][5] = "white_pawn"
chessBoard[6][6] = "white_pawn"
chessBoard[6][7] = "white_pawn"

# Calculate the starting position to center the chessboard
start_x = (screen_width - (board_size * square_size)) // 2
start_y = (screen_height - (board_size * square_size)) // 2


def draw_board():
    for row in range(board_size):
        for column in range(board_size):
            if (row + column) % 2 == 0:
                color = color1
            else:
                color = color2
            if (possible_moves is not None and (row, column) in possible_moves) or (selected_piece_row ==row and selected_piece_col == column):
                color = selected_color
            pygame.draw.rect(screen, color, pygame.Rect((start_x + column * square_size), (start_y + row * square_size), square_size, square_size))
            piece = chessBoard[row][column]
            if piece:
                piece_img = pygame.transform.scale(pieces[piece], (square_size, square_size))
                screen.blit(piece_img, (start_x + column * square_size, start_y + row * square_size))


selected_piece = None
selected_piece_row = None
selected_piece_col = None
turn = "white"
possible_moves = []

def handleClick(row,col):
    print("Mouse clicked at", row, col)
    global selected_piece, selected_piece_row, selected_piece_col, turn, possible_moves

    # Check if there's already a selected piece and it's the player's turn
    if selected_piece and (chessBoard[row][col] is None or not chessBoard[row][col].startswith(turn)) and possible_moves is not None and (row,col) in possible_moves and selected_piece.startswith(turn):
        # Move the selected piece to the new position
        chessBoard[row][col] = selected_piece
        # Clear the old position
        chessBoard[selected_piece_row][selected_piece_col] = None
        # Switch turn to the other player
        turn = "white" if turn == "black" else "black"
        selected_piece = None
    elif chessBoard[row][col] and chessBoard[row][col].startswith(turn):
        # If the clicked square contains a piece of the player's color, select it
        selected_piece = chessBoard[row][col]
        selected_piece_row, selected_piece_col = row, col
        possible_moves = get_moves(chessBoard[row][col], row, col, chessBoard, board_size, turn)
    else:
        # If the clicked square is empty or contains an opponent's piece, deselect
        selected_piece = None




while not exit:
    for event in pygame.event.get():
        # If user press ESC or clicks X
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            # Handle logic if clicked inside the board
            if start_x <= mouse_x <= start_x + (board_size * square_size) and start_y <= mouse_y <= start_y + (board_size * square_size):
                col = (mouse_x - start_x) // square_size
                row = (mouse_y - start_y) // square_size
                handleClick(row, col)
                
            
    screen.fill(bgColor)  # Clear the screen
    draw_board()

    pygame.display.update()
