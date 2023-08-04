import pygame
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

def draw_board():
    for row in range(board_size):
        for column in range(board_size):
            if (row + column) % 2 == 0:
                color = color1
            else:
                color = color2
            pygame.draw.rect(screen, color, pygame.Rect((start_x + column * square_size), (start_y + row * square_size), square_size, square_size))
            piece = chessBoard[row][column]
            if piece:
                piece_img = pygame.transform.scale(pieces[piece], (square_size, square_size))
                screen.blit(piece_img, (start_x + column * square_size, start_y + row * square_size))



# Calculate the starting position to center the chessboard
start_x = (screen_width - (board_size * square_size)) // 2
start_y = (screen_height - (board_size * square_size)) // 2

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            
    screen.fill((64, 62, 57))  # Clear the screen
    draw_board()

    pygame.display.update()
