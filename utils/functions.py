

def get_moves(piece_name, row, col, chessBoard, board_size):

    """
    Possible moves for a Pawn
    """
    if piece_name.endswith("pawn"):
        print("It's a Pawn")
        moves = []
        if piece_name.startswith("white"):
            if row == 6:
                moves.append(check_isNone(chessBoard, row - 1, col))
                moves.append(check_isNone(chessBoard, row - 2, col))
            else:
                moves.append(check_isNone(chessBoard, row - 1, col))
        else:
            if row == 1:
                moves.append(check_isNone(chessBoard, row + 1, col))
                moves.append(check_isNone(chessBoard, row + 2, col))
            else:
                moves.append(check_isNone(chessBoard, row + 1, col))
        
        return moves

    """
    Possible moves for a Knight
    """

    if piece_name.endswith("knight"):
        print("It's a Knight")
        moves = []
        moves.append(check_isNone(chessBoard, row - 2, col - 1))
        moves.append(check_isNone(chessBoard, row - 2, col + 1))
        moves.append(check_isNone(chessBoard, row - 1, col - 2))
        moves.append(check_isNone(chessBoard, row - 1, col + 2))
        moves.append(check_isNone(chessBoard, row + 1, col - 2))
        moves.append(check_isNone(chessBoard, row + 1, col + 2))
        moves.append(check_isNone(chessBoard, row + 2, col - 1))
        moves.append(check_isNone(chessBoard, row + 2, col + 1))
        return moves
    
    """
    Possible moves for a Bishop
    """
    if piece_name.endswith("bishop"):
        print("It's a Bishop")
        moves = []
        # Check possible moves in diagonal direction (up and down)
        for i in range(1,board_size):
            if row + i < board_size and col + i < board_size:
                if chessBoard[row+i][col+i] is None:
                    moves.append((row + i, col + i))
                else:
                    break
        for i in range(1, board_size):
            if row - i >= 0 and col - i >= 0:
                if chessBoard[row-i][col-i] is None:
                    moves.append((row - i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row+i < board_size and col - i >= 0:
                if chessBoard[row+i][col-i] is None:
                    moves.append((row + i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row-i >= 0 and col + i < board_size:
                if chessBoard[row-i][col+i] is None:
                    moves.append((row - i, col + i))
                else:
                    break
        return moves


    """
    Possible moves for a Queen
    """
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
        for i in range(1,board_size):
            if row + i < board_size and col + i < board_size:
                if chessBoard[row+i][col+i] is None:
                    moves.append((row + i, col + i))
                else:
                    break
        for i in range(1, board_size):
            if row - i >= 0 and col - i >= 0:
                if chessBoard[row-i][col-i] is None:
                    moves.append((row - i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row+i < board_size and col - i >= 0:
                if chessBoard[row+i][col-i] is None:
                    moves.append((row + i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row-i >= 0 and col + i < board_size:
                if chessBoard[row-i][col+i] is None:
                    moves.append((row - i, col + i))
                else:
                    break
        return moves
    
    """
    Possible moves for a King
    """
    if piece_name.endswith("king"):
        print("It's a King")
        moves = []
        moves.append(check_isNone(chessBoard, row - 1, col - 1))
        moves.append(check_isNone(chessBoard, row - 1, col))
        moves.append(check_isNone(chessBoard,row - 1, col + 1))
        moves.append(check_isNone(chessBoard, row, col-1))
        moves.append(check_isNone(chessBoard, row,col+1))
        moves.append(check_isNone(chessBoard, row + 1, col - 1))
        moves.append(check_isNone(chessBoard, row + 1, col))
        moves.append(check_isNone(chessBoard, row + 1, col + 1))
        return moves


    """
    Possible moves for a Rook
    """

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
    

def check_isNone(chessBoard, row, col):
    try:
        if chessBoard[row][col] is None:
            return row,col
        else:
            return False
    # If the index is out of range return False
    except IndexError:
        return False