#!/usr/bin/env python3

def checkmate(board, *extra_rows):
    """
    ฟังก์ชันตรวจสอบว่า King กำลังถูก Check หรือไม่
    - พิมพ์ "Success" หาก King ถูก Check
    - พิมพ์ "Fail" หาก King ไม่ได้ถูก Check
    - พิมพ์ "Error" หากกระดานไม่ถูกต้องตามกติกา
    """
    try:
        # 1. จัดการ input ให้เป็น list ของแถว (rows)
        if extra_rows:
            rows = [board] + list(extra_rows)
        elif isinstance(board, str):
            stripped = board.strip('\n\r')
            if not stripped:
                print("Error")
                return
            rows = stripped.splitlines()
        elif isinstance(board, (list, tuple)):
            rows = list(board)
        else:
            print("Error")
            return

        # 2. ตรวจสอบว่ามีข้อมูลแถวหรือไม่
        if not rows:
            print("Error")
            return

        size = len(rows)
        if size == 0:
            print("Error")
            return

        # 3. ตรวจสอบว่าเป็นกระดานสี่เหลี่ยมจัตุรัส และหาตำแหน่งของ King (K)
        king_pos = None
        king_count = 0

        for r in range(size):
            row = rows[r]
            # แต่ละแถวต้องเป็น string และมีความยาวเท่ากับ size
            if not isinstance(row, str) or len(row) != size:
                print("Error")
                return
            for c in range(size):
                if row[c] == 'K':
                    king_pos = (r, c)
                    king_count += 1

        # บนกระดานต้องมี King เพียงตัวเดียวเท่านั้น
        if king_count != 1 or king_pos is None:
            print("Error")
            return

        kr, kc = king_pos

        # 4. ตรวจสอบ Pawn (P): ตามโจทย์ Pawn โจมตีทแยงขึ้นด้านบน
        p_row = kr + 1
        if 0 <= p_row < size:
            for p_col in (kc - 1, kc + 1):
                if 0 <= p_col < size:
                    if rows[p_row][p_col] == 'P':
                        print("Success")
                        return

        # 5. ตรวจสอบ Knight (N): เคลื่อนที่แบบตัว L 8 ทิศทาง
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        for dr, dc in knight_moves:
            nr = kr + dr
            nc = kc + dc
            if 0 <= nr < size and 0 <= nc < size:
                if rows[nr][nc] == 'N':
                    print("Success")
                    return

        # 6. ตรวจสอบแนวตรง 4 ทิศ สำหรับ Rook (R) และ Queen (Q)
        straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in straight_directions:
            nr = kr + dr
            nc = kc + dc
            while 0 <= nr < size and 0 <= nc < size:
                cell = rows[nr][nc]
                if cell in ('P', 'B', 'R', 'Q', 'N', 'K'):
                    if cell in ('R', 'Q'):
                        print("Success")
                        return
                    else:
                        break  # มีหมากตัวอื่นขวางเส้นทาง
                nr += dr
                nc += dc

        # 7. ตรวจสอบแนวทแยง 4 ทิศ สำหรับ Bishop (B) และ Queen (Q)
        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in diagonal_directions:
            nr = kr + dr
            nc = kc + dc
            while 0 <= nr < size and 0 <= nc < size:
                cell = rows[nr][nc]
                if cell in ('P', 'B', 'R', 'Q', 'N', 'K'):
                    if cell in ('B', 'Q'):
                        print("Success")
                        return
                    else:
                        break  # มีหมากตัวอื่นขวางเส้นทาง
                nr += dr
                nc += dc

        # หากไม่มีหมากตัวใดสามารถกิน King ได้
        print("Fail")

    except Exception:
        print("Error")
