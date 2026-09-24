#!/usr/bin/env python3
"""
plus_pattern.py - ตัวอย่างการตรวจแนวตรง 4 ทิศทาง (Rook และ Queen)
ใช้แค่ while loop และ if จากที่เรียนใน Cell 02 - Cell 03
"""

def check_straight(board, king_r, king_c):
    size = len(board)

    # 1. ทิศขึ้นด้านบน (แถวลดลงเรื่อยๆ)
    r = king_r - 1
    while r >= 0:
        if board[r][king_c] in ('R', 'Q'):
            return True
        elif board[r][king_c] != '.':
            break  # มีหมากตัวอื่นบังทาง ให้หยุดดูทิศนี้
        r -= 1

    # 2. ทิศลงด้านล่าง (แถวเพิ่มขึ้นเรื่อยๆ)
    r = king_r + 1
    while r < size:
        if board[r][king_c] in ('R', 'Q'):
            return True
        elif board[r][king_c] != '.':
            break  # มีหมากตัวอื่นบังทาง
        r += 1

    # 3. ทิศไปทางซ้าย (หลักลดลงเรื่อยๆ)
    c = king_c - 1
    while c >= 0:
        if board[king_r][c] in ('R', 'Q'):
            return True
        elif board[king_r][c] != '.':
            break
        c -= 1

    # 4. ทิศไปทางขวา (หลักเพิ่มขึ้นเรื่อยๆ)
    c = king_c + 1
    while c < size:
        if board[king_r][c] in ('R', 'Q'):
            return True
        elif board[king_r][c] != '.':
            break
        c += 1

    return False

# --- ทดสอบการทำงาน ---
if __name__ == "__main__":
    # ตัวอย่าง: Rook อยู่ด้านบน King
    board = [
        ".R..",
        ".K..",
        "....",
        "...."
    ]
    king_r = 1
    king_c = 1

    if check_straight(board, king_r, king_c):
        print("Success (King โดนแนวตรงรุก!)")
    else:
        print("Fail (King ปลอดภัยจากแนวตรง)")
