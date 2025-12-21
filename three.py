a = int(input("plz Enter a starter number:"))
b = int(input("plz Enter a end number:"))
for i in range(a, b+1):
    c = 0
    for j in range(1, i+1):
        if i%j == 0:
            c = c + 1
    if c == 2:
        print(i)
