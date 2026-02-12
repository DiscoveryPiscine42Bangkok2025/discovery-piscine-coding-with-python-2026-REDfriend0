# test_main.py
from checkmate import checkmate

def run_test(name, board, expected):
    print(f"--- Test: {name} ---")
    print(board)
    print(f"Expected: {expected}")
    print("Result:   ", end="")
    checkmate(board)
    print("")

def main():
    # Case 1: (Rook กิน King)
    board1 = """\
R...
.K..
..P.
....\
"""
    run_test("Subject Example 1 (Rook check)", board1, "Success")

    # Case 2: (ปลอดภัย)
    board2 = """\
..
.K\
"""
    run_test("Subject Example 2 (Safe)", board2, "Fail")

    # Case 3: Pawn กิน King (Pawn อยู่ล่าง King อยู่บน)
    board3 = """\
....
.K..
P...
....\
"""
    run_test("Pawn Attack (Bottom-Left)", board3, "Success")

    # Case 4: Bishop กิน King (แนวทแยง)
    board4 = """\
B...
.K..
....
....\
"""
    run_test("Bishop Attack", board4, "Success")

    # Case 5: Queen กิน King (แนวตั้ง)
    board5 = """\
Q...
K...
....
....\
"""
    run_test("Queen Attack (Vertical)", board5, "Success")

    # Case 6: มีตัวบัง (Blocking)
    # Rook จะกิน King แต่มี Pawn บังอยู่ -> ต้อง Fail
    board6 = """\
R...
P...
K...
....\
"""
    run_test("Blocking (Rook blocked by Pawn)", board6, "Fail")

    # Case 7: ไม่มี King -> ควร Fail หรือไม่ Error
    board7 = """\
....
....
....
....\
"""
    run_test("No King", board7, "Fail")

if __name__ == "__main__":
    main()