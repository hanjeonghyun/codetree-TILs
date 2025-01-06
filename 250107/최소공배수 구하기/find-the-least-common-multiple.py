n, m = map(int, input().split())

def common(n, m):
    a = max(n, m)
    while True:
        if a % n == 0 and a % m == 0:
            return a
        else:
            a = a + 1
            

print(common(n, m))