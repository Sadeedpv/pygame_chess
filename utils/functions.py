

def get_moves(piece_name, row, col, chessBoard, board_size, turn):

    """
    Possible moves for a Pawn
    """
    if piece_name.endswith("pawn"):
        print("It's a Pawn")
        moves = []
        if piece_name.startswith("white"):
            if chessBoard[row-1][col] is None:
                if row == 6:
                    moves.append((row-1, col))
                    moves.append((row-2, col))
                else:
                    moves.append((row-1, col))
            # Check if there are pieces for pawns to capture sideways
            moves.append(check_side_captures_for_pawn(chessBoard, row - 1, col - 1, turn))
            moves.append(check_side_captures_for_pawn(chessBoard, row - 1, col + 1, turn))
        elif piece_name.startswith("black"):
            if chessBoard[row+1][col] is None:
                if row == 1:
                    moves.append((row + 1, col))
                    moves.append((row + 2, col))
                else:
                    moves.append((row + 1, col))
            # Check if there are pieces for pawns to capture sideways
            moves.append(check_side_captures_for_pawn(chessBoard, row + 1, col - 1, turn,))
            moves.append(check_side_captures_for_pawn(chessBoard, row + 1, col + 1, turn,))
            
        return moves

    """
    Possible moves for a Knight
    """

    if piece_name.endswith("knight"):
        print("It's a Knight")
        moves = []
        moves.append(check_possible_move(chessBoard, row - 2, col - 1, turn))
        moves.append(check_possible_move(chessBoard, row - 2, col + 1, turn))
        moves.append(check_possible_move(chessBoard, row - 1, col - 2, turn))
        moves.append(check_possible_move(chessBoard, row - 1, col + 2, turn))
        moves.append(check_possible_move(chessBoard, row + 1, col - 2, turn))
        moves.append(check_possible_move(chessBoard, row + 1, col + 2, turn))
        moves.append(check_possible_move(chessBoard, row + 2, col - 1, turn))
        moves.append(check_possible_move(chessBoard, row + 2, col + 1, turn))
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
                if check_possible_move(chessBoard, row+i, col+i, turn):
                    if chessBoard[row+i][col+i] and not chessBoard[row+i][col+i].startswith(turn):
                        moves.append((row+i, col+i))
                        break
                    moves.append((row + i, col + i))
                else:
                    break
        for i in range(1, board_size):
            if row - i >= 0 and col - i >= 0:
                if check_possible_move(chessBoard, row-i, col-i, turn):
                    if chessBoard[row-i][col-i] and not chessBoard[row-i][col-i].startswith(turn):
                        moves.append((row-i, col-i))
                        break
                    moves.append((row - i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row+i < board_size and col - i >= 0:
                if check_possible_move(chessBoard, row+i, col-i, turn):
                    if chessBoard[row+i][col-i] and not chessBoard[row+i][col-i].startswith(turn):
                        moves.append((row+i, col-i))
                        break
                    moves.append((row + i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row-i >= 0 and col + i < board_size:
                if check_possible_move(chessBoard, row-i, col+i, turn):
                    if chessBoard[row-i][col+i] and not chessBoard[row-i][col+i].startswith(turn):
                        moves.append((row-i, col+i))
                        break
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
            if check_possible_move(chessBoard, i, col, turn):
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):
                    moves.append((i, col))
                    break
                moves.append((i, col))
            else:
                break

        for i in range(row - 1, -1, -1):
            if check_possible_move(chessBoard, i, col, turn):
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):
                    moves.append((i, col))
                    break
                moves.append((i, col))
            else:
                break

        # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break

        for j in range(col - 1, -1, -1):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break

        # Check possible moves in diagonal direction (up and down)
        for i in range(1,board_size):
            if row + i < board_size and col + i < board_size:
                if check_possible_move(chessBoard, row+i, col+i, turn):
                    if chessBoard[row+i][col+i] and not chessBoard[row+i][col+i].startswith(turn):
                        moves.append((row+i, col+i))
                        break
                    moves.append((row + i, col + i))
                else:
                    break
        for i in range(1, board_size):
            if row - i >= 0 and col - i >= 0:
                if check_possible_move(chessBoard, row-i, col-i, turn):
                    if chessBoard[row-i][col-i] and not chessBoard[row-i][col-i].startswith(turn):
                        moves.append((row-i, col-i))
                        break
                    moves.append((row - i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row+i < board_size and col - i >= 0:
                if check_possible_move(chessBoard, row+i, col-i, turn):
                    if chessBoard[row+i][col-i] and not chessBoard[row+i][col-i].startswith(turn):
                        moves.append((row+i, col-i))
                        break
                    moves.append((row + i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row-i >= 0 and col + i < board_size:
                if check_possible_move(chessBoard, row-i, col+i, turn):
                    if chessBoard[row-i][col+i] and not chessBoard[row-i][col+i].startswith(turn):
                        moves.append((row-i, col+i))
                        break
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
        moves.append(check_possible_move(chessBoard, row - 1, col - 1, turn))
        moves.append(check_possible_move(chessBoard, row - 1, col, turn))
        moves.append(check_possible_move(chessBoard,row - 1, col + 1, turn))
        moves.append(check_possible_move(chessBoard, row, col-1, turn))
        moves.append(check_possible_move(chessBoard, row,col+1, turn))
        moves.append(check_possible_move(chessBoard, row + 1, col - 1, turn))
        moves.append(check_possible_move(chessBoard, row + 1, col, turn))
        moves.append(check_possible_move(chessBoard, row + 1, col + 1, turn))
        return moves


    """
    Possible moves for a Rook
    """

    if piece_name.endswith("rook"):
        print("It's a Rook")
        moves = []

        # Check possible moves in vertical direction (up and down)
        for i in range(row + 1, board_size):
            if check_possible_move(chessBoard, i, col, turn):
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):
                    moves.append((i, col))
                    break
                moves.append((i, col))
            else:
                break

        for i in range(row - 1, -1, -1):
            if check_possible_move(chessBoard, i, col, turn):
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):
                    moves.append((i, col))
                    break
                moves.append((i, col))
            else:
                break

        # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break

        for j in range(col - 1, -1, -1):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break
        return moves
    

# This function checks whether the box user clicked is empty or blocked with their own piece
def check_possible_move(chessBoard, row, col, turn):
    try:
        if chessBoard[row][col] is None or not chessBoard[row][col].startswith(turn):
            return row,col
        else:
            return False
        
    # If the index is out of range return False
    except IndexError:
        return False

# This function checks whether there are any pieces that pawns can capture
def check_side_captures_for_pawn(chessBoard, row, col, turn):
    try:
        if chessBoard[row][col] is not None and not chessBoard[row][col].startswith(turn):
            return row,col
        else:
            return False
    # If the index is out of range return False
    except IndexError:
        return False
