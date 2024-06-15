N = int(input())

year = N//365
r = N%365
month = r//30
r%= 30

print(f'{year} ano(s)')
print(f'{month} mes(es)')
print(f'{r} dia(s)')


