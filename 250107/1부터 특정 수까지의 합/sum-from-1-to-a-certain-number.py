n = int(input())
answer = 0

for i in range(n + 1):
    answer = answer + i
    
answer = int(answer / 10)
print(answer)
