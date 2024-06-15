N = int(input())

banknotes = [100, 50, 20, 10, 5, 2, 1]

print(N)

for note in banknotes:
    count = N // note
    print(f'{count} nota(s) de R$ {note},00')
    N %= note



