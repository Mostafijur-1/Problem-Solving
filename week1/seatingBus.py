def checkRecommendation(n,seats):
    occupied = set()
    occupied.add(seats[0])
    
    for i in range(1,n):
        seat = seats[i]
        if (seat - 1 in occupied) or (seat +1  in occupied):
            occupied.add(seat)
        else:
            return "NO"    
        
    return "YES"
        



t = int(input())
for _ in range(t):
    n = int(input())
    seats = list(map(int,input().split()))
    print(checkRecommendation(n,seats))    