import math

Number = float(input())

N = int(math.modf(Number)[1])
n = round((Number - N) * 100)


banknotes = [100, 50, 20, 10, 5, 2]
bankcoins = [50, 25, 10, 5, 1]

print("NOTAS:")
for note in banknotes:
    count = N // note
    print(f'{count} nota(s) de R$ {note}.00')
    N %= note

print("MOEDAS:")
print(f'{N} moeda(s) de R$ 1.00')

for note in bankcoins:
    count = n // note
    print(f'{count} moeda(s) de R$ {note/100:.2f}')
    n %= note