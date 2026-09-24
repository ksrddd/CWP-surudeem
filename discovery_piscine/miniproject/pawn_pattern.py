#!/usr/bin/env python3
"""
pawn_pattern.py - ตัวอย่างการตรวจ Pawn (เบี้ย)
ใช้แค่ความรู้พื้นฐานจาก Cell 00 - Cell 07 (for, if, list)
"""

def check_pawn(board, king_r, king_c):
    size = len(board)
    # Pawn เดินขึ้นข้างหน้า ดังนั้นจะกิน King ได้ ต้องอยู่แถวด้านล่าง King (king_r + 1)
    pawn_row = king_r + 1
    
    # ตรวจว่าแถวด้านล่างยังอยู่ในกระดานไหม
    if pawn_row < size:
        # ตรวจเฉียงซ้ายล่าง
        if king_c - 1 >= 0 and board[pawn_row][king_c - 1] == 'P':
            return True
        # ตรวจเฉียงขวาล่าง
        if king_c + 1 < size and board[pawn_row][king_c + 1] == 'P':
            return True
            
    return False

# --- ทดสอบการทำงาน ---
if __name__ == "__main__":
    # กระดานตัวอย่าง King อยู่ที่ (1, 1) และ Pawn อยู่ที่ (2, 2)
    board = [
        "R...",
        ".K..",
        "..P.",
        "...."
    ]
    king_r = 1
    king_c = 1

    if check_pawn(board, king_r, king_c):
        print("Success (King โดน Pawn รุก!)")
    else:
        print("Fail (King ปลอดภัยจาก Pawn)")
