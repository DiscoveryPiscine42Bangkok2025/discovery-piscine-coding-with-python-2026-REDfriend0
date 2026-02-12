import sys
from checkmate import is_king_checked_logic

def read_board(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            if not lines: return None
            n = len(lines)
            for line in lines:
                if len(line) != n:
                    return None
            return lines
    except Exception:
        return None

def main():
    if len(sys.argv) < 2:
        return

    for file_path in sys.argv[1:]:
        board = read_board(file_path)
        
        if board is None:
            print("Error")
            continue

        k_count = sum(row.count('K') for row in board)
        if k_count != 1:
            print("Error")
            continue

        if is_king_checked_logic(board):
            print("Success")
        else:
            print("Fail")

if __name__ == "__main__":
    main()