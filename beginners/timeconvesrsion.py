N = int(input())

day = N//3600
r = N%3600
hour = r//60
r%= 60

print(f'{day}:{hour}:{r}')
