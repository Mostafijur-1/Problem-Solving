numbers = input().split()

A = float(numbers[0])
B = float(numbers[1])
C = float(numbers[2])

if A+B>C and B+C>A and C+A>B:
    print(f'Perimetro = {A+B+C:.1f}')
else:
    print(f'Area = {.5*(A+B)*C:.1f}')    