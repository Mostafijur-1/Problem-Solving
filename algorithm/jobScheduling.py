arr = [
    #title,deadline,profits
    ['a',2,100],
    ['b',2,20],
    ['c',1,40],
    ['d',3,35],
    ['e',1,25],
]

n = len(arr)
t=3

for i in range(n):
    for j in range(n-1-i):
        if arr[j][2]<arr[j+1][2]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
slots = [False]*t    
jobs = ['-1']*t    

for i in range(n):
    for j in range(min(t - 1, arr[i][1] - 1),-1,-1):
        if slots[j] == False:
            slots[j] = True
            jobs[j] = arr[i][0]
            break
        
print(jobs)          