item = input().split()

X = int(item[0])
Y = int(item[1])

price = 0.0
if(X==1):
    price = 4.00
elif(X==2):
    price = 4.50   
elif(X==3):
    price = 5.00  
elif(X==4):
    price = 2.00 
elif(X==5):
    price = 1.50             
    
    
print(f'Total: R$ {price*Y:.2f}')    