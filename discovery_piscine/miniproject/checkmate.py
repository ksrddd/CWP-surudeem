#!/usr/bin/env python3

def checkmate(board, *extra_rows):
    """
    ฟังก์ชันตรวจสอบว่า King ถูกรุก (Check) หรือไม่ ตามโจทย์ Rush00
    - พิมพ์ "Success" หาก King ถูกรุก
    - พิมพ์ "Fail" หาก King ปลอดภัย
    - พิมพ์ "Error" หรือไม่พิมพ์อะไร หากกระดานผิดกติกา
    """
    try:
        # 1. จัดการ input ให้เป็น list ของแถว (รองรับทั้งแบบ string แผ่นเดียว หรือส่งแยกแถว)
        if extra_rows:
            rows = [board] + list(extra_rows)
        elif isinstance(board, str):
            board_clean = board.replace('\r', '').strip('\n')
            if not board_clean:
                print("Error")
                return
            rows = board_clean.split('\n')
        elif isinstance(board, list):
            rows = board
        else:
            print("Error")
            return

        size = len(rows)
        if size == 0:
            print("Error")
            return

        # 2. ตรวจสอบว่าเป็นกระดานสี่เหลี่ยมจัตุรัส (ความยาวของทุกแถวต้องเท่ากับ size)
        for row in rows:
            if len(row) != size:
                print("Error")
                return

        # 3. วนลูปหาตำแหน่งของ King (K) ซึ่งต้องมีเพียง 1 ตัวเท่านั้น
        king_r = -1
        king_c = -1
        king_count = 0

        for r in range(size):
            for c in range(size):
                if rows[r][c] == 'K':
                    king_r = r
                    king_c = c
                    king_count += 1

        if king_count != 1:
            print("Error")
            return

        # 4. ตรวจสอบ Pawn (P): โจมตีทแยงขึ้นบน ดังนั้นจะกิน King ได้ ต้องอยู่แถวล่าง (king_r + 1)
        p_row = king_r + 1
        if p_row < size:
            # เฉียงซ้ายล่าง
            if king_c - 1 >= 0 and rows[p_row][king_c - 1] == 'P':
                print("Success")
                return
            # เฉียงขวาล่าง
            if king_c + 1 < size and rows[p_row][king_c + 1] == 'P':
                print("Success")
                return

        # 5. ตรวจสอบแนวตรง 4 ทิศ (Rook 'R' และ Queen 'Q')
        # เดินขึ้น
        r = king_r - 1
        while r >= 0:
            cell = rows[r][king_c]
            if cell in ('R', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'B', 'K'):
                break  # มีหมากตัวอื่นบังทาง
            r -= 1

        # เดินลง
        r = king_r + 1
        while r < size:
            cell = rows[r][king_c]
            if cell in ('R', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'B', 'K'):
                break
            r += 1

        # เดินไปทางซ้าย
        c = king_c - 1
        while c >= 0:
            cell = rows[king_r][c]
            if cell in ('R', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'B', 'K'):
                break
            c -= 1

        # เดินไปทางขวา
        c = king_c + 1
        while c < size:
            cell = rows[king_r][c]
            if cell in ('R', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'B', 'K'):
                break
            c += 1

        # 6. ตรวจสอบแนวทแยง 4 ทิศ (Bishop 'B' และ Queen 'Q')
        # ทแยงซ้ายบน
        r = king_r - 1
        c = king_c - 1
        while r >= 0 and c >= 0:
            cell = rows[r][c]
            if cell in ('B', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'R', 'K'):
                break  # มีหมากตัวอื่นบังทาง
            r -= 1
            c -= 1

        # ทแยงขวาบน
        r = king_r - 1
        c = king_c + 1
        while r >= 0 and c < size:
            cell = rows[r][c]
            if cell in ('B', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'R', 'K'):
                break
            r -= 1
            c += 1

        # ทแยงซ้ายล่าง
        r = king_r + 1
        c = king_c - 1
        while r < size and c >= 0:
            cell = rows[r][c]
            if cell in ('B', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'R', 'K'):
                break
            r += 1
            c -= 1

        # ทแยงขวาล่าง
        r = king_r + 1
        c = king_c + 1
        while r < size and c < size:
            cell = rows[r][c]
            if cell in ('B', 'Q'):
                print("Success")
                return
            elif cell in ('P', 'R', 'K'):
                break
            r += 1
            c += 1

        # 7. ถ้าไม่มีหมากตัวใดรุก King ได้
        print("Fail")

    except Exception:
        print("Error")
