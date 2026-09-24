#!/usr/bin/env python3
"""
Q_pattern.py - ตัวอย่างการตรวจ Queen
Queen สามารถเดินได้ทั้งแนวตรง (+) และแนวทแยง (X) รวม 8 ทิศทาง
"""
from plus_pattern import check_straight
from x_pattern import check_diagonal

def check_queen(board, king_r, king_c):
    # ถ้าโดนรุกจากแนวตรง หรือ แนวทแยง ก็คือโดน Queen ได้
    if check_straight(board, king_r, king_c):
        return True
    if check_diagonal(board, king_r, king_c):
        return True
    return False

# --- ทดสอบการทำงาน ---
if __name__ == "__main__":
    board = [
        "....",
        ".K.Q",
        "....",
        "...."
    ]
    king_r = 1
    king_c = 1

    if check_queen(board, king_r, king_c):
        print("Success (King โดน Queen รุก!)")
    else:
        print("Fail (King ปลอดภัยจาก Queen)")
