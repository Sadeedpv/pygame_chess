

def get_moves(piece_name, row, col, chessBoard, board_size):
    if piece_name.endswith("pawn"):
        print("It's a Pawn")
        moves = []
        if piece_name.startswith("white"):
            if row == 6:
                moves.append((row - 1, col))
                moves.append((row - 2, col))
            else:
                moves.append((row - 1, col))
        else:
            if row == 1:
                moves.append((row + 1, col))
                moves.append((row + 2, col))
            else:
                moves.append((row + 1, col))
        
        return moves

    if piece_name.endswith("knight"):
        print("It's a Knight")
    
    if piece_name.endswith("bishop"):
        print("It's a Bishop")
        moves = []
        # Check possible moves in diagonal direction (up and down)
        for i in range(board_size):
            moves.append((row + i, col + i))
            moves.append((row - i, col - i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))
        return moves

    if piece_name.endswith("queen"):
        print("It's a Queen")
        moves = []
                # Check possible moves in vertical direction (up and down)
        for i in range(row + 1, board_size):
            if chessBoard[i][col] is None:
                moves.append((i, col))
            else:
                break

        for i in range(row - 1, -1, -1):
            if chessBoard[i][col] is None:
                moves.append((i, col))
            else:
                break

        # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):
            if chessBoard[row][j] is None:
                moves.append((row, j))
            else:
                break

        for j in range(col - 1, -1, -1):
            if chessBoard[row][j] is None:
                moves.append((row, j))
            else:
                break
                # Check possible moves in diagonal direction (up and down)
        for i in range(board_size):
            moves.append((row + i, col + i))
            moves.append((row - i, col - i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))
        return moves
    
    if piece_name.endswith("king"):
        print("It's a King")
        moves = []
        moves.append((row - 1, col - 1))
        moves.append((row - 1, col))
        moves.append((row - 1, col + 1))
        moves.append((row,col-1))
        moves.append((row,col+1))
        moves.append((row + 1, col - 1))
        moves.append((row + 1, col))
        moves.append((row + 1, col + 1))
        return moves

    if piece_name.endswith("rook"):
        print("It's a Rook")
        moves = []

        # Check possible moves in vertical direction (up and down)
        for i in range(row + 1, board_size):
            if chessBoard[i][col] is None:
                moves.append((i, col))
            else:
                break

        for i in range(row - 1, -1, -1):
            if chessBoard[i][col] is None:
                moves.append((i, col))
            else:
                break

        # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):
            if chessBoard[row][j] is None:
                moves.append((row, j))
            else:
                break

        for j in range(col - 1, -1, -1):
            if chessBoard[row][j] is None:
                moves.append((row, j))
            else:
                break
        return moves