N = int(input())

commands = []
num = []

for _ in range(N):
    line = input().split()
    commands.append(line[0])
    if line[0] == 'get':
        k = int(line[1])
        print(num[k - 1])
    if line[0] == "push_back":
        num.append(int(line[1]))
    if line[0] == "pop_back":
        num.pop()
    if line[0] == 'size':
        print(len(num))
