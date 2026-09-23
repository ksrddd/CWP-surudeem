#!/usr/bin/env python3
import sys
import os
from checkmate import checkmate

def main():
    # หากไม่มี argument ส่งเข้ามา ให้จบการทำงานและคืนการควบคุมให้ผู้ใช้ (prints nothing)
    if len(sys.argv) < 2:
        return

    # วนลูปตรวจสอบไฟล์กระดานตาม arguments ที่ส่งเข้ามาทีละไฟล์
    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print("Error")
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            checkmate(content)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
