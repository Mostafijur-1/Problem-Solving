numbers = input().split()

a = int(numbers[0])
b = int(numbers[1])

if b%a == 0 or a%b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")    