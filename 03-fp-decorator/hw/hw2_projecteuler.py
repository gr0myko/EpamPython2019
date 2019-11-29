d = [a * b * c
     for a in range(1, int(1000/3) + 1)
     for b in range(a + 1, int(1000/2) + 1)
     for c in range(b + 1, (1001 - a - b))
     if a + b + c == 1000 and a**2 + b**2 == c**2]
print(d)
