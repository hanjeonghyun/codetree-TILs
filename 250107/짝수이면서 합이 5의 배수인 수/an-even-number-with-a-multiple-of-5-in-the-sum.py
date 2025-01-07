n = int(input())
def getEven(n):
    a, b = list(str(n))
    if n % 2 == 0 and (int(a) + int(b)) % 5 == 0:
        return "Yes"
    else:
        return "No"

print(getEven(n))