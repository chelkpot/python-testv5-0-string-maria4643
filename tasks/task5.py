# tasks/task5.py

def solve():
    chars = input().split()
    for c in chars:
        print(f"Код символа {c} равен {ord(c)}")

if __name__ == "__main__":
    solve()