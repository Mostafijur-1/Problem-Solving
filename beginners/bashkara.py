import math
numbers = input().split()

a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])


try:
    R1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    R2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
    
except ValueError: 
    print("Impossivel calcular")    
 
except ZeroDivisionError:
    print("Impossivel calcular")     