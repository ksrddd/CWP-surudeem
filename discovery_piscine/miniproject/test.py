#!/usr/bin/env python3
import io
import sys
import os
import subprocess

# เพิ่ม path ไปยัง ex00
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(current_dir, 'ex00'))

from checkmate import checkmate

def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        func(*args, **kwargs)
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdout = old_stdout

def run_tests():
    print("=== 1. Running Rush00 (ex00) Unit Tests ===")

    # Test 1: Example 1 ในโจทย์หน้า 6 (Pawn check)
    b1 = """\
R...
.K..
..P.
...."""
    res1 = capture_output(checkmate, b1)
    assert res1 == "Success", f"Test 1 failed: expected Success, got {res1}"
    print("[PASS] Test 1: Subject Example 1 (Success)")

    # Test 2: Example 2 ในโจทย์หน้า 6 (King รอด)
    b2 = """\
..
.K"""
    res2 = capture_output(checkmate, b2)
    assert res2 == "Fail", f"Test 2 failed: expected Fail, got {res2}"
    print("[PASS] Test 2: Subject Example 2 (Fail)")

    # Test 3: Rook อยู่แนวทแยง (ไม่ Check เพราะ Rook เดินแนวตรง)
    b3 = """\
R...
.K..
....
...."""
    res3 = capture_output(checkmate, b3)
    assert res3 == "Fail", f"Test 3 failed: expected Fail, got {res3}"
    print("[PASS] Test 3: Rook on diagonal (Fail)")

    # Test 4: Rook อยู่แนวตรง (Check)
    b4 = """\
.R..
.K..
....
...."""
    res4 = capture_output(checkmate, b4)
    assert res4 == "Success", f"Test 4 failed: expected Success, got {res4}"
    print("[PASS] Test 4: Rook vertical check (Success)")

    # Test 5: Bishop อยู่แนวทแยง (Check)
    b5 = """\
B...
.K..
....
...."""
    res5 = capture_output(checkmate, b5)
    assert res5 == "Success", f"Test 5 failed: expected Success, got {res5}"
    print("[PASS] Test 5: Bishop diagonal check (Success)")

    # Test 6: Queen อยู่แนวตรง (Check)
    b6 = """\
....
.K.Q
....
...."""
    res6 = capture_output(checkmate, b6)
    assert res6 == "Success", f"Test 6 failed: expected Success, got {res6}"
    print("[PASS] Test 6: Queen horizontal check (Success)")

    # Test 7: Bishop ถูกบังด้วย Rook (ไม่ Check)
    b7 = """\
B...
.R..
..K.
...."""
    res7 = capture_output(checkmate, b7)
    assert res7 == "Fail", f"Test 7 failed: expected Fail, got {res7}"
    print("[PASS] Test 7: Blocked Bishop ray (Fail)")

    # Test 8: กระดานไม่เป็นสี่เหลี่ยมจัตุรัส (Error)
    b8 = """\
R...
.K.....
..P.
...."""
    res8 = capture_output(checkmate, b8)
    assert res8 == "Error", f"Test 8 failed: expected Error, got {res8}"
    print("[PASS] Test 8: Invalid non-square board (Error)")

    # Test 9: ไม่มี King (Error)
    b9 = """\
R...
.P..
....
...."""
    res9 = capture_output(checkmate, b9)
    assert res9 == "Error", f"Test 9 failed: expected Error, got {res9}"
    print("[PASS] Test 9: Invalid board with no King (Error)")

    # Test 10: มี King มากกว่า 1 ตัว (Error)
    b10 = """\
R..K
.K..
....
...."""
    res10 = capture_output(checkmate, b10)
    assert res10 == "Error", f"Test 10 failed: expected Error, got {res10}"
    print("[PASS] Test 10: Invalid board with multiple Kings (Error)")

    print("\n=== 2. Running Bonus (ex01) CLI Tests ===")
    ex01_dir = os.path.join(current_dir, 'ex01')

    # CLI Test 1: รันโดยไม่มี argument (ต้องคืนการควบคุมโดยไม่พิมพ์อะไร)
    cmd = [sys.executable, 'main.py']
    p = subprocess.run(cmd, cwd=ex01_dir, capture_output=True, text=True)
    assert p.stdout.strip() == "", f"ex01 0-arg test failed: expected empty, got '{p.stdout}'"
    print("[PASS] ex01 Test 1: No arguments -> returns empty output")

    # CLI Test 2: valid_board.chess -> Success
    cmd = [sys.executable, 'main.py', 'valid_board.chess']
    p = subprocess.run(cmd, cwd=ex01_dir, capture_output=True, text=True)
    assert p.stdout.strip() == "Success", f"ex01 valid_board failed: got '{p.stdout}'"
    print("[PASS] ex01 Test 2: valid_board.chess -> Success")

    # CLI Test 3: valid_board.chess valid_board2.chess -> Success \n Success
    cmd = [sys.executable, 'main.py', 'valid_board.chess', 'valid_board2.chess']
    p = subprocess.run(cmd, cwd=ex01_dir, capture_output=True, text=True)
    expected = "Success\nSuccess"
    assert p.stdout.strip().replace('\r\n', '\n') == expected, f"ex01 2 valid boards failed: got '{p.stdout}'"
    print("[PASS] ex01 Test 3: valid_board.chess valid_board2.chess -> Success, Success")

    # CLI Test 4: invalid_board.chess -> Error
    cmd = [sys.executable, 'main.py', 'invalid_board.chess']
    p = subprocess.run(cmd, cwd=ex01_dir, capture_output=True, text=True)
    assert p.stdout.strip() == "Error", f"ex01 invalid_board failed: got '{p.stdout}'"
    print("[PASS] ex01 Test 4: invalid_board.chess -> Error")

    # CLI Test 5: invalid_board.chess valid_board2.chess -> Error \n Success
    cmd = [sys.executable, 'main.py', 'invalid_board.chess', 'valid_board2.chess']
    p = subprocess.run(cmd, cwd=ex01_dir, capture_output=True, text=True)
    expected = "Error\nSuccess"
    assert p.stdout.strip().replace('\r\n', '\n') == expected, f"ex01 invalid + valid failed: got '{p.stdout}'"
    print("[PASS] ex01 Test 5: invalid_board.chess valid_board2.chess -> Error, Success")

    # CLI Test 6: Non-existent file -> Error
    cmd = [sys.executable, 'main.py', 'nonexistent_file.chess']
    p = subprocess.run(cmd, cwd=ex01_dir, capture_output=True, text=True)
    assert p.stdout.strip() == "Error", f"ex01 missing file failed: got '{p.stdout}'"
    print("[PASS] ex01 Test 6: nonexistent_file.chess -> Error")

    print("\nAll unit tests and CLI tests passed successfully!")

if __name__ == "__main__":
    run_tests()
