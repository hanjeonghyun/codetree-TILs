n = int(input())
i = 1

for _ in range(n):
    for _ in range(n):
        print(i)
        i = i + 1 % 10