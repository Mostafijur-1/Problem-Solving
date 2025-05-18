def generateImportantNumbers():
    importantNumbers = set()
    for x in range(2,100):
        importantNumber = int(f"10{x}")
        if(importantNumber<=10000):
            importantNumbers.add(importantNumber)
    return importantNumbers




t = int(input())
numbers = [int(input()) for _ in range(t)]

importantNumbers = generateImportantNumbers()    

for num in numbers:
    if num in importantNumbers:
        print("YES")
    else:
        print("NO")    