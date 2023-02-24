n = int(input())
contador = 0
while contador < n:
    x = int(input())
    if x % 2 == 0 and x > 0:
        print("EVEN POSITIVE")
    if x % 2 == 0 and x < 0:
        print("EVEN NEGATIVE")
    if x % 2 == 1 and x > 0:
        print("ODD POSITIVE")
    if x % 2 == 1 and x < 0:
        print("ODD NEGATIVE")
    if x == 0:
        print("NULL")
    contador = contador + 1