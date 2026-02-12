def parse_board(board):
    if isinstance(board, str):
        return board.strip().split('\n')
    return board

def is_king_checked_logic(board):
    board = parse_board(board)
    n = len(board)

    king_pos = None
    for r in range(n):
        if 'K' in board[r]:
            king_pos = (r, board[r].index('K'))
            break

    if not king_pos:
        return False

    kx, ky = king_pos

    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    pawn_check = [(1, -1), (1, 1)] 
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dirs = bishop_dirs + rook_dirs

    for dx, dy in pawn_check:
        nx, ny = kx + dx, ky + dy
        if is_in_bounds(nx, ny) and board[nx][ny] == 'P':
            return True

    for piece_type, directions in [('B', bishop_dirs), ('R', rook_dirs), ('Q', queen_dirs)]:
        for dx, dy in directions:
            x, y = kx, ky
            while True:
                x += dx
                y += dy
                if not is_in_bounds(x, y):
                    break
                cell = board[x][y]
                if cell == piece_type:
                    return True
                if cell != '.':
                    break
    
    return False