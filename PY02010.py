t = int(input())
while t > 0:
    m = 1e18
    M = -1e18
    for i in range(0, t):
        x = int(input())
        m = min(m, x)
        M = max(M, x)
    print(f"{m} {M}" if M != m else "BANG NHAU")
    t = int(input())
