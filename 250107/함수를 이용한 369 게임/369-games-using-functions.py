a, b = map(int, input().split())

count = 0

for i in range(a, b + 1):
    if (str(3) in str(i) or str(6) in str(i) or str(9) in str(i)) or i % 3 == 0:
        count = count + 1

print(count)    