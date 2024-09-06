n = float(input())

if(n<0 or n>100):
    print("Fora de intervalo")
    
elif(0<=n<=25.0000):
    print("Intervalo [0,25]")    
    
elif(25.00001<n<=50.000000):
    print("Intervalo (25,50]")      
    
elif(50.00001<n<=75.000000):
    print("Intervalo (50,70]")
else:
    print("Intervalo (75,100]")           