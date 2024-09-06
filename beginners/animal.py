n1 = float(input().split()[0])
n2 = float(input().split()[0])
n3 = float(input().split()[0])
n4 = float(input().split()[0])
n5 = float(input().split()[0])
n6 = float(input().split()[0])

n = [n1, n2, n3,n4,n5,n6]

count = 0
for number in n:
    if number > 0:
        count += 1

print(count)