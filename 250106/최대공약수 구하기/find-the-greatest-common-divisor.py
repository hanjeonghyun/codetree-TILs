n, m = map(int, input().split())

def gcd(n, m):
    a = min(n, m)
    while True:
        if n % a == 0 and m % a == 0:
            return a
        else:
            a = a - 1

print(gcd(n, m))