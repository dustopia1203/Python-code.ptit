for _ in range(int(input())):
    a = sorted(input())
    b = sorted(input())
    check = "YES" if a == b else "NO"
    print(f"Test {_ + 1}: {check}")
