def robinHelppss():
    t = int(input())
    
    for _ in range(t):
        n,k= map(int,input().split())
        people = list(map(int,input().split()))
        
        robinGold = 0
        peopleHelped = 0
        
        for gold in people:
            if gold == 0:
                if robinGold > 0:
                    robinGold-=1
                    peopleHelped+=1
            elif gold>=k:
                robinGold+= gold
        
        print(peopleHelped)             
                 
            


robinHelppss()                    
                    