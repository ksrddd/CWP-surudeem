#!/usr/bin/env python3
"""
x_pattern.py - ตัวอย่างการตรวจแนวทแยง 4 ทิศทาง (Bishop และ Queen)
ใช้แค่ while loop และ if จากที่เรียนใน Cell 02 - Cell 03
"""

def check_diagonal(board, king_r, king_c):
    size = len(board)

    # 1. ทิศซ้ายบน (แถวลด, หลักลด)
    r = king_r - 1
    c = king_c - 1
    while r >= 0 and c >= 0:
        if board[r][c] in ('B', 'Q'):
            return True
        elif board[r][c] != '.':
            break  # มีหมากตัวอื่นบังทาง
        r -= 1
        c -= 1

    # 2. ทิศขวาบน (แถวลด, หลักเพิ่ม)
    r = king_r - 1
    c = king_c + 1
    while r >= 0 and c < size:
        if board[r][c] in ('B', 'Q'):
            return True
        elif board[r][c] != '.':
            break
        r -= 1
        c += 1

    # 3. ทิศซ้ายล่าง (แถวเพิ่ม, หลักลด)
    r = king_r + 1
    c = king_c - 1
    while r < size and c >= 0:
        if board[r][c] in ('B', 'Q'):
            return True
        elif board[r][c] != '.':
            break
        r += 1
        c -= 1

    # 4. ทิศขวาล่าง (แถวเพิ่ม, หลักเพิ่ม)
    r = king_r + 1
    c = king_c + 1
    while r < size and c < size:
        if board[r][c] in ('B', 'Q'):
            return True
        elif board[r][c] != '.':
            break
        r += 1
        c += 1

    return False

# --- ทดสอบการทำงาน ---
if __name__ == "__main__":
    # ตัวอย่าง: Bishop อยู่ซ้ายบนของ King
    board = [
        "B...",
        ".K..",
        "....",
        "...."
    ]
    king_r = 1
    king_c = 1

    if check_diagonal(board, king_r, king_c):
        print("Success (King โดนแนวทแยงรุก!)")
    else:
        print("Fail (King ปลอดภัยจากแนวทแยง)")
